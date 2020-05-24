#! python3
# basics.py - understanding the basics of pygame
import pygame, sys
from pygame.locals import *

pygame.init()
DISPLAY_SURF = pygame.display.set_mode((500, 500))
pygame.display.set_caption('Basics')

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    DISPLAY_SURF.fill((0, 255, 255))
    pygame.display.update()