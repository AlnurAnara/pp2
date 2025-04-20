import pygame

pygame.init()


screen_width, screen_height = 400, 300
screen = pygame.display.set_mode((screen_width, screen_height))

black = (255,255,255)
rad = (255,0,0)

done = False
x, y = 30, 30  
radius = 25 
move_step = 20  

clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    
    pressed = pygame.key.get_pressed()
    
    
    if pressed[pygame.K_UP] and y - move_step >= radius:
        y -= move_step
    if pressed[pygame.K_DOWN] and y + move_step <= screen_height - radius:
        y += move_step
    if pressed[pygame.K_LEFT] and x - move_step >= radius:
        x -= move_step
    if pressed[pygame.K_RIGHT] and x + move_step <= screen_width - radius:
        x += move_step
   
    screen.fill((255, 255, 255))
    
    pygame.draw.circle(screen, (0, 255, 0), (x, y), radius)

    pygame.display.flip()
    clock.tick(60)
