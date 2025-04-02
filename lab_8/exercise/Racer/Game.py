import pygame, sys
from pygame.locals import *
import random, time

pygame.init()
FPS = 60
FramePerSec = pygame.time.Clock()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)


SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0  # Enemy score
COINS_COLLECTED = 0  # Coin score

# Fonts 字体，for the ending of this game
font = pygame.font.SysFont("Verdana", 60)# Fonts 字体，for the ending of this game
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

background = pygame.image.load("AnimatedStreet.png")

DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")



class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)#This ensures that enemies spawn at random horizontal positions at the top of the game window
        

    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)# 0 means enemy means no horizontal movement.表示没有水平移动。
        if self.rect.bottom > SCREEN_HEIGHT:
            SCORE += 1
            # line 42-43 mean if the enemy goes down to the bottom of the canva,the score will be added into 1
            self.rect.top = 0 #Resets the enemy to the top of the screen.
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)#Gives the enemy a new random horizontal position at the top of the screen.



class Player(pygame.sprite.Sprite):#"pygame.sprite.Sprite" makes the Player Class it’s child class
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520) # set the initial position of the player
        self.speed_x = 0 #set the initial speed
    
    def move(self):
        self.rect.move_ip(self.speed_x, 0) # 0 means player do not have vertical movement
        if self.rect.left < 0:
            self.rect.left = 0 # avoid the player has moved past the right edge of the screen.
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH# avoid the player has moved past the left edge of the screen.


class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Coin.png")
        self.image = pygame.transform.scale(self.image, (30, 30)) # set the size of the coins
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

        '''
        This sets the initial position of the coin.
        The x-coordinate is randomly chosen between 40 and SCREEN_WIDTH - 40.
        '''


    def move(self):
        self.rect.move_ip(0, SPEED) # the coins do not have horizontal movement
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
            '''
            if loop : 这个方法使硬币持续向下移动。当它移出屏幕底部时，会将硬币重置到顶部的一个新的随机位置
            This method makes the coin move downward continuously. 
            When it goes off the bottom of the screen, it resets the coin to a new random position at the top, 
            creating an endless stream of coins for the player to collect.
            '''


P1 = Player()
E1 = Enemy()
C1 = Coin()


enemies = pygame.sprite.Group()
enemies.add(E1)
coins = pygame.sprite.Group()
coins.add(C1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1, E1, C1)

INC_SPEED = pygame.USEREVENT + 1 # increase the speed
pygame.time.set_timer(INC_SPEED, 1000)


while True:
    for event in pygame.event.get():
        if event.type == QUIT:  #If the user closes the game window, it quits pygame and exits the program.
            pygame.quit()
            sys.exit()
        if event.type == INC_SPEED:
            SPEED += 0.5

        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                P1.speed_x = -5
                #If the left arrow key is pressed, it sets the player's horizontal speed to -5 (moving left).
            if event.key == K_RIGHT:
                P1.speed_x = 5
                #If the right arrow key is pressed, it sets the player's horizontal speed to 5 (moving right)
        if event.type == KEYUP:
            if event.key in [K_LEFT, K_RIGHT]:
                P1.speed_x = 0

                '''
                If either the left or right arrow key is released, 
                it sets the player's horizontal speed to 0 (stopping horizontal movement
                '''

    
    DISPLAYSURF.blit(background, (0, 0))
    
    # Display Scores
    enemy_score = font_small.render(f"Score: {SCORE}", True, BLACK)
    coin_score = font_small.render(f"Coins: {COINS_COLLECTED}", True, BLACK)
    DISPLAYSURF.blit(enemy_score, (10, 10)) #set the score of enemy
    DISPLAYSURF.blit(coin_score, (300, 10)) #set the score of coins
    
 
    for entity in all_sprites:
        entity.move()
        DISPLAYSURF.blit(entity.image, entity.rect)
    
    # Collision Detection
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound('crash.wav').play()
        time.sleep(1)
        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over, (30, 250))
        pygame.display.update()
        for entity in all_sprites:
                entity.kill()
        time.sleep(2)
        pygame.quit()
        sys.exit()

        '''
        It checks if the player (P1) collides with any enemy sprite.
        If a collision occurs:
        It plays a crash sound.
        Pauses for 1 second.
        Fills the screen with red.
        Displays a "Game Over" message.
        Updates the display to show these changes.
        Removes all sprites from the game.
        Waits for 2 seconds.
        Quits Pygame and exits the program.
        '''
    
    if pygame.sprite.spritecollideany(P1, coins):
        COINS_COLLECTED += 1
        C1.rect.top = 0
        C1.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
    
    pygame.display.update() # refreshes the game window to show the latest frame.
    FramePerSec.tick(FPS)
