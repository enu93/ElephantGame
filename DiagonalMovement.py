bif = "bg.jpg"
mif = "ball.png"

import pygame, sys
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((640, 350), 0, 32)
background = pygame.image.load(bif).convert()
ball = pygame.image.load(mif).convert()

# initiazes the object
x = 0
y = 0
clock = pygame.time.Clock()
speedx = 150
speedy = 170

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        screen.blit(background, (0, 0))
        screen.blit(ball, (x, y))

        # count the time
        milli = clock.tick()
        seconds = milli/1000.

        # find distance move(dm)
        dmx = seconds * speedx
        dmy = seconds * speedy

        # calulate value of x and y
        x += dmx
        y += dmy

        if x > 640:
            x = 0

        if y > 350:
            y = 0



    pygame.display.update()
