import pygame
import sys
import math

pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Simple Paint')

white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
gray = (200, 200, 200)

canvas = pygame.Surface((width, height))
canvas.fill(white)

class Button:
    def __init__(self, x, y, width, height, text, color, action):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.action = action

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        font = pygame.font.Font(None, 30)
        text_surface = font.render(self.text, True, white)
        screen.blit(text_surface, (self.rect.x + 10, self.rect.y + 5))

    def check_action(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos):
            self.action()

drawing = False
circle_mode = False
rect_mode = False
eraser_mode = False
square_mode = False
right_triangle_mode = False
equilateral_triangle_mode = False
rhombus_mode = False

brush_color = black

circle_start = None
circle_radius = 0
rect_start = None

def set_black():
    global brush_color, eraser_mode
    brush_color = black
    eraser_mode = False

def set_green():
    global brush_color, eraser_mode
    brush_color = green
    eraser_mode = False

def set_red():
    global brush_color, eraser_mode
    brush_color = red
    eraser_mode = False

def set_blue():
    global brush_color, eraser_mode
    brush_color = blue
    eraser_mode = False

def clear_screen():
    canvas.fill(white)
    pygame.display.flip()

def exit_app():
    pygame.quit()
    sys.exit()

def toggle_circle_mode():
    global circle_mode, rect_mode, eraser_mode, square_mode, right_triangle_mode, equilateral_triangle_mode, rhombus_mode
    circle_mode = True
    rect_mode = False
    eraser_mode = False
    square_mode = False
    right_triangle_mode = False
    equilateral_triangle_mode = False
    rhombus_mode = False

def toggle_rect_mode():
    global rect_mode, circle_mode, eraser_mode, square_mode, right_triangle_mode, equilateral_triangle_mode, rhombus_mode
    rect_mode = True
    circle_mode = False
    eraser_mode = False
    square_mode = False
    right_triangle_mode = False
    equilateral_triangle_mode = False
    rhombus_mode = False

def toggle_eraser_mode():
    global eraser_mode, circle_mode, rect_mode, brush_color, square_mode, right_triangle_mode, equilateral_triangle_mode, rhombus_mode
    eraser_mode = not eraser_mode
    circle_mode = False
    rect_mode = False
    square_mode = False
    right_triangle_mode = False
    equilateral_triangle_mode = False
    rhombus_mode = False
    brush_color = white if eraser_mode else black

buttons = [
    Button(10, 10, 60, 30, 'Black', black, set_black),
    Button(80, 10, 60, 30, 'Green', green, set_green),
    Button(150, 10, 60, 30, 'Red', red, set_red),
    Button(220, 10, 60, 30, 'Blue', blue, set_blue),
    Button(290, 10, 60, 30, 'Clear', gray, clear_screen),
    Button(380, 10, 60, 30, 'Exit', gray, exit_app),
    Button(470, 10, 80, 30, "Circle", gray, toggle_circle_mode),
    Button(570, 10, 80, 30, "Rectangle", gray, toggle_rect_mode),
    Button(670, 10, 80, 30, "Eraser", gray, toggle_eraser_mode),
]

while True:
    screen.fill(white)
    screen.blit(canvas, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_app()

        for button in buttons:
            button.check_action(event)

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if circle_mode:
                    circle_start = pygame.mouse.get_pos()
                    circle_radius = 0
                elif rect_mode:
                    rect_start = pygame.mouse.get_pos()
                else:
                    drawing = True

        if event.type == pygame.MOUSEMOTION:
            screen.blit(canvas, (0, 0))  # 重新绘制画布以避免重复轨迹
            mouse_x, mouse_y = pygame.mouse.get_pos()

            if drawing and not eraser_mode:
                pygame.draw.circle(canvas, brush_color, (mouse_x, mouse_y), 5)
            elif eraser_mode:
                pygame.draw.circle(canvas, white, (mouse_x, mouse_y), 10)

            if circle_mode and circle_start:
                circle_radius = int(math.hypot(mouse_x - circle_start[0], mouse_y - circle_start[1]))
                pygame.draw.circle(screen, brush_color, circle_start, circle_radius, 2)

            if rect_mode and rect_start:
                rect_end = pygame.mouse.get_pos()
                x1, y1 = rect_start
                x2, y2 = rect_end
                pygame.draw.rect(screen, brush_color, (min(x1, x2), min(y1, y2), abs(x2 - x1), abs(y2 - y1)), 2)

        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                drawing = False

                if circle_mode and circle_start:
                    pygame.draw.circle(canvas, brush_color, circle_start, circle_radius, 2)
                    circle_start = None

                if rect_mode and rect_start:
                    rect_end = pygame.mouse.get_pos()
                    x1, y1 = rect_start
                    x2, y2 = rect_end
                    pygame.draw.rect(canvas, brush_color, (min(x1, x2), min(y1, y2), abs(x2 - x1), abs(y2 - y1)), 2)
                    rect_start = None

    pygame.draw.rect(screen, gray, (0, 0, width, 90))  
    for button in buttons:
        button.draw(screen)

    pygame.display.flip()
