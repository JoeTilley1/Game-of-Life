# The Game of Life
# By Joe Tilley
import pygame, math, os
from pygame.locals import *


# Initial Setup
os.environ['SDL_VIDEO_WINDOW_POS'] = "3,27"
WINDOWWIDTH = 1360
WINDOWHEIGHT = 700
pygame.init()
playSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('The Game of Life')

# Defining the cells
CELLSIZE = 20
assert WINDOWWIDTH % CELLSIZE == 0, "Window width must be a multiple of cell size."
assert WINDOWHEIGHT % CELLSIZE == 0, "Window height must be a multiple of cell size."
CELLWIDTH = int(WINDOWWIDTH / CELLSIZE)
CELLHEIGHT = int(WINDOWHEIGHT / CELLSIZE)

# Colours
whiteColour = pygame.Color(255, 255, 255)
blackColour = pygame.Color(0, 0, 0)
greyColour = pygame.Color(150, 150, 150)

# Make board
board = [[]]
for row in range(0, CELLHEIGHT):
    board[0].append(["."]*CELLWIDTH)

# Define Glider Gun
def glider_gun():
    board[0][2][26] = "O"
    board[0][3][24] = "O"
    board[0][3][26] = "O"
    board[0][4][14] = "O"
    board[0][4][15] = "O"
    board[0][4][22] = "O"
    board[0][4][23] = "O"
    board[0][4][36] = "O"
    board[0][4][37] = "O"
    board[0][5][13] = "O"
    board[0][5][17] = "O"
    board[0][5][22] = "O"
    board[0][5][23] = "O"
    board[0][5][36] = "O"
    board[0][5][37] = "O"
    board[0][6][2] = "O"
    board[0][6][3] = "O"
    board[0][6][12] = "O"
    board[0][6][18] = "O"
    board[0][6][22] = "O"
    board[0][6][23] = "O"
    board[0][7][2] = "O"
    board[0][7][3] = "O"
    board[0][7][12] = "O"
    board[0][7][16] = "O"
    board[0][7][18] = "O"
    board[0][7][19] = "O"
    board[0][7][24] = "O"
    board[0][7][26] = "O"
    board[0][8][12] = "O"
    board[0][8][18] = "O"
    board[0][8][26] = "O"
    board[0][9][13] = "O"
    board[0][9][17] = "O"
    board[0][10][14] = "O"
    board[0][10][15] = "O"

# Insert Glider Gun
glider_gun()

# Display Initial Setup
for row in range(0, CELLHEIGHT):
        for col in range(0, CELLWIDTH):
            if board[0][row][col] == "O":
                pygame.draw.rect(playSurface, whiteColour, Rect(col*20, row*20, 20, 20))
            if board[0][row][col] == ".":
                pygame.draw.rect(playSurface, blackColour, Rect(col*20, row*20, 20, 20))

# Draw Grid
for x in range(0, WINDOWWIDTH, CELLSIZE): # draw vertical lines
    pygame.draw.line(playSurface, greyColour, (x, 0), (x, WINDOWHEIGHT))
for y in range(0, WINDOWHEIGHT, CELLSIZE): # draw horizontal lines
    pygame.draw.line(playSurface, greyColour, (0, y), (WINDOWWIDTH, y))

# Update board
pygame.display.flip()

# Let User decide starting board
while True:
    event = pygame.event.wait()
    if event.type == pygame.MOUSEBUTTONUP:
        mousex, mousey = pygame.mouse.get_pos()
        mouserow = math.floor(mousey/CELLSIZE)
        mousecolumn = math.floor(mousex/CELLSIZE)
        if board[0][mouserow][mousecolumn] == "O":
            board[0][mouserow][mousecolumn] = "."
            pygame.draw.rect(playSurface, blackColour, Rect(mousecolumn*20, mouserow*20, 20, 20))
            #Draw Grid
            for x in range(0, WINDOWWIDTH, CELLSIZE): # draw vertical lines
                pygame.draw.line(playSurface, greyColour, (x, 0), (x, WINDOWHEIGHT))
            for y in range(0, WINDOWHEIGHT, CELLSIZE): # draw horizontal lines
                pygame.draw.line(playSurface, greyColour, (0, y), (WINDOWWIDTH, y))
            pygame.display.flip()
        else:
            board[0][mouserow][mousecolumn] = "O"
            pygame.draw.rect(playSurface, whiteColour, Rect(mousecolumn*20, mouserow*20, 20, 20))
            #Draw Grid
            for x in range(0, WINDOWWIDTH, CELLSIZE): # draw vertical lines
                pygame.draw.line(playSurface, greyColour, (x, 0), (x, WINDOWHEIGHT))
            for y in range(0, WINDOWHEIGHT, CELLSIZE): # draw horizontal lines
                pygame.draw.line(playSurface, greyColour, (0, y), (WINDOWWIDTH, y))
            pygame.display.flip()
    if event.type == KEYDOWN:
        if event.key == K_SPACE:
            break
        else:
            pass
    if event.type == QUIT:
            pygame.quit()
    else:
        pass

# Start Game Logic

for its in range(0,2**10000):
    pygame.time.wait(100)   # How long generation is shown for
    board.append([])    # Make new generation
    for row in range(0, CELLHEIGHT):
        board[its+1].append(["."]*CELLWIDTH)    # Fill new generation with dead cells
    for row in range(0, CELLHEIGHT):
        for col in range(0, CELLWIDTH):         #Tests whether neighbours are alive or dead
            neighbours = 0
            if row > 0:
                if col > 0:
                    if board[its][row-1][col-1] == "O":
                        neighbours += 1
                if board[its][row-1][col] == "O":
                    neighbours += 1
                if col < CELLWIDTH-1:
                    if board[its][row-1][col+1] == "O":
                        neighbours += 1
            if col > 0:
                if board[its][row][col-1] == "O":
                    neighbours += 1
            if col < CELLWIDTH-1:
                if board[its][row][col+1] == "O":
                    neighbours += 1
            if row < CELLHEIGHT-1:
                if col > 0:
                    if board[its][row+1][col-1] == "O":
                        neighbours += 1
                if board[its][row+1][col] == "O":
                    neighbours += 1
                if col < CELLWIDTH-1:
                    if board[its][row+1][col+1] == "O":
                        neighbours += 1

            # Determining if next generation will be alive or dead and changing colour
            if board[its][row][col] == "O":
                if neighbours == 2 or neighbours == 3:
                    board[its+1][row][col] = "O"
                else:
                    board[its+1][row][col] = "."
                    pygame.draw.rect(playSurface, blackColour, Rect(col*20, row*20, 20, 20))
            elif board[its][row][col] == ".":
                if neighbours == 3:
                    board[its+1][row][col] = "O"
                    pygame.draw.rect(playSurface, whiteColour, Rect(col*20, row*20, 20, 20))
                else:
                    board[its+1][row][col] = "."
            else:
                print("Something has fucked up here")

    # Draw Grid
    for x in range(0, WINDOWWIDTH, CELLSIZE): # draw vertical lines
        pygame.draw.line(playSurface, greyColour, (x, 0), (x, WINDOWHEIGHT))
    for y in range(0, WINDOWHEIGHT, CELLSIZE): # draw horizontal lines
        pygame.draw.line(playSurface, greyColour, (0, y), (WINDOWWIDTH, y))

    # Update screen
    pygame.display.flip()

    # End Game scenario
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
