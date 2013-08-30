import pygame, sys
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((640, 350), 0, 32)

# polygon ponts
points = [(20, 120), (140, 140), (110,30)]
color = (255, 255, 0)

# circle points
position = (300, 176)
radius = (60)
color = (230, 170, 0)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    screen.lock()
    # draw rectangel with RGB color
    pygame.draw.rect(screen, (140, 240, 130), Rect((100, 100), (130, 170)))

    # draw polygon
    pygame.draw.polygon(screen, color, points)
    
    # draw circle
    pygame.draw.circle(screen, color, position, radius)

    screen.unlock()

    pygame.display.update()
