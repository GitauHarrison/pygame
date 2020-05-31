import pygame, random, sys
from pygame.locals import *

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

    mouse_x = 0
    mouse__y = 0
    pygame.display.set_caption('Memory Puzzle Game')

    main_board = getRandomizedBoard()
    revealed_boxes = generateRevealedBoxesData(False)

    first_selection = None

    display_surf.fill(bg_color)
    startGameAnimation(main_board)

    while True:
        mouse_clicked = False

        display_surf.fill(bg_color)
        drawBoard(main_board, revealed_boxes)

        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYUP and event.type == K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:
                mouse_x, mouse_x = event.pos
            elif event.type == MOUSEBUTTONUP:
                mouse_x, mouse__y = event.pos
                mouse_clicked = True
        
        box_x, box_y = getBoXAtPixel(mouse_x, mouse__y)
        if box_x != None and box_y != None:
            # if mouse is currently over a box
            if not revealed_boxes[box_x][box_y]:
                draw_highlight_box(box_x, box_y)
            if not revealed_boxes[box_x][box_y] and mouse_clicked:
                revealed_boxes_animation(main_board, [box_x, box_y])
                revealed_boxes[box_x][box_y] = True # set the box as revealed

                # the current box was the first box clicked
                if first_selection == None:
                    first_selection  = box_x, box_y
                # the current box was the second box clicked
                else:
                    # check if there was a match between the two icons
                    icon_1_shape, icon_1_color = get_shape_and_color(main_board, first_selection[0], first_selection[1])
                    icon_2_shape, icon_2_color = get_shape_and_color(main_board, box_x, box_y)

                    if icon_1_shape != icon_2_shape or icon_1_color != icon_2_color:
                        pygame.time.wait(1000)            
                        cover_boxes_animation(main_board, [(first_selection[0], first_selection[1]), box_x, box_y])
                        revealed_boxes[first_selection[0]][first_selection[1]] = False
                        revealed_boxes[box_x, box_y] = False
                    elif hasWon(revealed_boxes):
                        game_won_animation(main_board)
                        pygame.time.wait(1000)

                        # Reset the board
                        main_board = getRandomizedBoard()
                        revealed_boxes = generateRevealedBoxesData(False)

                        # Show the fully unrevealed board for a second
                        draw_board(main_board, revealed_boxes)
                        pygame.display.update()
                        pygame.time.wait(1000)

                        # Replay the start game animation
                        start_game_animation(main_board)
                    first_selection = None # reset first selection variable
        
        # redraw the screen and wait for a clock tick
        pygame.display.update()
        fps_clock.tick(fps)

def generateRevealedBoxesData(val):
    revealed_boxes = []
    for i in range (board_width):
        revealed_boxes.append([val] * board_height)
    return revealed_boxes

def getRandomizedBoard():
    # get a list of every possible shape in every possible color
    icons = []
    for color in all_colors:
        for shape in all_shapes:
            icons.append((shape, color))

    random.shuffle(icons) # randomize the order of the icons list
    num_icons_used = int(board_width * board_height / 2) # calculate how many icons are needed
    icons = icons[:num_icons_used] * 2 # make two of each
    random.shuffle(icons)

    # create the board data structure, with randomly placed icons
    board = []
    for x in range(board_width):
        column = []
        for y in range(board_height):
            column.append(icons[0])
            del icons[0] # remove icons as we assign them
        board.append(column)
    return board

def splitIntoGroupsOf(group_size, the_list):
    # split a list into a list of lists, where the inner lists have at most group_size number of items
    result =[]
    for i in range(0, len(the_list), group_size):
        result.append(the_list[i:i + group_size])
    return result