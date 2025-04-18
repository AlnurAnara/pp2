import pygame
import sys
import math

pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Simple Paint')

white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
gray = (200, 200, 200)

canvas = pygame.Surface((width, height))
canvas.fill(white)

class Button:
    def __init__(self, x, y, width, height, text, color, action):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.action = action

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)#the size of the screen
        font = pygame.font.Font(None, 30)
        text_surface = font.render(self.text, True, white)
        screen.blit(text_surface, (self.rect.x + 10, self.rect.y + 5))

    def check_action(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos):
            self.action()

drawing = False
circle_mode = False
rect_mode = False
eraser_mode = False
square_mode = False
right_triangle_mode = False
equilateral_triangle_mode = False
rhombus_mode = False

brush_color = black

circle_start = None
circle_radius = 0
rect_start = None
rects = []
circles = []
squares = []
right_triangles = []
equilateral_triangles = []
rhombuses = []

def set_black():
    global brush_color, eraser_mode
    brush_color = black
    eraser_mode = False

def set_green():
    global brush_color, eraser_mode
    brush_color = green
    eraser_mode = False

def set_red():
    global brush_color, eraser_mode
    brush_color = red
    eraser_mode = False

def set_blue():
    global brush_color, eraser_mode
    brush_color = blue
    eraser_mode = False

def clear_screen():
    global circles, rects, squares, right_triangles, equilateral_triangles, rhombuses
    canvas.fill(white)
    circles = []
    rects = []
    squares = []
    right_triangles = []
    equilateral_triangles = []
    rhombuses = []
    pygame.display.flip()

def exit_app():
    pygame.quit()
    sys.exit()

def toggle_circle_mode():
    global circle_mode, rect_mode, eraser_mode, square_mode, right_triangle_mode, equilateral_triangle_mode, rhombus_mode
    circle_mode = True
    rect_mode = False
    eraser_mode = False
    square_mode = False
    right_triangle_mode = False
    equilateral_triangle_mode = False
    rhombus_mode = False

def toggle_rect_mode():
    global rect_mode, circle_mode, eraser_mode, square_mode, right_triangle_mode, equilateral_triangle_mode, rhombus_mode
    rect_mode = True
    circle_mode = False
    eraser_mode = False
    square_mode = False
    right_triangle_mode = False
    equilateral_triangle_mode = False
    rhombus_mode = False

def toggle_eraser_mode():
    global eraser_mode, circle_mode, rect_mode, brush_color, square_mode, right_triangle_mode, equilateral_triangle_mode, rhombus_mode
    eraser_mode = not eraser_mode
    circle_mode = False
    rect_mode = False
    square_mode = False
    right_triangle_mode = False
    equilateral_triangle_mode = False
    rhombus_mode = False
    if eraser_mode:
        brush_color = white
    else:
        brush_color = black

def toggle_square_mode():
    global square_mode, circle_mode, rect_mode, eraser_mode, right_triangle_mode, equilateral_triangle_mode, rhombus_mode
    square_mode = True
    circle_mode = False
    rect_mode = False
    eraser_mode = False
    right_triangle_mode = False
    equilateral_triangle_mode = False
    rhombus_mode = False

def toggle_right_triangle_mode():
    global right_triangle_mode, square_mode, circle_mode, rect_mode, eraser_mode, equilateral_triangle_mode, rhombus_mode
    right_triangle_mode = True
    square_mode = False
    circle_mode = False
    rect_mode = False
    eraser_mode = False
    equilateral_triangle_mode = False
    rhombus_mode = False

def toggle_equilateral_triangle_mode():
    global equilateral_triangle_mode, right_triangle_mode, square_mode, circle_mode, rect_mode, eraser_mode, rhombus_mode
    equilateral_triangle_mode = True
    right_triangle_mode = False
    square_mode = False
    circle_mode = False
    rect_mode = False
    eraser_mode = False
    rhombus_mode = False

def toggle_rhombus_mode():
    global rhombus_mode, equilateral_triangle_mode, right_triangle_mode, square_mode, circle_mode, rect_mode, eraser_mode
    rhombus_mode = True
    equilateral_triangle_mode = False
    right_triangle_mode = False
    square_mode = False
    circle_mode = False
    rect_mode = False
    eraser_mode = False

