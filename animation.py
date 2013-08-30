bif = "bg.jpg"
mif = "ball.png"

import pygame, sys
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((640, 320), 0, 32)
background = pygame.image.load(bif).convert()
ball = pygame.image.load(mif).convert_alpha()

x = 0
clock = pygame.time.Clock()
speed = 250

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(background, (0, 0))
    screen.blit(ball, (x, 150))

    # setup spedd and time
    # calculate distance move(dm) = speed * time
    # add distance move with x co-orident
    # move x with given time 
    
    milli = clock.tick()
    seconds = milli/1000.
    dm = seconds * speed
    x += dm

    if x > 640:
        x = 0

    pygame.display.update()
