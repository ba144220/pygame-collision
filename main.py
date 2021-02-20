import pygame, math
from vector_operations import *

pygame.init()

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE = (0,0,200)
GREEN = (0,200,0)
RED = (200,0,0)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

# block
block_center = (300,300)
block_width = 100
block_color = BLUE

def display_block():
    rect = pygame.Rect(0,0,1,1)
    rect.width = block_width
    rect.height = block_width
    rect.center = block_center
    pygame.draw.rect(screen, block_color, rect)

# ball
ball_center = (40.0,200.0)
ball_radius = 20
ball_color = GREEN
ball_v = (6.0,3.0)

def update_ball():
    global ball_center
    (x0,y0) = ball_center
    x = x0 + ball_v[0]
    y = y0 + ball_v[1]
    ball_center = (x,y)

def display_ball():
    bc = (round(ball_center[0]), round(ball_center[1]))
    pygame.draw.circle(screen, ball_color, bc, ball_radius)

def sides_collision():
    global ball_center
    global block_center
    global ball_radius
    global block_width
    global ball_v

    ball_x, ball_y = ball_center
    block_x, block_y = block_center
    ball_r = ball_radius
    block_hw = block_width * 0.5

    x0 = block_x - block_hw
    x1 = block_x + block_hw
    y0 = block_y - block_hw
    y1 = block_y + block_hw

    if ball_y >= y0 and ball_y <= y1:
        if ball_x>=(x0-ball_r) and ball_x <= x0:
            print('left')
            if ball_v[0] >= 0:
                ball_v = reflect(ball_v, (-1,0))
        elif ball_x>=x1 and ball_x <=x1+ball_r:
            print('right')
            if ball_v[0] <= 0:
                ball_v = reflect(ball_v, (1,0))
    elif ball_x >= x0 and ball_x <= x1:
        if ball_y>=y0-ball_r and ball_y <=y0:
            print('top')
            if ball_v[1] >= 0:
                ball_v = reflect(ball_v, (0,-1))
        elif ball_y >= y1 and ball_y <= y1+ball_r:
            print('bottom')
            if ball_v[1] <= 0:
                ball_v = reflect(ball_v, (0,1))
    
    if ball_x <= ball_r:
        print('wall left')
        
        if ball_v[0] <= 0:
            ball_v = reflect(ball_v, (-1,0))
        
    elif ball_x >= SCREEN_WIDTH - ball_r :
        print('wall right')
        
        if ball_v[0] >= 0:
            ball_v = reflect(ball_v, ( 1,0))
        
    elif ball_y <= ball_r :
        print('wall top')

        if ball_v[1] <= 0:
            ball_v = reflect(ball_v, (0,-1))

    elif ball_y >= SCREEN_HEIGHT - ball_r :
        print('wall bottom')

        if ball_v[1] >= 0:
            ball_v = reflect(ball_v, (0,1))

def edges_collision():
    global ball_center
    global block_center
    global ball_radius
    global block_width
    global ball_v

    ball_x, ball_y = ball_center
    block_x, block_y = block_center
    ball_r = ball_radius
    block_hw = block_width * 0.5
    
    edge_top_left = (block_x - block_hw, block_y - block_hw)
    edge_top_right = (block_x + block_hw, block_y - block_hw)
    edge_bottom_left = (block_x - block_hw, block_y + block_hw)
    edge_bottom_right = (block_x + block_hw, block_y + block_hw)

    if distance(edge_bottom_left, ball_center) <= ball_r:
        print('bottom left')
        ball_v = reflect(ball_v, (-1,1))
    elif distance(edge_bottom_right, ball_center) <= ball_r:
        print('bottom right')
        ball_v = reflect(ball_v, (1,1))
    elif distance(edge_top_left, ball_center) <= ball_r:
        print('top left')
        ball_v = reflect(ball_v, (-1,-1))
    elif distance(edge_top_right, ball_center) <= ball_r:
        print('top right')
        ball_v = reflect(ball_v, (1,-1))

while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    screen.fill(BLACK)
    display_block()
    update_ball()
    sides_collision()
    edges_collision()
    display_ball()
    pygame.display.update()
    print(clock.get_fps())
