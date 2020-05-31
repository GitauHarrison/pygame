import pygame, random, sys
from pygame.locals import *

fps = 30
window_width = 640
window_height = 460
reveal_speed = 8
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
                reveal_boxes_animation(main_board, [box_x, box_y])
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

def left_top_coords_of_box(box_x, box_y):
    # convert board coordinates to pixel coordinates 
    left = box_x * (box_size + gap_size) + x_margin
    top = box_y * (box_size + gap_size) + y_margin
    return (left, top)

def getBoxAtPixel(x, y):
    for bax_x in range(board_width):
        for box_y in range(board_height):
            left, top = left_top_coords_of_box(box_x, box_y)
            box_rect = pygame.Rect(left, top, box_size, box_size)
            if box_rect.collide_point(x, y):
                return (box_x, box_y)
    return (None, None)

def drawIcon(shape, color, box_x, box_y):
    quarter = int((box_size * 0.25)) # syntactic sugar
    half = int(box_size * 0.5) # syntactic sugar

    left, top = left_top_coords_of_box(box_x, box_y) # get pixel coordinates from board coordinates

    # draw the shapes
    if shape == donut:
        pygame.draw.circle(display_surf, color, (left + half, top + half), half - 5)
        pygame.draw.circle(display_surf, bg_color, (left + half, top + half), quarter - 5)
    elif shape == square:
        pygame.draw.rect(display_surf, color, (left + quarter, top + quarter, box_size - half, box_size - half))
    elif shape == diamond:
        pygame.draw.polygon(display_surf, color, ((left + half, top), (left + box_size - 1, top + half), (left + half, top + box_size - 1), (left, top + half)))
    elif shape == lines:
        for i in range(0, box_size, 4):
            pygame.draw.line(display_surf, color, (left, top + i), (left + i, top))
            pygame.draw.line(display_surf, color, (left + i, top + box_size - 1), (left + box_size - 1, top + i))
    elif shape == oval:
        pygame.draw.ellipse(display_surf, color, (left, top + quarter, box_size, half))

def get_shape_and_color(board, box_x, box_y):
    # shape value for x,y spot is stored in board[x][y][0]
    #color value for x,y spot is stored in board[x][y][1]
    return board[box_x][box_y][0], board[box_x][box_y][1]

def draw_box_covers(board, boxes, coverage):
    # Draw boxes being covered/revealed
    # 'boxes' is a list of two-item lists, which have the x & y spot of the box
    for box in boxes:
        left, top = left_top_coords_of_box(box[0], box[1])
        pygame.draw.rect(display_surf, bg_color, (left,top, box_size, box_size))
        shape, color = get_shape_and_color(board, (box[0], box[1]))
        drawIcon(shape, color, box[0], box[1])
        if coverage > 0: #only draw the cover if there is a coverage
            pygame.draw.rect(display_surf, box_color, (left, top, coverage, box_size))
    pygame.display.update()
    fps_clock.tick(fps)

def reveal_boxes_animation(board, boxes_to_reveal):
    # Do the box reveal animation
    for coverage in range(box_size, (-reveal_speed) - 1, - reveal_speed):
        draw_box_covers(board, boxes_to_reveal, coverage)