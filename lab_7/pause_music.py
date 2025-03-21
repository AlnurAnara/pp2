# creat colored terminal
import pygame
import sys

black=(0,0,0)
white=(255,255,255)
yellow=(255,255,51)
green=(0,255,0)
red=(255,0,0)

def run():
    pygame.init()
    screen_width = 500
    screen_height = 500

    screen=pygame.display.set_mode((screen_width,screen_height))
    pygame.display.set_caption("Test gaming")

    pygame.mixer.music.load('Not_Like_Us_.Com_.mp3')
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)


    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()


        screen.fill(red)
        pygame.mixer.music.unpause()  
        pygame.display.flip()

    pygame.quit() 
    
run()
