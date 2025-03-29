import pygame, sys
from pygame.locals import *
import random, time

# Initialize pygame
pygame.init()

# FPS and Clock
FPS = 60
FramePerSec = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Screen Settings
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0  # Enemy score
COINS_COLLECTED = 0  # Coin score

# Fonts
font = pygame.font.SysFont("Verdana", 60)#pygame.font.SysFont(font,size)(字体。大小)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)#create the graphics for the Font and the color

# Load Background
background = pygame.image.load("AnimatedStreet.png")

# Setup Display
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")

# Enemy Class
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
        '''Next it checks to see if the top of the Enemy has reached the end of the screen. 
        If True, it resets it back to the top of screen and at a random location on the X axis.
        '''

    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)
        if self.rect.bottom > SCREEN_HEIGHT:
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

# Player Class
class Player(pygame.sprite.Sprite):#"pygame.sprite.Sprite" makes the Player Class it’s child class
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)#defines a starting position for
        self.speed_x = 0
    
    def move(self):
        self.rect.move_ip(self.speed_x, 0)
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH

# Coin Class
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Coin.png")
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
    
    def move(self):
        self.rect.move_ip(0, SPEED)
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

# Initialize Sprites
P1 = Player()
E1 = Enemy()
C1 = Coin()

# Sprite Groups
enemies = pygame.sprite.Group()
enemies.add(E1)
coins = pygame.sprite.Group()
coins.add(C1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1, E1, C1)

# User Event
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

# Game Loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == INC_SPEED:
            SPEED += 0.5

        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                P1.speed_x = -5
            if event.key == K_RIGHT:
                P1.speed_x = 5
        if event.type == KEYUP:
            if event.key in [K_LEFT, K_RIGHT]:
                P1.speed_x = 0
    
    # Draw Background
    DISPLAYSURF.blit(background, (0, 0))
    
    # Display Scores
    enemy_score = font_small.render(f"Score: {SCORE}", True, BLACK)
    coin_score = font_small.render(f"Coins: {COINS_COLLECTED}", True, BLACK)
    DISPLAYSURF.blit(enemy_score, (10, 10))#create the font of scores
    DISPLAYSURF.blit(coin_score, (300, 10))
    
    # Update Sprites
    for entity in all_sprites:
        entity.move()
        DISPLAYSURF.blit(entity.image, entity.rect)
    
    # Collision Detection
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound('crash.wav').play()#to play a crash sound once collision has occurred.碰撞发生时播放碰撞声音
        time.sleep(1)
        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over, (30, 250))
        pygame.display.update()
        for entity in all_sprites:
                entity.kill()
                '''
                code from 115-122 is used to check whether Player has collided with any of the sprites in the enemies group.
                Finally, the collision holds True, 
                we kill all the sprites using the kill() function, fill the screen with red, wait two seconds and close the entire program.
                '''
        time.sleep(2)
        pygame.quit()
        sys.exit()
    
    if pygame.sprite.spritecollideany(P1, coins):
        COINS_COLLECTED += 1
        C1.rect.top = 0
        C1.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
    
    pygame.display.update()
    FramePerSec.tick(FPS)
