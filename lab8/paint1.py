import pygame
import math

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()
    
    # холст, на который рисуем (чтобы рисунок сохранялся между кадрами)
    canvas = pygame.Surface(screen.get_size()).convert()
    canvas.fill((0, 0, 0))

    radius = 15
    tool = 'BRUSH'              # BRUSH | RECT | CIRCLE | ERASER
    color = (0, 0, 255)         # текущий цвет
    drawing = False
    start_pos = None
    last_pos = None
    preview_end = None

    while True:
        pressed = pygame.key.get_pressed()
        alt_held  = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]
        
        for event in pygame.event.get():
            # выход
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held: return
                if event.key == pygame.K_F4 and alt_held: return
                if event.key == pygame.K_ESCAPE: return

                # инструменты
                if event.key == pygame.K_b: tool = 'BRUSH'
                if event.key == pygame.K_t: tool = 'RECT'
                if event.key == pygame.K_c: tool = 'CIRCLE'
                if event.key == pygame.K_e: tool = 'ERASER'

                # выбор цвета
                if event.key == pygame.K_r: color = (255, 0, 0)
                if event.key == pygame.K_g: color = (0, 255, 0)
                if event.key == pygame.K_b: color = (0, 0, 255)
                if event.key == pygame.K_y: color = (255, 255, 0)
                if event.key == pygame.K_w: color = (255, 255, 255)
                if event.key == pygame.K_k: color = (0, 0, 0)
            
            # управление толщиной и старт рисования
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # лкм: толще + начать рисовать
                    radius = min(200, radius + 1)
                    drawing = True
                    start_pos = event.pos
                    last_pos = event.pos
                    preview_end = event.pos
                elif event.button == 3:  # пкм: тоньше
                    radius = max(1, radius - 1)
            
            if event.type == pygame.MOUSEMOTION:
                if drawing:
                    if tool == 'BRUSH':
                        pygame.draw.line(canvas, color, last_pos, event.pos, radius * 2)
                        last_pos = event.pos
                    elif tool == 'ERASER':
                        pygame.draw.line(canvas, (0, 0, 0), last_pos, event.pos, radius * 2)
                        last_pos = event.pos
                    else:
                        preview_end = event.pos  # для предпросмотра прямоугольника/круга

            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                if drawing:
                    end_pos = event.pos
                    if tool == 'RECT':
                        rect = rect_from_points(start_pos, end_pos)
                        pygame.draw.rect(canvas, color, rect, max(1, radius // 2))
                    elif tool == 'CIRCLE':
                        r = int(math.hypot(end_pos[0] - start_pos[0], end_pos[1] - start_pos[1]))
                        pygame.draw.circle(canvas, color, start_pos, r, max(1, radius // 2))
                drawing = False
                start_pos = None
                last_pos = None
                preview_end = None
                
        # рендер
        screen.blit(canvas, (0, 0))

        # предпросмотр фигур во время перетаскивания
        if drawing and start_pos and preview_end and tool in ('RECT', 'CIRCLE'):
            if tool == 'RECT':
                rect = rect_from_points(start_pos, preview_end)
                pygame.draw.rect(screen, color, rect, max(1, radius // 2))
            elif tool == 'CIRCLE':
                r = int(math.hypot(preview_end[0] - start_pos[0], preview_end[1] - start_pos[1]))
                pygame.draw.circle(screen, color, start_pos, r, max(1, radius // 2))
        
        pygame.display.flip()
        clock.tick(60)

def rect_from_points(a, b):
    x1, y1 = a
    x2, y2 = b
    left = min(x1, x2)
    top = min(y1, y2)
    w = abs(x2 - x1)
    h = abs(y2 - y1)
    return pygame.Rect(left, top, w, h)

main()
