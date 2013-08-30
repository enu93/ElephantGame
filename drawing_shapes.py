import pygame, sys
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((640, 350), 0, 32)
color = (255, 255, 0)

# polygon ponts
points = [(20, 120), (140, 140), (10,30)]

# circle points
position = (300, 176)
radius = (60)

# ellipse points
rectangle = (140, 180, 50, 190)

# draw line
pos1 = (20, 20)
pos2 = (150, 134)

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

    # draw ellipse
    pygame.draw.ellipse(screen, color, rectangle)

    # draw line
    pygame.draw.line(screen, color, pos1, pos2, 10)
    
    screen.unlock()

    pygame.display.update()
