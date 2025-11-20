# importing libraries
import pygame
import time
import random

snake_speed = 15 # скорость змейки

# Window size
window_x = 720
window_y = 480

# defining colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
yellow = pygame.Color(255, 255, 0)

pygame.init()
pygame.display.set_caption('Snake')
game_window = pygame.display.set_mode((window_x, window_y))  # создаём окно
fps = pygame.time.Clock()  # таймер FPS

# начальная позиция змейки
snake_position = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50], [70, 50]]

direction = 'RIGHT' # текущее направление
change_to = direction # направление куда хотим повернуть

score = 0 # очки

# food types: color, score added, lifetime
food_types = [
    {"color": white,  "score": 10, "lifetime": 5},
    {"color": yellow, "score": 20, "lifetime": 4},
    {"color": red,    "score": 40, "lifetime": 3}
]

# функция появления еды
def spawn_food():
    f = random.choice(food_types)  # выбираем случайный тип еды
    pos = [random.randrange(1, window_x // 10) * 10,
           random.randrange(1, window_y // 10) * 10] # случайная позиция
    return pos, f, time.time() # возвращаем позицию, еду и время появления

# первое появление еды
fruit_position, current_food, fruit_spawn_time = spawn_food()

# функция показа счёта
def show_score(color, font, size):
    font_obj = pygame.font.SysFont(font, size) # создаём шрифт
    surface = font_obj.render(f"Score : {score}", True, color) # сам текст
    game_window.blit(surface, surface.get_rect())  # выводим на экран

# функция завершения игры
def game_over():
    my_font = pygame.font.SysFont('times new roman', 50)
    game_over_surface = my_font.render(
        f'Your Score is : {score}', True, red)
    game_window.blit(game_over_surface, game_over_surface.get_rect(center=(window_x/2, window_y/4)))
    pygame.display.flip()
    time.sleep(2)
    pygame.quit()
    quit()

# main loop
while True:

   # обработка клавиш
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP: change_to = 'UP'
            if event.key == pygame.K_DOWN: change_to = 'DOWN'
            if event.key == pygame.K_LEFT: change_to = 'LEFT'
            if event.key == pygame.K_RIGHT: change_to = 'RIGHT'

     # запрещаем поворот в противоположную сторону
    if change_to == 'UP' and direction != 'DOWN': direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP': direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT': direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT': direction = 'RIGHT'

    # движение змейки
    if direction == 'UP': snake_position[1] -= 10
    if direction == 'DOWN': snake_position[1] += 10
    if direction == 'LEFT': snake_position[0] -= 10
    if direction == 'RIGHT': snake_position[0] += 10

    snake_body.insert(0, list(snake_position)) # добавляем новую голову

    # проверяем, съели ли еду
    if snake_position == fruit_position:
        score += current_food["score"] # добавляем очки
        fruit_position, current_food, fruit_spawn_time = spawn_food() # новая еда
    else:
        snake_body.pop() # удаляем хвост, если не ели

   # еда исчезает через время
    if time.time() - fruit_spawn_time > current_food["lifetime"]:
        fruit_position, current_food, fruit_spawn_time = spawn_food()
    # выход за границы = проигрыш
    if snake_position[0] < 0 or snake_position[0] > window_x - 10: game_over()
    if snake_position[1] < 0 or snake_position[1] > window_y - 10: game_over()

    # столкновение с собой
    if snake_position in snake_body[1:]:
        game_over()

   # закрашиваем фон
    game_window.fill(black)

    # рисуем змейку
    for pos in snake_body:
        pygame.draw.rect(game_window, green, pygame.Rect(pos[0], pos[1], 10, 10))

    # рисуем еду
    pygame.draw.rect(game_window, current_food["color"],
                     pygame.Rect(fruit_position[0], fruit_position[1], 10, 10))

    # рисуем счёт
    show_score(white, 'times new roman', 20)

    pygame.display.update()  # обновляем экран
    fps.tick(snake_speed) # скорость игры
