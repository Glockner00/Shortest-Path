import pygame
import pickle

from pygame.image import load
# Define constants
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
DO_NOT_DRAW = (1, 1, 1)

WIDTH = 1200
HEIGHT = 1200
TOTAL_ROWS = 100

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
IMAGE = pygame.image.load("images/halfmap.png")
IMAGE_SCALED = pygame.transform.scale(IMAGE, (WIDTH, HEIGHT))
FILENAME = "grid.pickle"


class Tile():
    def __init__(self, row, col, cell_width):
        self.row = row
        self.col = col
        self.cell_width = cell_width
        self.x = cell_width * col
        self.y = cell_width * row
        self.color = DO_NOT_DRAW
        self.neighbors = []
        self.b = False

    def make_start(self):
        self.color = GREEN

    def make_end(self):
        self.color = BLUE

    def make_path(self):
        self.color = GREEN

    def get_pos(self):
        return self.x, self.y

    def make_barrier(self):
        self.color = BLACK

    def reset(self):
        self.color = DO_NOT_DRAW

    # Draw a single tile
    def draw(self, win):
        if self.color != DO_NOT_DRAW:
            pygame.draw.rect(
                win, self.color, (self.x, self.y,
                                  self.cell_width, self.cell_width))


def make_grid():
    grid = []
    gap = WIDTH // TOTAL_ROWS
    for i in range(TOTAL_ROWS):
        grid.append([])
        for j in range(TOTAL_ROWS):
            tile = Tile(i, j, gap)
            grid[i].append(tile)
    return grid


def draw(win, grid):
    win.fill(WHITE)  # Fill the window with transparent color
    win.blit(IMAGE_SCALED, (0, 0))  # Draw the image on top of the window
    for row in grid:
        for tile in row:
            tile.draw(win)

    draw_grid(win)
    pygame.display.update()


def draw_grid(win):
    gap = WIDTH // TOTAL_ROWS
    for i in range(TOTAL_ROWS):
        pygame.draw.line(win, BLUE, (0, i*gap), (WIDTH, i * gap))
        for j in range(TOTAL_ROWS):
            pygame.draw.line(win, BLUE, (j * gap, 0), (j * gap, WIDTH))


def mouse_clicked_position(pos, row, width):
    gap = width // row  # width of each cube
    x, y = pos
    col = x // gap
    row = y // gap
    return row, col


def save_grid(grid, filename):
    with open(filename, 'wb') as file:
        pickle.dump(grid, file)


def load_grid(filename):
    with open(filename, 'rb') as file:
        grid = pickle.load(file)
    return grid


def main(win):
    grid = load_grid(FILENAME)

    run = True
    while run:
        draw(win, grid)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            # LEFT CLICK - make barrier
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                row, col = mouse_clicked_position(pos, TOTAL_ROWS, WIDTH)
                grid[row][col].make_barrier()

            # RIGHT CLICK - reset Tile
            if pygame.mouse.get_pressed()[2]:
                pos = pygame.mouse.get_pos()
                row, col = mouse_clicked_position(pos, TOTAL_ROWS, WIDTH)
                tile = grid[row][col]
                tile.reset()

    save_grid(grid, FILENAME)
    pygame.quit()


if __name__ == "__main__":
    pygame.init()
    main(WIN)
