import pygame

pygame.init()

# Create screen
screen = pygame.display.set_mode((500, 300))

# Load font (None loads default system font)
font = pygame.font.Font(None, 36)

# Render text
text_surface = font.render("Hello, Pygame!", True, (255, 255, 255))

# Game loop
running = True
while running:
    screen.fill((0, 0, 0))
    screen.blit(text_surface, (100, 100))
    pygame.display.flip()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
