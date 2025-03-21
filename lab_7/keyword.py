import pygame
import sys
from image_button import Button  
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
    pygame.display.set_caption("Test Gaming")


    pygame.mixer.music.load('Not_Like_Us_.Com_.mp3')  
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)  

    music_paused = False  
    running = True

    button = Button(x=screen_width // 2 - 75, y=20, width=150, heigth=50, text='PAUSE')
    pic = Pic(screen)

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

            if event.type == pygame.KEYUP:
                print(f'Pressed the keyword: {pygame.key.name(event.key)}') # print the keyword u tapped 
                if event.key == pygame.K_UP:
                    pygame.mixer.music.unpause()
                    button.text = 'PAUSE'
                if event.key == pygame.K_DOWN:
                    pygame.mixer.music.pause()
                    button.text = 'UNPAUSE'


        screen.fill(red)
        
        pic.output()
        button.draw(screen) #draws must after the output,otherwise the button will be covered by the image
        pygame.display.flip()

run()
'''
List of Common event.key Values
pygame.K_UP # Up arrow key
pygame.K_DOWN # Down arrow key
pygame.K_LEFT # Left arrow key
pygame.K_RIGHT # Right arrow key
…
pygame.K_a # 'A' key
pygame.K_b # 'B' key
pygame.K_c # 'C' key
...
pygame.K_0 # '0' key
pygame.K_1 # '1' key
pygame.K_2 # '2' key
...
pygame.K_RETURN # Enter key
pygame.K_ESCAPE # Escape key
pygame.K_BACKSPACE # Backspace key
pygame.K_TAB # Tab key
pygame.K_SPACE # Spacebar
pygame.K_DELETE # Delete key
pygame.K_HOME # Home key
pygame.K_END # End key
pygame.K_PAGEUP # Page Up key
pygame.K_PAGEDOWN # Page Down key
pygame.K_INSERT # Insert key


'''