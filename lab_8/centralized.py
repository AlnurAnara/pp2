import pygame
import sys
from button import Button
from image import Pic

# Define colors
black = (0, 0, 0)
white = (255, 255, 255)
yellow = (255, 255, 0)
green = (0, 255, 0)
red = (255, 0, 0)

# Base Scene Class
class Scene:
    def handle_events(self, events):
        pass

    def update(self):
        pass

    def draw_image(self, screen):
        pass

# Game Scene Class
class GameScene(Scene):
    def __init__(self, scene_manager):
        self.scene_manager = scene_manager
        self.screen_width = 500
        self.screen_height = 500
        self.pic = Pic(self.scene_manager.screen)
        self.button = Button(x=self.screen_width // 2 - 75, y=20, width=150,  heigth=50, text='PAUSE')

        self.music_paused = True
        self.running = True
        self.visible = False
        self.start_ticks = pygame.time.get_ticks()

        pygame.mixer.music.load('Not_Like_Us_.Com_.mp3')
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                sys.exit()

            if self.button.is_clicked(event):
                if self.music_paused:
                    pygame.mixer.music.unpause()
                    self.button.text = 'PAUSE'
                else:
                    pygame.mixer.music.pause()
                    self.button.text = 'UNPAUSE'
                self.music_paused = not self.music_paused

            if event.type == pygame.KEYUP:
                print(f'Pressed the key: {pygame.key.name(event.key)}')
                if event.key == pygame.K_UP:
                    pygame.mixer.music.unpause()
                    self.button.text = 'PAUSE'
                if event.key == pygame.K_DOWN:
                    pygame.mixer.music.pause()
                    self.button.text = 'UNPAUSE'

            if event.type == pygame.MOUSEBUTTONDOWN:
                self.visible = True

    def update(self):
        if (pygame.time.get_ticks() - self.start_ticks) // 1000 >= 10:
            pygame.mixer.music.pause()
            self.button.text = 'UNPAUSE'
   

        self.pic.output()
        

    def draw_image(self, screen):
        screen.fill(white)
        font = pygame.font.Font(None, 36)
        elapsed_time = (pygame.time.get_ticks() - self.start_ticks) // 1000
        time_text = font.render(f"Time: {elapsed_time} sec", True, red)
        screen.blit(time_text, (10, 10))
        self.button.draw(screen)

        if self.visible:
            font = pygame.font.Font(None, 50)
            text_surface = font.render("Hello, Pygame!", True, (0, 0, 0))
            screen.blit(text_surface, (100, 100))

# Scene Manager Class
class SceneManager:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((500, 500))
        pygame.display.set_caption("Test Gaming")
        self.clock = pygame.time.Clock()
        self.scene = GameScene(self)

    def run(self):
        while True:
            events = pygame.event.get()
            self.scene.handle_events(events)
            self.scene.update()
            self.scene.draw_image(self.screen)
            pygame.display.flip()
            self.clock.tick(30)

# Main Execution
if __name__ == "__main__":
    manager = SceneManager()
    manager.run()
