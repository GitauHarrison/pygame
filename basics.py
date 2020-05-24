#! python3
# basics.py - understanding the basics of pygame
import pygame, sys
from pygame.locals import *

pygame.init()
display_surf = pygame.display.set_mode((500, 500), 0, 32)
pygame.display.set_caption('Basics')

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
aqua = (0, 255, 255)

display_surf.fill(aqua)
clock = pygame.time.Clock()

pygame.draw.polygon(display_surf, green,  ((146, 0), (291, 106), (236, 277), (56, 277), (0, 106)))
pygame.draw.line(display_surf, blue, (60,60), (120, 60), 4)
pygame.draw.line(display_surf, blue, (120, 60), (60, 120))
pygame.draw.line(display_surf, blue, (60, 120), (120, 120), 4)
pygame.draw.circle(display_surf, blue, (300, 50), 20, 0)
pygame.draw.ellipse(display_surf, red, (300, 250, 40, 80), 1)
pygame.draw.rect(display_surf, red, (200, 150, 100, 50))

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()