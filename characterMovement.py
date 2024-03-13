from pygame_functions import *

def drawPaddle(X, Y, width, height, color):
    global bgSurface
    color = parseColour(color)
    thisrect = pygame.Rect(X - width / 2, Y - height / 2, width, height)
    Paddle = pygame.draw.rect(screen, color, thisrect)
    if screenRefresh:
        pygame.display.update(thisrect)
    return Paddle

def movePaddleA():
    global PadA_y, PadA_speed
    
    PadA_y = PadA_y + PadA_speed
    

def moveBall(velx, vely):
    global ball_x, ball_y
    
    ball_x = ball_x + velx
    ball_y = ball_y + vely

def drawBall(X, Y, size, color, linewidth=0):
    global bgSurface
    color = parseColour(color)
    thisrect = pygame.Rect(X - size / 2, Y - size / 2, size, size)
    Circle = pygame.draw.ellipse(screen, color, thisrect, linewidth)
    if screenRefresh:
        pygame.display.update(thisrect)
    return Circle
    
screen =screenSize(800,800)
ball_x = 400
ball_y = 400
ball_size = 20
ball_color = 'white'
ball_lineWidth = 0
ball_speed = -2
PadA_x = 0
PadA_y = 300
PadA_width = 50
PadA_height = 200
PadA_color = "blue"
PadA_speed = 0

while True:
    if keyPressed("up"):
        PadA_speed = -4
    elif keyPressed("down"):
        PadA_speed = 4
    else:
        PadA_speed = 0
    
    clearShapes()
    movePaddleA()
    moveBall(ball_speed, ball_speed)
    Ball = drawBall(ball_x, ball_y, ball_size, ball_color)
    PadA = drawPaddle(PadA_x, PadA_y, PadA_width, PadA_height, PadA_color)
    if Ball.colliderect(PadA):
        print("collision")
        ball_speed = -ball_speed
    tick(40)
    