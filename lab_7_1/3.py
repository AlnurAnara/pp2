import pygame
pygame.init()
# Constants
WIDTH, HEIGHT = 500, 500
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
# Create screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
# Player settings
player = pygame.Rect(200, 200, 50, 50)
speed = 5

running = True
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.x -= speed
    if keys[pygame.K_RIGHT]:
        player.x += speed
    if keys[pygame.K_UP]:
        player.y -= speed
    if keys[pygame.K_DOWN]:
        player.y += speed

    pygame.draw.rect(screen, BLUE, player)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()