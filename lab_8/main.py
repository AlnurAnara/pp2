import pygame
import sys
from button import Button
from image import Pic

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

    pygame.mixer.music.load('Not_Like_Us_.Com_.mp3')
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)
    
    music_paused = True
    running = True
    button = Button(x = screen_width // 2 - 75, y = 20, width = 150, heigth = 50, text = 'PAUSE')
    pic = Pic(screen)

    clock = pygame.time.Clock()
    start_ticks = pygame.time.get_ticks()
    visiable = False
    
    while running:
        
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                sys.exit()
                
            if button.is_clicked(event):
                if music_paused:
                    pygame.mixer.music.unpause()
                    button.text = 'PAUSE'
                else:
                    pygame.mixer.music.pause()
                    button.text = 'UNPAUSE'
                music_paused = not music_paused
            
            if event.type == pygame.KEYUP:
                print(f'Pressed the keyword: {pygame.key.name(event.key)}')
                if event.key == pygame.K_UP:
                    pygame.mixer.music.unpause()
                    button.text = 'PAUSE'
                if event.key == pygame.K_DOWN:
                    pygame.mixer.music.pause()
                    button.text = 'UNPAUSE'
            if event.type == pygame.MOUSEBUTTONDOWN:
                visiable = True
            # clink the mouse,then the text will appear

        screen.fill(yellow)
        
       
        
        
        
        pic.output()
        button.draw(screen)
        elapsed_time = (pygame.time.get_ticks() - start_ticks) // 1000
        font = pygame.font.Font(None, 36)
        time_next = font.render(f"Time: {elapsed_time} sec", True, red)
        screen.blit(time_next, (10, 10))

        if visiable:
            font = pygame.font.Font(None,50)
            text_surface = font.render("Hello,Pygame!",True,(0,0,0))
            screen.blit(text_surface,(100,100))

        if elapsed_time >= 10:
            pygame.mixer.music.pause()
            button.text = "UNPAUSE"
            #after 10 sec it atumatically stop the time

        pygame.display.flip()

run()
                