import pygame, sys
from pygame.locals import *
import random, time 
 
pygame.init()

 #Setting up FPS 
FPS = 60
FramePerSec = pygame.time.Clock()
 
# Predefined some colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
 
# Screen information
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0
COINS = 0
COINS_FOR_SPEED_UP = 5  # каждые N монет увеличиваем скорость врага
speed_level = 0         # сколько раз уже ускорялись из-за монет

#Setting up fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK) #renderncreate the graphics for the Font of our choice
background = pygame.image.load("AnimatedStreet.png")
 
 #Create a white screen 
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")
 
 
class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Enemy.png") #load enemy picture
        self.rect = self.image.get_rect() ## make box around the picture
        self.rect.center=(random.randint(40,SCREEN_WIDTH-40),0) #put enemy at random place on top
 
      def move(self): # move the enemy
        global SCORE
        self.rect.move_ip(0,SPEED) # move down by 10 pixels
        if (self.rect.bottom > SCREEN_HEIGHT):  # if enemy goes off screen
            SCORE+=1
            self.rect.top = 0  # send back to top
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

 
class Player(pygame.sprite.Sprite): #this makes a player
    def __init__(self):
        super().__init__()  # start the sprite
        self.image = pygame.image.load("Player.png")  # get the picture
        self.rect = self.image.get_rect() # make a box around it
        self.rect.center = (160, 520)  # put it on the screen
 
    def move(self):  # moves the player
        pressed_keys = pygame.key.get_pressed()  # check which keys are pressed
       #if pressed_keys[K_UP]:  # move up
            #self.rect.move_ip(0, -5)
       #if pressed_keys[K_DOWN]: # move down
            #self.rect.move_ip(0,5)
         
        if self.rect.left > 0:  # stop going off left side
              if pressed_keys[K_LEFT]:  # move left
                  self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:        # stop going off right side
              if pressed_keys[K_RIGHT]: # move right
                  self.rect.move_ip(5, 0) #moves the player box (x = left/right, y = up/down)

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.value = random.choice([1, 2, 3]) #вес монеты
        self.image = pygame.image.load("Coin.png")   
        size = 15 + self.value * 5  # чем "тяжелее" монета, тем она крупнее и заметнее
        self.image = pygame.transform.scale(self.image, (size, size))

        self.rect = self.image.get_rect() # Прямоугольник монеты
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)     # Появляется в случайной точке по горизонтали сверху
        self.speed = 3 + self.value  # Скорость падения, "тяжелые" монеты падают чуть быстрее

    def move(self):
        self.rect.move_ip(0, self.speed) # Двигаем монету вниз
        if self.rect.top > SCREEN_HEIGHT: # Если монета ушла за экран удаляем спрайты
            self.kill()
 
#Setting up Sprites        
P1 = Player()
E1 = Enemy()
 
#Creating Sprites Groups
enemies = pygame.sprite.Group() # make a group for enemies
enemies.add(E1) # add enemy to that group

all_sprites = pygame.sprite.Group()  # make group for all sprites
all_sprites.add(P1)  # add player
all_sprites.add(E1) # add enemy

coins = pygame.sprite.Group() #группа моент 
 
#Adding a new User event 
INC_SPEED = pygame.USEREVENT + 1  # make our own event (user event)
pygame.time.set_timer(INC_SPEED, 1000) #run this event every 1 second
COIN_EVENT = pygame.USEREVENT + 2
pygame.time.set_timer(COIN_EVENT, 1200)
 
#Game Loop
while True:   # game loop runs forever
       
    for event in pygame.event.get():
        if event.type == COIN_EVENT: # периодически создаём новую монету
            c = Coin()
            coins.add(c)
            all_sprites.add(c)
        if event.type == QUIT: 
            pygame.quit()  # Закрытие окна
            sys.exit()

    DISPLAYSURF.blit(background, (0,0))  # draw background first

    scores = font_small.render(str(SCORE), True, BLACK) # make text with SCORE
    DISPLAYSURF.blit(scores, (10,10))  # show SCORE on screen

    coins_text = font_small.render(str(COINS), True, BLACK)
    DISPLAYSURF.blit(coins_text, (SCREEN_WIDTH - coins_text.get_width() - 10, 10))
 
    #Moves and Re-draws all Sprites
    for entity in all_sprites:  #loop through all sprites
        DISPLAYSURF.blit(entity.image, entity.rect) #draw sprite
        entity.move() #move sprite

#столкновение с монетами
    hits = pygame.sprite.spritecollide(P1, coins, dokill=True)
    if hits:
        for coin in hits:
            COINS += coin.value  # Увеличиваем количество монет с учётом их веса

            current_level = COINS // COINS_FOR_SPEED_UP  #проверяем не пора ли ускорить врага
        # Каждый раз когда мы переходим новый "уровень" по монетам увеличиваем скорость
        if current_level > speed_level:
            speed_level = current_level
            SPEED += 1  # ускоряем всех врагов 
    
 
    #To be run if collision occurs between Player and Enemy
    if pygame.sprite.spritecollideany(P1, enemies): #checks if player touches any enemy
          pygame.mixer.Sound('crash.wav').play()
          time.sleep(0.5)

          DISPLAYSURF.fill(RED)  #make screen red
          DISPLAYSURF.blit(game_over, (30,250)) # show "Game Over" text

          pygame.display.update()
          for entity in all_sprites:  #go through all sprites
                entity.kill()  #remove them

          time.sleep(2)  #wait 2 seconds
          pygame.quit()  #close game
          sys.exit()        #stop program
          
    pygame.display.update()
    FramePerSec.tick(FPS)
