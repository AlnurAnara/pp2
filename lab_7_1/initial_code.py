'''
import pygame

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Window")

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        screen.fill((0, 0, 0)) # Clear screen with black color
        pygame.display.flip() # Update the display

pygame.quit()
'''



import pygame

pygame.init()
width ,height = 800,600

screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Pygame")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        screen.fill((0,255,0))
        pygame.display.flip()

pygame.quit()