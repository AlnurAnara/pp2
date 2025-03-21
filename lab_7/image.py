import pygame

class Pic():
    def __init__(self,screen):
        self.screen = screen
        self.image = pygame.image.load('pinggu.jpg') # professor said that use unique image that is created by myself
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.center = self.screen_rect.center
        '''
        the ways to chanbge the position of the image
        self.rect.bottom = self.screen_rect.bottom
        self.rect.top = self.screen_rect.top
        self.rect.right = self.screen_rect.right

        can change the position of the image


        '''

    def output(self):
        self.screen.blit(self.image,self.rect)