def point_in_circle(point, circle_center, radius):
    return (point[0] - circle_center[0])**2 + (point[1] - circle_center[1])**2 <= radius**2
#Calculates the squared difference in x-coordinates.and Calculates the squared difference in y-coordinates.

def point_in_rect(point, rect_pos, width, height):
    return (rect_pos[0] <= point[0] <= rect_pos[0] + width and
            rect_pos[1] <= point[1] <= rect_pos[1] + height)

def point_in_polygon(point, polygon):
    x, y = point
    n = len(polygon)
    inside = False
    p1x, p1y = polygon[0]
    for i in range(n + 1):
        p2x, p2y = polygon[i % n]
        if y > min(p1y, p2y):
            if y <= max(p1y, p2y):
                if x <= max(p1x, p2x):
                    if p1y != p2y:
                        xinters = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                    if p1x == p2x or x <= xinters:
                        inside = not inside
        p1x, p1y = p2x, p2y
    return inside

buttons = [
    Button(10, 10, 60, 30, 'Black', black, set_black),
    Button(80, 10, 60, 30, 'Green', green, set_green),
    Button(150, 10, 60, 30, 'Red', red, set_red),
    Button(220, 10, 60, 30, 'Blue', blue, set_blue),
    Button(290, 10, 60, 30, 'Clear', gray, clear_screen),
    Button(380, 10, 60, 30, 'Exit', gray, exit_app),
    Button(470, 10, 80, 30, "Circle", gray, toggle_circle_mode),
    Button(570, 10, 80, 30, "Rectangle", gray, toggle_rect_mode),
    Button(670, 10, 80, 30, "Eraser", gray, toggle_eraser_mode),
    Button(10, 50, 80, 30, "Square", gray, toggle_square_mode),
    Button(100, 50, 120, 30, "Right Triangle", gray, toggle_right_triangle_mode),
    Button(230, 50, 140, 30, "Equilateral Triangle", gray, toggle_equilateral_triangle_mode),
    Button(380, 50, 80, 30, "Rhombus", gray, toggle_rhombus_mode)
]

