#B(кисть), T(прямоугольник), C(круг), E(eraser)
#R — красный, G — зелёный, B — синий, Y — жёлтый, W — белый, K — чёрный

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

    while True:  # главный цикл программ
        pressed = pygame.key.get_pressed()  # проверяем все нажатые клавиши

        for event in pygame.event.get():  # перебираем события

            if event.type == pygame.QUIT:  # если нажали закрыть окно
                return

            if event.type == pygame.KEYDOWN:  # обработка нажатия клавиш

                if event.key == pygame.K_b: tool = 'BRUSH'
                if event.key == pygame.K_t: tool = 'RECT'
                if event.key == pygame.K_c: tool = 'CIRCLE'
                if event.key == pygame.K_e: tool = 'ERASER'


                if event.key == pygame.K_s: tool = 'SQUARE'          # квадрат
                if event.key == pygame.K_r: tool = 'RIGHT_TRIANGLE'       # прямоугольный треугольник
                if event.key == pygame.K_q: tool = 'EQUILATERAL_TRIANGLE'# равносторонний треугольник
                if event.key == pygame.K_h: tool = 'RHOMBUS'         # ромб

                # выбираем цвет
                if event.key == pygame.K_r: color = (255, 0, 0)  # красный
                if event.key == pygame.K_g: color = (0, 255, 0) # зелёный
                if event.key == pygame.K_b: color = (0, 0, 255) # синий
                if event.key == pygame.K_y: color = (255, 255, 0)  # жёлтый
                if event.key == pygame.K_w: color = (255, 255, 255) # белый
                if event.key == pygame.K_k: color = (0, 0, 0)  # чёрный
            
            # когда нажали кнопку мыши
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # левая кнопка
                    radius = min(200, radius + 1) # делаем кисть толще
                    drawing = True  # начинаем рисовать
                    start_pos = event.pos # сохраняем точку начала
                    last_pos = event.pos  # последняя точка = текущая
                    preview_end = event.pos # конец фигуры = точка начала

                elif event.button == 3:  # правая кнопка
                    radius = max(1, radius - 1) # уменьшаем толщину
            
           # движение мыши
            if event.type == pygame.MOUSEMOTION:
                if drawing: # если мышь зажата
                    if tool == 'BRUSH':
                        pygame.draw.line(canvas, color, last_pos, event.pos, radius * 2)
                        last_pos = event.pos
                    elif tool == 'ERASER':
                        pygame.draw.line(canvas, (0, 0, 0), last_pos, event.pos, radius * 2)
                        last_pos = event.pos
                    else:
                        preview_end = event.pos

    
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                if drawing:
                    end_pos = event.pos

                    if tool == 'RECT':
                        pygame.draw.rect(canvas, color, rect_from_points(start_pos, end_pos), max(1, radius // 2))

                    elif tool == 'CIRCLE':
                        r = int(math.hypot(end_pos[0]-start_pos[0], end_pos[1]-start_pos[1]))
                        pygame.draw.circle(canvas, color, start_pos, r, max(1, radius // 2))

                    # квадрат
                    elif tool == 'SQUARE':
                        pygame.draw.rect(canvas, color, square_from_points(start_pos, end_pos), max(1, radius // 2))

                    # прямоугольный треугольник
                    elif tool == 'RIGHT_TRIANGLE':
                        pygame.draw.polygon(canvas, color, right_triangle(start_pos, end_pos), max(1, radius // 2))

                    # равносторонний треугольник
                    elif tool == 'EQUILATERAL_TRIANGLE':
                        pygame.draw.polygon(canvas, color, equilateral_triangle(start_pos, end_pos), max(1, radius // 2))

                    # ромб
                    elif tool == 'RHOMBUS':
                        pygame.draw.polygon(canvas, color, rhombus(start_pos, end_pos), max(1, radius // 2))

                drawing = False
                start_pos = None
                last_pos = None
                preview_end = None
        
       
        screen.blit(canvas, (0, 0))

        # предпросмотр фигур
        if drawing and start_pos and preview_end and tool in (
            'RECT', 'CIRCLE', 'SQUARE', 'RIGHT_TRIANGLE', 'EQUILATERAL_TRIANGLE', 'RHOMBUS'
        ):
            if tool == 'RECT':
                pygame.draw.rect(screen, color, rect_from_points(start_pos, preview_end), max(1, radius // 2))

            elif tool == 'CIRCLE':
                r = int(math.hypot(preview_end[0]-start_pos[0], preview_end[1]-start_pos[1]))
                pygame.draw.circle(screen, color, start_pos, r, max(1, radius // 2))

            elif tool == 'SQUARE':
                pygame.draw.rect(screen, color, square_from_points(start_pos, preview_end), max(1, radius // 2))

            elif tool == 'RIGHT_TRIANGLE':
                pygame.draw.polygon(screen, color, right_triangle(start_pos, preview_end), max(1, radius // 2))

            elif tool == 'EQUILATERAL_TRIANGLE':
                pygame.draw.polygon(screen, color, equilateral_triangle(start_pos, preview_end), max(1, radius // 2))

            elif tool == 'RHOMBUS':
                pygame.draw.polygon(screen, color, rhombus(start_pos, preview_end), max(1, radius // 2))

        pygame.display.flip()
        clock.tick(60)


# прямоугольник
def rect_from_points(a, b): # прямоугольник из двух точек
    x1, y1 = a  # точка A
    x2, y2 = b  # точка B
    return pygame.Rect(min(x1,x2), min(y1,y2), abs(x2-x1), abs(y2-y1))

# квадрат
def square_from_points(a, b):
    size = max(abs(b[0]-a[0]), abs(b[1]-a[1])) # сторона квадрата
    return pygame.Rect(a[0], a[1], size, size)

# прямоугольный треугольник
def right_triangle(a, b):
    return [a, (b[0], a[1]), b] # три точки треугольника

# равносторонний треугольник
def equilateral_triangle(a, b):
    x1, y1 = a
    side = abs(b[0] - x1) # длина стороны
    h = side * (3**0.5) / 2  # высота
    return [(x1, y1), (x1 + side, y1), (x1 + side/2, y1 - h)]

# ромб
def rhombus(a, b):
    cx = (a[0] + b[0]) // 2 # центр по Х
    cy = (a[1] + b[1]) // 2 # центр по Y
    return [(cx, a[1]), (b[0], cy), (cx, b[1]), (a[0], cy)] # 4 точки ромба

main()
