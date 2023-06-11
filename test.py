import pygame
from pygame.locals import *

# Constants
RED = (255, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (128, 128, 128)
TRANSPARENT = pygame.Color(255, 0, 0)

WIDTH = 1150
HEIGHT = 1800
ROWS = 150
COLS = 200

WIN = pygame.display.set_mode((HEIGHT, WIDTH))
image = pygame.image.load("mapnew.png")
image = pygame.transform.scale(image, (HEIGHT, WIDTH))


class Tile:
    # Constructor
    def __init__(self, row, col, width, total_rows):
        self.row = row
        self.col = col
        self.width = width
        self.total_rows = total_rows
        self.x = row * width
        self.y = col * width
        self.color = TRANSPARENT
        self.neighbours = []

    def get_pos(self):
        return self.row, self.col
    
    def is_barrier(self):
        return self.color == BLACK
    
    def is_start(self):
        return self.color == GREEN
    
    def is_end(self):
        return self.color == RED
    
    def reset(self):
        self.color = TRANSPARENT
    
    def make_start(self):
        self.color = GREEN
    
    def make_barrier(self):
        self.color = BLACK
    
    def make_end(self):
        self.color = RED
    
    def make_path(self):
        self.color = GREEN

    # Draw a single tile
    def draw(self, win):
        if self.color != TRANSPARENT:  # Draw only if the color is not transparent
            pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))

    # Check if neighbours are barriers or not.
    def update_neighbours(self, grid):
        self.neighbours = []
        # Down
        if self.row < self.total_rows - 1 and not grid[self.row + 1][self.col].is_barrier():
            self.neighbours.append(grid[self.row + 1][self.col])
        # Up
        if self.row > 0 and not grid[self.row - 1][self.col].is_barrier():
            self.neighbours.append(grid[self.row - 1][self.col])
        # Left
        if self.col > 0 and not grid[self.row][self.col - 1].is_barrier():
            self.neighbours.append(grid[self.row][self.col - 1])
        # Right
        if self.col < self.total_rows - 1 and not grid[self.row][self.col + 1].is_barrier():
            self.neighbours.append(grid[self.row][self.col + 1])

    # "less than", compares lt tile and other tile.
    # The other tile is always going to be greater than lt:s tile
    def __lt__(self, other):
        return False


# draw every tile and grid on top.
# drawing the grid is temporary.
def draw(win, grid, rows, width):
    win.fill(WHITE)  # Fill the window with transparent color
    win.blit(image, (0, 0))  # Draw the image on top of the window

    for row in grid:
        for tile in row:
            tile.draw(win)

    draw_grid(win, rows, width, HEIGHT)
    pygame.display.update()


def draw_grid(win, rows, width, height):
    gap = width // rows  # width of each cube.
    for i in range(rows):
        # Vertical lines
        pygame.draw.line(win, GREY, (0, i * gap), (width, i * gap))
        for j in range(rows):

            # Horizontal lines
            pygame.draw.line(win, GREY, (j * gap, 0), (j * gap, height))


# 2d array of a grid.
def make_grid(rows, cols, width):
    grid = []
    gap = width // rows
    for i in range(rows):
        grid.append([])
        for j in range(cols):
            tile = Tile(i, j, gap, rows)
            grid[i].append(tile)
    return grid


def main(win, width):
    grid = make_grid(ROWS, COLS, width)
    run = True
    pygame.display.set_caption(" ")

    while run:
        draw(win, grid, ROWS, width)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

    pygame.quit()


if __name__ == "__main__":
    pygame.init()
    main(WIN, WIDTH)
