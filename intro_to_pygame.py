# !python3
#intro_to_pygame.py - shows how to use the pygame package for the very first time

# TODO 1: Import pygame
import pygame

# TODO 2: Initialize pygame
pygame.init()

# TODO 3: Instantiate the game display
display_width = 500
display_height = 500
game_display = pygame.display.set_mode((display_width, display_height))

# TODO 5: Update the game window caption
pygame.display.set_caption('Intro to Pygame')

# TODO 4: Learn how to close the game display using the keyboard
def event_handler():
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (
            event.type == pygame.KEYDOWN and (
                event.key == pygame.K_ESCAPE or 
                event.key == pygame.K_q                
            )):
            pygame.quit()
            quit()
while True:
    event_handler()
    pygame.display.update()