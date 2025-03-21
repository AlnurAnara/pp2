import pygame
import sys
from button import Button  

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
    pygame.display.set_caption("Test Gaming")


    pygame.mixer.music.load('Not_Like_Us_.Com_.mp3')  
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)  

    music_paused = False  
    running = True

    button = Button(x=screen_width // 2 - 75, y=20, width=150, heigth=50, text='PAUSE')

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False 
                pygame.quit()
                sys.exit()

            if button.is_clicked(event):  
                if music_paused:
                    pygame.mixer.music.unpause()
                    button.text = 'PAUSE'
                else:
                    pygame.mixer.music.pause()
                    button.text = 'UNPAUSE'

                music_paused = not music_paused  

        screen.fill(red)
        button.draw(screen)
        pygame.display.flip()

run()
