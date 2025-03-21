import pygame

pygame.init()

# 设置屏幕大小
screen_width, screen_height = 400, 300
screen = pygame.display.set_mode((screen_width, screen_height))

# 变量初始化
done = False
x, y = 30, 30  # 球的初始位置
radius = 25  # 球的半径
move_step = 20  # 每次移动的步长

clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    # 获取键盘按键状态
    pressed = pygame.key.get_pressed()
    
    # 处理按键移动，同时确保球不会超出边界
    if pressed[pygame.K_UP] and y - move_step >= radius:
        y -= move_step
    if pressed[pygame.K_DOWN] and y + move_step <= screen_height - radius:
        y += move_step
    if pressed[pygame.K_LEFT] and x - move_step >= radius:
        x -= move_step
    if pressed[pygame.K_RIGHT] and x + move_step <= screen_width - radius:
        x += move_step

    # 清屏（白色背景）
    screen.fill((255, 255, 255))
    
    # 画红色的球
    pygame.draw.circle(screen, (255, 0, 0), (x, y), radius)

    # 刷新屏幕
    pygame.display.flip()
    clock.tick(60)
