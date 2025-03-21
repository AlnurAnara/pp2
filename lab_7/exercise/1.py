import pygame
import sys
from image_button import Button  
from image import Pic  # Import the corrected Pic class

# Colors
red = (255, 0, 0)
white = (255, 255, 255)

def run():
    pygame.init()
    screen_width = 500
    screen_height = 500
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Test Gaming")

    # Load and play music
    pygame.mixer.music.load('Not_Like_Us_.Com_.mp3')  
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)  

    music_paused = False  
    running = True

    # Create button and picture object
    button = Button(x=screen_width // 2 - 75, y=20, width=150, height=50, text='PAUSE')
    pic = Pic(screen, 'pinggu.jpg', size=(200, 200), position=(150, 150))  # Load image

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
                print(f'Pressed the key: {pygame.key.name(event.key)}')
                if event.key == pygame.K_UP:
                    pygame.mixer.music.unpause()
                    button.text = 'PAUSE'
                if event.key == pygame.K_DOWN:
                    pygame.mixer.music.pause()
                    button.text = 'UNPAUSE'

        screen.fill(red)  # Set background color
        
        pic.output()  # Draw image
        button.draw(screen)  # Draw button
        pygame.draw.rect(screen, white, (50, 50, 50, 50))  # Draw extra rectangle

        pygame.display.flip()  # Update display

run()
