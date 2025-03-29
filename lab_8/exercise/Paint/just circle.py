import pygame
import sys

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

# 画布（存储绘制内容）
canvas = pygame.Surface((width, height))
canvas.fill(white)

# set the button
class Button:
    def __init__(self, x, y, width, height, text, color, action):
        self.rect = pygame.Rect(x, y, width, height)
        self.text= text
        self.color = color
        self.action = action
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        font = pygame.font.Font(None, 30)
        text_surface = font.render(self.text, True, white)
        screen.blit(text_surface, (self.rect.x + 12, self.rect.y + 12))
    def check_action(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.action()

# tools
drawing = False
circle_mode = False
brush_color = black
circle_start = None
circle_radius = 0
circles = []

# color selctions
def set_black():
    global brush_color
    brush_color = black
def set_green():
    global brush_color
    brush_color = green
def set_red():
    global brush_color
    brush_color = red
def set_blue():
    global brush_color
    brush_color = blue

# clear the canvas with clear button
def clear_screen():
    global circles  # Also clear the saved circles
    canvas.fill(white)
    circles = []  # clear all circles
    screen.fill(white)  # refresh the canvas
    pygame.display.flip()

# exit button
def exit_app():
    pygame.quit()
    sys.exit()

#  circle button 
def toggle_circle_mode():
    global circle_mode
    circle_mode = not circle_mode

# the information of buttons
buttons = [
    Button(10, 10, 60, 30, 'Black', black, set_black),
    Button(80, 10, 60, 30, 'Green', green, set_green),
    Button(150, 10, 60, 30, 'Red', red, set_red),
    Button(220, 10, 60, 30, 'Blue', blue, set_blue),
    Button(290, 10, 60, 30, 'Clear', gray, clear_screen),  
    Button(380, 10, 60, 30, 'Exit', gray, exit_app), 
    Button(470, 10, 60, 30, "Circle", blue, toggle_circle_mode)
    
]


while True:
    screen.fill(white)  # Refill Background
    screen.blit(canvas, (0, 0))  # redraw

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_app()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if circle_mode:
                    circle_start = pygame.mouse.get_pos()
                    circle_radius = 0  # draw the circle
                else:
                    drawing = True

        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                drawing = False
                if circle_mode and circle_start:
                    circles.append((circle_start, circle_radius, brush_color))
                    pygame.draw.circle(canvas, brush_color, circle_start, circle_radius, 2)
                    circle_start = None
                    circle_radius = 0

        # check the buttons
        for button in buttons:
            button.check_action(event)

    # Brush mode: Hold down the left mouse button to draw 
    if drawing:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if mouse_y > 50:  # 避免绘制在按钮栏上 Avoid drawing over button bars
            pygame.draw.circle(canvas, brush_color, (mouse_x, mouse_y), 5)

    if circle_mode and circle_start and pygame.mouse.get_pressed()[0]:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        circle_radius = int(((mouse_x - circle_start[0]) ** 2 + (mouse_y - circle_start[1]) ** 2) ** 0.5)
    
    for (pos, radius, color) in circles:
        pygame.draw.circle(screen, color, pos, radius, 2)

    if circle_mode and circle_start:
        pygame.draw.circle(screen, brush_color, circle_start, circle_radius, 2)

    pygame.draw.rect(screen, gray, (0, 0, width, 50))
    for button in buttons:
        button.draw(screen)

    pygame.display.flip()
