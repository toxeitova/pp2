
import pygame
import time
import random
import psycopg2


def connect_db():
    return psycopg2.connect(
        dbname="suppliers",
        user="postgres",
        password="123",   
        host="localhost",
        port="5432"
    )


def init_tables():
    conn = connect_db()
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            username VARCHAR(50) UNIQUE NOT NULL
        );
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS user_score (
            id SERIAL PRIMARY KEY,
            user_id INTEGER REFERENCES users(id),
            score INTEGER DEFAULT 0,
            level INTEGER DEFAULT 1,
            snake_body TEXT,
            snake_position TEXT,
            direction VARCHAR(10)
        );
    """)

    conn.commit()
    conn.close()


def get_or_create_user(username):
    conn = connect_db()
    cur = conn.cursor()

    cur.execute("SELECT id FROM users WHERE username=%s", (username,))
    result = cur.fetchone()

    if result:
        user_id = result[0]
    else:
        cur.execute("INSERT INTO users(username) VALUES (%s) RETURNING id", (username,))
        user_id = cur.fetchone()[0]
        conn.commit()

    conn.close()
    return user_id


def load_saved_game(user_id):
    conn = connect_db()
    cur = conn.cursor()

    cur.execute("""
        SELECT score, level, snake_body, snake_position, direction 
        FROM user_score WHERE user_id=%s ORDER BY id DESC LIMIT 1
    """, (user_id,))
    row = cur.fetchone()

    conn.close()
    return row


def save_game(user_id, score, level, snake_body, snake_position, direction):
    conn = connect_db()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO user_score(user_id, score, level, snake_body, snake_position, direction)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (user_id, score, level, str(snake_body), str(snake_position), direction))

    conn.commit()
    conn.close()



#функции игры
def calculate_level(score):
    if score < 100:
        return 1
    elif score < 250:
        return 2
    else:
        return 3

pygame.init()

snake_speed = 15
window_x = 720
window_y = 480

black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
yellow = pygame.Color(255, 255, 0)

pygame.display.set_caption('Snake')
game_window = pygame.display.set_mode((window_x, window_y))
fps = pygame.time.Clock()

#food
food_types = [
    {"color": white,  "score": 10, "lifetime": 5},
    {"color": yellow, "score": 20, "lifetime": 4},
    {"color": red,    "score": 40, "lifetime": 3}
]

def spawn_food():
    f = random.choice(food_types)
    pos = [random.randrange(1, window_x//10)*10,
           random.randrange(1, window_y//10)*10]
    return pos, f, time.time()

level_walls = {
    1: [],
    2: [(200,200), (210,200), (220,200), (230,200), (240,200)],
    3: [(100,100), (110,100), (120,100), (130,100),
        (300,300), (310,300), (320,300)]
}



init_tables()  # авто-создание таблиц

username = input("Enter your username: ")

user_id = get_or_create_user(username)
saved = load_saved_game(user_id)

if saved:
    print("Saved game found!")
    score, level, snake_body_str, snake_pos_str, direction = saved
    snake_body = eval(snake_body_str)
    snake_position = eval(snake_pos_str)
else:
    print("Starting new game!")
    score = 0
    level = 1
    snake_position = [100, 50]
    snake_body = [[100, 50], [90, 50], [80, 50], [70, 50]]
    direction = "RIGHT"

snake_speed = {1: 10, 2: 15, 3: 20}[level]
change_to = direction

fruit_position, current_food, fruit_spawn_time = spawn_food()

walls = level_walls[level] #walls for current level

def show_score():
    font = pygame.font.SysFont('times new roman', 20)
    s = font.render(f"Score: {score} | Level: {level}", True, white)
    game_window.blit(s, (0, 0))


def pause_game():
    paused = True
    font = pygame.font.SysFont('times new roman', 40)
    text = font.render("Paused - Press P to Resume", True, white)

    save_game(user_id, score, level, snake_body, snake_position, direction)
    print("Game saved!")

    while paused:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    paused = False

        game_window.blit(text, (100, 200))
        pygame.display.update()


def game_over():
    save_game(user_id, score, level, snake_body, snake_position, direction)
    print("Game saved on exit.")

    font = pygame.font.SysFont('times new roman', 50)
    text = font.render(f"Your Score: {score}", True, red)
    game_window.blit(text, (200, 150))
    pygame.display.flip()
    time.sleep(2)
    pygame.quit()
    quit()


#osnovnoi цикл
while True:

    # ввод
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP: change_to = "UP"
            if event.key == pygame.K_DOWN: change_to = "DOWN"
            if event.key == pygame.K_LEFT: change_to = "LEFT"
            if event.key == pygame.K_RIGHT: change_to = "RIGHT"
            if event.key == pygame.K_p: pause_game()

    # неправильные движения
    if change_to == 'UP' and direction != 'DOWN': direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP': direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT': direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT': direction = 'RIGHT'

    # движение змейки
    if direction == 'UP': snake_position[1] -= 10
    if direction == 'DOWN': snake_position[1] += 10
    if direction == 'LEFT': snake_position[0] -= 10
    if direction == 'RIGHT': snake_position[0] += 10

    snake_body.insert(0, list(snake_position))

    # eat food
    if snake_position == fruit_position:
        score += current_food["score"]
        level = calculate_level(score)
        snake_speed = {1: 10, 2: 15, 3: 20}[level]
        walls = level_walls[level]
        fruit_position, current_food, fruit_spawn_time = spawn_food()
    else:
        snake_body.pop()

    # food lifetime
    if time.time() - fruit_spawn_time > current_food["lifetime"]:
        fruit_position, current_food, fruit_spawn_time = spawn_food()

    # death condiions
    if (
        snake_position[0] < 0 or snake_position[0] > window_x - 10 or
        snake_position[1] < 0 or snake_position[1] > window_y - 10 or 
        snake_position in snake_body[1:] or
        tuple(snake_position) in walls
    ):
        game_over()


    # draw
    game_window.fill(black)
    #draw snake
    for pos in snake_body:
        pygame.draw.rect(game_window, green, pygame.Rect(pos[0], pos[1], 10, 10))
    
    for wx, wy in walls:
        pygame.draw.rect(game_window, gray, pygame.Rect(wx, wy, 10, 10))

    pygame.draw.rect(game_window, current_food["color"], pygame.Rect(
        fruit_position[0], fruit_position[1], 10, 10))

    show_score()
    pygame.display.update()
    fps.tick(snake_speed)
