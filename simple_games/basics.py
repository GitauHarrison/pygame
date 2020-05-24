#! python3
# basics.py - understanding the basics of pygame
import pygame, sys
from pygame.locals import *
from time import sleep

pygame.init()
display_surf = pygame.display.set_mode((500, 500), 0, 32)
pygame.display.set_caption('Animation')

white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 255)

fontObj = pygame.font.Font('freesansbold.ttf', 32)
textSurfaceObj = fontObj.render('Hello World', True, green, blue)
textRectObj = textSurfaceObj.get_rect()
textRectObj.center = (200, 150)

soundObj = pygame.mixer.Sound('church_bells.wav')
soundObj.play()
sleep(2)
soundObj.stop()

pygame.mixer.music.load('Stranger_In_the_Way.wav')
pygame.mixer.music.play(-1, 0.0)
sleep(4)
pygame.mixer.music.stop()

while True:
    display_surf.fill(white)
    display_surf.blit(textSurfaceObj, textRectObj)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()