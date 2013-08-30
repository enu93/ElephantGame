import pygame, sys
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((640, 350), 0, 32)
color = (255, 255, 0)
points = []

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == MOUSEBUTTONDOWN:
            points.append(event.pos)

    if len(points) > 1:
        pygame.draw.lines(screen, color, False, points, 5)



    pygame.display.update()
