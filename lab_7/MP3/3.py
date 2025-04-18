import pygame
import os
import re
import random
from image import Pic

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Pygame MP3 Player")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (30, 144, 255)


font = pygame.font.Font(None, 36)
small_font = pygame.font.Font(None, 28)

try:
    background = pygame.image.load("pinggu.jpg")
    background = pygame.transform.scale(background, (300, 300))  #
except:
    print("Could not load background image")
    background = None

music_folder = "C:\\Anara\\pp2\\lab_7\\MP3"  

songs = []
current_index = 0 
is_playing = False 

def playlist_init():
    for file in os.listdir(music_folder):
        file_name = os.fsdecode(file)
        ok = re.findall("mp3$", file_name)
        if ok:
            songs.append(os.path.join(music_folder, file_name))
    if not songs:
        print("Couldn't find songs maaan...")
        exit(1)

def play_song():
    global is_playing
    pygame.mixer.music.load(songs[current_index])
    pygame.mixer.music.play()
    is_playing = True

def next_song():
    global current_index
    current_index = (current_index + 1) % len(songs)  
    play_song()

def previous_song():
    global current_index
    current_index = (current_index - 1) % len(songs)  
    play_song()

def toggle_pause():
    global is_playing
    if is_playing:
        pygame.mixer.music.pause()
    else:
        pygame.mixer.music.unpause()
    is_playing = not is_playing

def stop_music():
    pygame.mixer.music.stop()

def draw_screen():
    if background:
        screen.blit(background, (0, 0))
    else:
        screen.fill(WHITE)


    text_surface = pygame.Surface((580, 380), pygame.SRCALPHA)
    text_surface.fill((255, 255, 255, 128)) 
    if songs:
        song_text = f"Now Playing: {os.path.basename(songs[current_index])}"
    else:
        song_text = "No MP3 files found"

    # Draw text on the transparent surface
    text_render = font.render(song_text, True, BLACK)
    text_surface.blit(text_render, (20, 20))

    instructions = [
        "Controls:",
        "SPACE - Play / Pause",
        "RIGHT ARROW - Next Song",
        "LEFT ARROW - Previous Song",
        "S - Stop",
        "ESC - Exit"
    ]

    y_offset = 60
    for line in instructions:
        text_render = small_font.render(line, True, BLUE)
        text_surface.blit(text_render, (20, y_offset))
        y_offset += 30


    screen.blit(text_surface, (10, 10))

    pygame.display.flip()

playlist_init()
play_song()

running = True
while running:
    draw_screen() 

    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False  

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE: 
                toggle_pause()
            elif event.key == pygame.K_RIGHT: 
                next_song()
            elif event.key == pygame.K_LEFT:  
                previous_song()
            elif event.key == pygame.K_s:  
                stop_music()

pygame.quit()