while True:
    screen.fill(white)
    screen.blit(canvas, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_app()

        for button in buttons:
            button.check_action(event)

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if circle_mode:
                    circle_start = pygame.mouse.get_pos()
                    circle_radius = 0
                elif rect_mode or square_mode or right_triangle_mode or equilateral_triangle_mode or rhombus_mode:
                    rect_start = pygame.mouse.get_pos()
                elif eraser_mode:

                    # First check if we clicked on any shape to erase it!!!!!!!!!!
                    pos = pygame.mouse.get_pos()
                    shape_erased = False
                    
                    # Check circles
                    for i in range(len(circles)-1, -1, -1):
                        center, radius, _ = circles[i]
                        if point_in_circle(pos, center, radius):
                            del circles[i]
                            shape_erased = True
                            break
                    
                    # Check rectangles
                    if not shape_erased:
                        for i in range(len(rects)-1, -1, -1):
                            rect_pos, w, h, _ = rects[i]
                            if point_in_rect(pos, rect_pos, w, h):
                                del rects[i]
                                shape_erased = True
                                break
                    
                    # Check squares
                    if not shape_erased:
                        for i in range(len(squares)-1, -1, -1):
                            square_pos, side, _ = squares[i]
                            if point_in_rect(pos, square_pos, side, side):
                                del squares[i]
                                shape_erased = True
                                break
                    
                    # Check right triangles
                    if not shape_erased:
                        for i in range(len(right_triangles)-1, -1, -1):
                            points, _ = right_triangles[i]
                            if point_in_polygon(pos, points):
                                del right_triangles[i]
                                shape_erased = True
                                break
                    
                    # Check equilateral triangles
                    if not shape_erased:
                        for i in range(len(equilateral_triangles)-1, -1, -1):
                            points, _ = equilateral_triangles[i]
                            if point_in_polygon(pos, points):
                                del equilateral_triangles[i]
                                shape_erased = True
                                break
                    
                    # Check rhombuses
                    if not shape_erased:
                        for i in range(len(rhombuses)-1, -1, -1):
                            points, _ = rhombuses[i]
                            if point_in_polygon(pos, points):
                                del rhombuses[i]
                                shape_erased = True
                                break
                    
                    if shape_erased:
                        # Redraw canvas if a shape was erased
                        canvas.fill(white) 
                        #redraw the cnavan
                        for (pos, w, h, color) in rects:
                            pygame.draw.rect(canvas, color, (*pos, w, h), 2)
                        for (pos, radius, color) in circles:
                            pygame.draw.circle(canvas, color, pos, radius, 2)
                        for (pos, side, color) in squares:
                            pygame.draw.rect(canvas, color, (*pos, side, side), 2)
                        for (points, color) in right_triangles:
                            pygame.draw.polygon(canvas, color, points, 2)
                        for (points, color) in equilateral_triangles:
                            pygame.draw.polygon(canvas, color, points, 2)
                        for (points, color) in rhombuses:
                            pygame.draw.polygon(canvas, color, points, 2)
                    else:
                        # If no shape was clicked, start erasing with mouse movement
                        drawing = True
                else:
                    drawing = True # free earser 

                    ''''
                   When the left button is pressed: 当左键按下时

                    If it is a circle mode: record the center position  如果是圆形模式：记录圆心位置

                    If it is another shape mode: record the starting point 如果是其他形状模式：记录起始点

                    Otherwise: enter free drawing mode  否则：进入自由绘制模式
                    
                    '''

        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                drawing = False # When the left mouse button (button 1) is released, drawing is set to False, indicating the end of drawing.
                #当左鼠标按钮（按钮1）释放时，将drawing设置为False，表示停止绘制

                if circle_mode and circle_start:
                    circles.append((circle_start, circle_radius, brush_color))
                    pygame.draw.circle(canvas, brush_color, circle_start, circle_radius, 2)

                if rect_mode and rect_start:
                    rect_end = pygame.mouse.get_pos()
                    x1, y1 = rect_start
                    x2, y2 = rect_end
                    width = abs(x2 - x1)
                    height = abs(y2 - y1)
                    rect_top_left = (min(x1, x2), min(y1, y2))
                    rects.append((rect_top_left, width, height, brush_color))
                    pygame.draw.rect(canvas, brush_color, (*rect_top_left, width, height), 2)
                    rect_start = None

                if square_mode and rect_start:
                    end_pos = pygame.mouse.get_pos()
                    side = min(abs(end_pos[0] - rect_start[0]), abs(end_pos[1] - rect_start[1]))
                    top_left = (min(rect_start[0], end_pos[0]), min(rect_start[1], end_pos[1]))
                    squares.append((top_left, side, brush_color))
                    pygame.draw.rect(canvas, brush_color, (*top_left, side, side), 2)
                    rect_start = None

                if right_triangle_mode and rect_start:
                    end_pos = pygame.mouse.get_pos()
                    points = [rect_start, (end_pos[0], rect_start[1]), end_pos]
                    right_triangles.append((points, brush_color))
                    pygame.draw.polygon(canvas, brush_color, points, 2)
                    rect_start = None

                if equilateral_triangle_mode and rect_start:
                    end_pos = pygame.mouse.get_pos()
                    base = abs(end_pos[0] - rect_start[0])
                    height = int((math.sqrt(3) / 2) * base)
                    top_point = (rect_start[0] + (end_pos[0] - rect_start[0]) // 2, min(rect_start[1], end_pos[1]) - height)
                    points = [rect_start, end_pos, top_point]
                    equilateral_triangles.append((points, brush_color))
                    pygame.draw.polygon(canvas, brush_color, points, 2)
                    rect_start = None

                if rhombus_mode and rect_start:
                    end_pos = pygame.mouse.get_pos()
                    width = abs(end_pos[0] - rect_start[0])
                    height = abs(end_pos[1] - rect_start[1])
                    points = [(rect_start[0] + width // 2, rect_start[1]), (end_pos[0], rect_start[1] + height // 2), (rect_start[0] + width // 2, end_pos[1]), (rect_start[0], rect_start[1] + height // 2)]
                    rhombuses.append((points, brush_color))
                    pygame.draw.polygon(canvas, brush_color, points, 2)
                    rect_start = None

        if event.type == pygame.MOUSEMOTION:
            if drawing and eraser_mode and pygame.mouse.get_pressed()[0]:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if mouse_y > 90:
                    pygame.draw.circle(canvas, white, (mouse_x, mouse_y), 10)
                '''
the eraser draws a white circle at the mouse position with a radius of 10 pixels to over with the background color.
                    '''
            elif drawing and not eraser_mode and pygame.mouse.get_pressed()[0]:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if mouse_y > 90:
                    pygame.draw.circle(canvas, brush_color, (mouse_x, mouse_y), 5)

    # save all
    for (pos, w, h, color) in rects:
        pygame.draw.rect(screen, color, (*pos, w, h), 2)

    for (pos, radius, color) in circles:
        pygame.draw.circle(screen, color, pos, radius, 2)

    for (pos, side, color) in squares:
        pygame.draw.rect(screen, color, (*pos, side, side), 2)

    for (points, color) in right_triangles:
        pygame.draw.polygon(screen, color, points, 2)

    for (points, color) in equilateral_triangles:
        pygame.draw.polygon(screen, color, points, 2)

    for (points, color) in rhombuses:
        pygame.draw.polygon(screen, color, points, 2)

    # 实时预览当前正在绘制的形状
    if circle_mode and circle_start and pygame.mouse.get_pressed()[0]:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        circle_radius = int(((mouse_x - circle_start[0]) ** 2 + (mouse_y - circle_start[1]) ** 2) ** 0.5)
        pygame.draw.circle(screen, brush_color, circle_start, circle_radius, 2)
        #Calculates the radius of the circle using the distance formula between two points.


    if rect_mode and rect_start and pygame.mouse.get_pressed()[0]: # show the drawing path of these geomateric features
        mouse_x, mouse_y = pygame.mouse.get_pos()
        x1, y1 = rect_start
        width = abs(mouse_x - x1)
        height = abs(mouse_y - y1)
        rect_top_left = (min(x1, mouse_x), min(y1, mouse_y))
        pygame.draw.rect(screen, brush_color, (*rect_top_left, width, height), 2)

    if square_mode and rect_start and pygame.mouse.get_pressed()[0]:
        end_pos = pygame.mouse.get_pos()
        side = min(abs(end_pos[0] - rect_start[0]), abs(end_pos[1] - rect_start[1]))
        top_left = (min(rect_start[0], end_pos[0]), min(rect_start[1], end_pos[1]))
        pygame.draw.rect(screen, brush_color, (*top_left, side, side), 2)

    if right_triangle_mode and rect_start and pygame.mouse.get_pressed()[0]:
        end_pos = pygame.mouse.get_pos()
        points = [rect_start, (end_pos[0], rect_start[1]), end_pos]
        pygame.draw.polygon(screen, brush_color, points, 2)

    if equilateral_triangle_mode and rect_start and pygame.mouse.get_pressed()[0]:
        end_pos = pygame.mouse.get_pos()
        base = abs(end_pos[0] - rect_start[0])
        height = int((math.sqrt(3) / 2) * base)
        top_point = (rect_start[0] + (end_pos[0] - rect_start[0]) // 2, min(rect_start[1], end_pos[1]) - height)
        points = [rect_start, end_pos, top_point]
        pygame.draw.polygon(screen, brush_color, points, 2)

    if rhombus_mode and rect_start and pygame.mouse.get_pressed()[0]:
        end_pos = pygame.mouse.get_pos()
        width = abs(end_pos[0] - rect_start[0])
        height = abs(end_pos[1] - rect_start[1])
        points = [(rect_start[0] + width // 2, rect_start[1]), (end_pos[0], rect_start[1] + height // 2), (rect_start[0] + width // 2, end_pos[1]), (rect_start[0], rect_start[1] + height // 2)]
        pygame.draw.polygon(screen, brush_color, points, 2)

    pygame.draw.rect(screen, gray, (0, 0, width, 90))
    for button in buttons:
        button.draw(screen)

    pygame.display.flip()