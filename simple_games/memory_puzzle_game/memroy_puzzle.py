import pygame, random, sys
from pygame import locals

fps = 30
window_width = 640
window_height = 460
revealed_speed = 8
box_size = 40
gap_size = 10
board_width = 10
board_height = 7
assert (board_width * board_height) % 2 == 0, 'Board needs to have an even number of boxes for pairs of matches.'
x_margin = int((window_width - (board_width * (box_size + gap_size))) / 2)
y_margin = int((window_height - (board_height * (box_size + gap_size))) / 2)

gray = (100, 100, 100)
navy_blue = (60, 60, 100)
white = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
orange = (255, 128, 0)
purple = (255, 0, 255)
cyan = (0, 255, 255)

bg_color = navy_blue
light_bg_color = gray
box_color = white
highlight_color = blue

donut = 'donut'
square = 'square'
diamond = 'diamond'
lines = 'lines'
oval = 'oval'

all_colors = (red, green, blue, yellow, orange, purple, cyan)
all_shapes = (donut, square, diamond, lines, oval)
assert len(all_colors) * len(all_shapes) * 2 >= board_width * board_height, 'Board is too big for the number of shapes/colors defined'

def main():
    global fps_clock, display_surf
    pygame.init()
    fps_clock = pygame.time.Clock()
    dispay_surf = pygame.display.set_mode(window_height, window_width)