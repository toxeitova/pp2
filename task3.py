import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Red Ball")

x = 400
y = 300
radius = 25
step = 20

cnt = 0
while True:
    if cnt % 100 == 0:
        print(cnt)

    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, (255, 0, 0), (x, y), radius)
    pygame.display.update()

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if x - step - radius >= 0:
                    x -= step
            if event.key == pygame.K_RIGHT:
                if x + step + radius <= 800:
                    x += step
            if event.key == pygame.K_UP:
                if y - step - radius >= 0:
                    y -= step
            if event.key == pygame.K_DOWN:
                if y + step + radius <= 600:
                    y += step
            if event.key == pygame.K_ESCAPE:
                exit(0)

    cnt += 1
