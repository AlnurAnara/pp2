#Imports
import pygame, sys
from pygame.locals import *
import random, time

#Initialzing 
pygame.init()

#Setting up FPS 
FPS = 60
FramePerSec = pygame.time.Clock()

#Creating colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

#Other Variables for use in the program
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0

#Setting up Fonts
font = pygame.font.SysFont("Verdana", 60)#pygame.font.SysFont(font,size)(字体。大小)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)#create the graphics for the Font and the color

background = pygame.image.load("AnimatedStreet.png")

#Create a white screen 
DISPLAYSURF = pygame.display.set_mode((400,600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")


class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40,SCREEN_WIDTH-40), 0)
        '''Next it checks to see if the top of the Enemy has reached the end of the screen. 
        If True, it resets it back to the top of screen and at a random location on the X axis.
        '''

      def move(self):
        global SCORE
        self.rect.move_ip(0,SPEED)
        if (self.rect.bottom > 600):
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)


class Player(pygame.sprite.Sprite):#"pygame.sprite.Sprite" makes the Player Class it’s child class
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)#defines a starting position for
       
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        #if pressed_keys[K_UP]:
            #self.rect.move_ip(0, -5)   纵向移动
       #if pressed_keys[K_DOWN]:
            #self.rect.move_ip(0,5)
        '''
        Two of the if statements are commented out 
        because this is a side scroller game. 横向游戏
        We do not need up and down movement here
        '''
        
        if self.rect.left > 0:#ensure that the player isn’t able to move off screen.
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:       #defines a starting position for
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(5, 0)
                  

#Setting up Sprites        
P1 = Player()
E1 = Enemy()

#Creating Sprites Groups
enemies = pygame.sprite.Group()
enemies.add(E1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)

#Adding a new User event 
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

#Game Loop
while True:
      
    #Cycles through all events occuring  
    for event in pygame.event.get():
        if event.type == INC_SPEED:
              SPEED += 0.5     
              '''
              we insert an if statement to check for the INC_SPEED event occuring. 
              If it does, we increase the SPEED variable by 2. 
              This variable us used by the Enemy class to determine it is speed.
              '''

        if event.type == QUIT:
            pygame.quit()
            sys.exit()


    DISPLAYSURF.blit(background, (0,0))
    scores = font_small.render(str(SCORE), True, BLACK)
    DISPLAYSURF.blit(scores, (10,10))#create the font of scores

    #Moves and Re-draws all Sprites
    for entity in all_sprites:
        entity.move()
        DISPLAYSURF.blit(entity.image, entity.rect)
        

    #To be run if collision occurs between Player and Enemy
    if pygame.sprite.spritecollideany(P1, enemies):
          pygame.mixer.Sound('crash.wav').play()#to play a crash sound once collision has occurred.碰撞发生时播放碰撞声音
          time.sleep(1)
                   
          DISPLAYSURF.fill(RED)
          DISPLAYSURF.blit(game_over, (30,250))
          
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
        
    pygame.display.update()
    FramePerSec.tick(FPS)
