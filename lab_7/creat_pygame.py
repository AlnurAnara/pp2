import pygame
import sys

# Define colors
black = (0, 0, 0)
white = (255, 255, 255)
yellow = (255, 255, 51)
green = (0, 255, 0)
red = (255, 0, 0)

def run():
    pygame.init()
    screen_width = 500
    screen_height = 500

    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Test gaming")

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False  # Properly exit the loop instead of calling sys.exit()

        screen.fill(red)  # Fill the screen with green inside the loop
        pygame.display.flip()  # Corrected typo: flip()

    pygame.quit()  # Quit pygame properly

run()
