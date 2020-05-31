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