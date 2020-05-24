#! python3
# basics.py - understanding the basics of pygame
import pygame, sys
from pygame.locals import *

pygame.init()
display_surf = pygame.display.set_mode((500, 500), 0, 32)
pygame.display.set_caption('Animation')

#display_surf.fill(aqua)
fps = 30
fps_clock = pygame.time.Clock()

white = (255, 255, 255)
cat_img = pygame.image.load('cat_image.jpeg')
cat_x = 10
cat_y = 10
direction = 'right'

while True:
    display_surf.fill(white)
    if direction == 'right':
        cat_x += 5
        if cat_x == 280:
            direction = 'up'
    elif direction == 'up':
        cat_y += 5
        if cat_y == 220:
            direction = 'left'
    elif direction == 'left':
        cat_x -= 5
        if cat_x == 10:
            direction = 'down'
    elif direction == 'down':
        cat_y -= 5
        if cat_y == 10:
            direction == 'right'
    display_surf.blit(cat_img, (cat_x, cat_y))


    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()