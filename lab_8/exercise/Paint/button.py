import pygame

black = (0, 0, 0)
white = (255, 255, 255)
yellow = (255, 255, 51)
green = (0, 255, 0)
red = (255, 0, 0)
sky_blue = (51, 255, 255)
dark_green = (0, 102, 0)

canvas = pygame.Surface((white))
canvas.fill(white)

class Button():

    def __init__(self, x, y, width, heigth, text,color,action):
        self.rect = pygame.Rect(x, y, width, heigth)
        self.text = text
        self.color = color
        self.action = action

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        font = pygame.font.Font(None,30)
        text_surface = font.render(self.text, True, white)
        screen.blit(text_surface, (self.rect.x + 10, self.rect.y + 5))

    def check_click(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN :
            if self.rect.collidepoint(event.pos):
                self.action()

#Drawing variables
drawing  =  False
brush_color = black
circle_mode = False
circle_start = None
circle_radius = 0

def set_color_black():
    global brush_color
    brush_color = black

def set_color_red():
    global brush_color
        