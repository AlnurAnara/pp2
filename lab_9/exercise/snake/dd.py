import pygame
import sys
import random


pygame.init()
width, height = 500, 500
cell_size = 10  # Snake size

black = (0, 0, 0)
red = (255, 0, 0)
white = (255, 255, 255)

snake_img = pygame.image.load('snake.png')
snake_img = pygame.transform.scale(snake_img, (cell_size, cell_size))

# Initialize screen
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake Game with Levels')

snake_pos = [100, 100]
snake_body = [[100, 100], [90, 100], [80, 100]]
direction = 'RIGHT'
change_to = direction

# Snake's initial info
speed = 10
score = 0
level = 1

clock = pygame.time.Clock()  # set the speed
running = True

# Food Generation Weights and Probabilities
food_weights = [1, 2, 3]
food_probabilities = [0.7, 0.9, 0.5]

foods = []

def generate_food():
    weight = random.choices(food_weights, food_probabilities)[0]
    new_food = {
        'pos': [
            random.randrange(0, width // cell_size) * cell_size,
            random.randrange(0, height // cell_size) * cell_size,
        ],
        'weight': weight,
        'disappear_time': pygame.time.get_ticks(), 
    }
    while new_food['pos'] in snake_body or any( 
        new_food['pos'] == food['pos'] for food in foods      # Avoid food appears on the snake's body
    ): 
        new_food['pos'] = [
            random.randrange(0, width // cell_size) * cell_size,
            random.randrange(0, height // cell_size) * cell_size,     #if is coinside with the body regenerated
        ]
    return new_food

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            # the usfulness of and direction != is to avoid the snake moving like train (can move with both head and tile)
            if event.key == pygame.K_UP and direction != 'DOWN':
                change_to = 'UP'
            elif event.key == pygame.K_DOWN and direction != 'UP':
                change_to = 'DOWN'
            elif event.key == pygame.K_RIGHT and direction != 'LEFT':
                change_to = 'RIGHT'
            elif event.key == pygame.K_LEFT and direction != 'RIGHT':
                change_to = 'LEFT'
        direction = change_to  # Update direction

    if direction == 'UP': 
        snake_pos[1] -= cell_size    #Decrease the y-coordinate by cell_size
    elif direction == 'DOWN':
        snake_pos[1] += cell_size
    elif direction == 'LEFT':
        snake_pos[0] -= cell_size
    elif direction == 'RIGHT':
        snake_pos[0] += cell_size

   # Check for collision with walls
    if snake_pos[0] < 0 or snake_pos[0] >= width or snake_pos[1] < 0 or snake_pos[1] >= height:
        running = False  # End game if hitting the wall

    # Update the length of the body
    snake_body.insert(0, list(snake_pos))

    # Check if snake eats food
    for food in foods[:]:
        if snake_pos == food['pos']:
            score += food['weight'] # add scores based on the weigth
            foods.remove(food)
            foods.append(generate_food()) #add a new food 
            break
    else:
        snake_body.pop()

    # Level up every 2 points
    if score % 2 == 0 and score != 0 and (score // 2) + 1 > level:
        level += 1
        speed += 2  # Increase speed when leveling up

    # Check for self-collision
    if snake_pos in snake_body[1:]:
        running = False  # End game if colliding with itself

    screen.fill(black)
    for block in snake_body:
        screen.blit(snake_img, (block[0], block[1]))

    # Food Disappearance and Drawing
    current_time = pygame.time.get_ticks()
    foods[:] = [
        food
        for food in foods
        if current_time - food['disappear_time'] <= 7000 # 7000 ms  = 7 seconds 
    ]  
    for food in foods:
        pygame.draw.rect(
            screen, red, pygame.Rect(food['pos'][0], food['pos'][1], cell_size, cell_size)
        )
    if len(foods) < 1:
        foods.append(generate_food())

    # set the font and size of the score and level
    font = pygame.font.SysFont('Arial', 20)
    score_text = font.render(f'Score: {score}  Level: {level}', True, white)
    screen.blit(score_text, [10, 10])

    pygame.display.flip()
    clock.tick(speed)

pygame.quit()
sys.exit()