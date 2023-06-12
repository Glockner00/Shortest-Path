import pygame
import pickle
from queue import PriorityQueue

# Define constants
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
DO_NOT_DRAW = (1, 1, 1)

WIDTH = 1200
HEIGHT = 1200
TOTAL_ROWS = 150

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
IMAGE = pygame.image.load("images/halfmap.png")
IMAGE_SCALED = pygame.transform.scale(IMAGE, (WIDTH, HEIGHT))
FILENAME = "grid.pickle"

# TODO:
# 1.      Map out where it is allowed to run.
# 2.      Change barriers to a bool.
# 3.      Implement A*.
# 4.      Figure out how to choose start point and end point.
# 5.          - Click for position?
# 6.          - Select two numbers on the map?
# 7.      Remove make_grid and draw_grid and all other visuall representation.
# 8.      Make an app/interface that is somewhat useable.


class Tile():
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.cell_width = WIDTH // TOTAL_ROWS
        self.x = self.cell_width * col
        self.y = self.cell_width * row
        self.color = DO_NOT_DRAW
        self.neighbors = []
        self.start = False
        self.end = False

    
    def is_closed(self):
        return self.color == RED

    def is_opened(self):
        return self.color == GREEN
    
    def is_barrier(self):
        return self.color == BLACK
    
    def is_start(self):
        if self.start:
            return True
        return False

    def is_end(self):
        if self.end:
            return True
        return False
    
    def make_start(self):
        self.color = GREEN
        self.start = True

    def make_end(self):
        self.color = BLUE
        self.end = False

    def make_path(self):
        self.color = GREEN

    def make_closed(self):
        self.color = RED

    def make_open(self):
        self.color = DO_NOT_DRAW

    def get_pos(self):
        return self.x, self.y

    def make_barrier(self):
        self.color = BLACK

    def reset(self):
        self.color = DO_NOT_DRAW
        self.end = False
        self.start = False

    # Draw a single tile
    def draw(self, win):
        if self.color == GREEN or self.color == BLUE:
            pygame.draw.rect(
                win, self.color, (self.x, self.y,
                                  self.cell_width, self.cell_width))
    
    # Check if neighbours are barriers or not.
    def update_neighbours(self, grid):
        self.neighbours = []
        # Down
        if self.row < TOTAL_ROWS - 1 and not grid[self.row + 1][self.col].is_barrier():
            self.neighbours.append(grid[self.row + 1][self.col])
        # Up
        if self.row > 0 and not grid[self.row - 1][self.col].is_barrier():
            self.neighbours.append(grid[self.row - 1][self.col])
        # Left
        if self.col > 0 and not grid[self.row][self.col - 1].is_barrier():
            self.neighbours.append(grid[self.row][self.col - 1])
        # Right
        if self.col < TOTAL_ROWS - 1 and not grid[self.row][self.col + 1].is_barrier():
            self.neighbours.append(grid[self.row][self.col + 1])

    # "less than", compares lt tile and other tile.
    # The other tile is always going to be greater than lt:s tile
    def __lt__(self, other):
        return False
    
# Main algorithm.
def a_star(draw, grid, start, end):
    count = 0  # Keeps track of the queue
    open_set = PriorityQueue()
    # Adding the start node with the original f-score (which is zero)
    open_set.put((0, count, start))
    came_from = {}  # keeps track of which node we came from

    # a table with a uniqe key for every tile.
    g_score = {tile: float("inf") for row in grid for tile in row}
    g_score[start] = 0  # start nodes g score.

    # a table with a uniqe key for every tile.
    f_score = {tile: float("inf") for row in grid for tile in row}
    # Heuristic, makes an estimate how far the end node is from the start node.
    f_score[start] = h(start.get_pos(), end.get_pos())  # start nodes f score.

    # keeps track of all the items in/not in the PriorityQueue
    open_set_hash = {start}  # set

    # if the set i empty we have checked all the possible node.
    while not open_set.empty():
        for event in pygame.event.get():
            #  A way of exiting the algorithm.
            if event.type == pygame.QUIT:
                pygame.quit()

        # if we get the same f score we will instead look at the count
        # (PriorityQueue).
        current = open_set.get()[2]  # the node.

        # take the node that poped of the PriorityQueue and sync the hash.
        # ensures that there are no duplicates.
        open_set_hash.remove(current)

        if current == end:  # path found.
            path(came_from, end, draw)
            return True

        # all edges are 1, neighbours g_score -> distance to current node
        # (currently known shortest distance) and add 1
        for neighbour in current.neighbours:
            temp_g_score = g_score[current] + 1

            # Found a shorter way
            if temp_g_score < g_score[neighbour]:
                came_from[neighbour] = current
                g_score[neighbour] = temp_g_score
                f_score[neighbour] = temp_g_score + h(neighbour.get_pos(),
                                                      end.get_pos())
                if neighbour not in open_set_hash:
                    count += 1
                    open_set.put((f_score[neighbour], count, neighbour))
                    open_set_hash.add(neighbour)
                    neighbour.make_open()

        draw()

        if current != start:
            current.make_closed()
    return False

    
    
# Heuristic function for the main algorithm.
# Returns the distance between point 1 and point 2 using manhattan distance
def h(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x2 - x1) + abs(y2 - y1)


# Reconstruct the path.
def path(came_from, current_tile, draw):
    while current_tile in came_from:
        current_tile = came_from[current_tile]
        current_tile.make_path()
        draw()


def draw(win, grid):
    win.fill(WHITE)
    win.blit(IMAGE_SCALED, (0, 0))
    for row in grid:
        for tile in row:
            tile.draw(win)
    pygame.display.update()



def mouse_clicked_position(pos, row):
    gap = WIDTH//row  # width of each cube
    x, y = pos
    col = x // gap
    row = y // gap
    return row, col


def load_grid(filename):
    with open(filename, 'rb') as file:
        grid = pickle.load(file)
    return grid

def reset_grid(grid):
    for row in grid:
        for tile in row:
            if(tile.color == GREEN or tile.color == BLUE):
                tile.reset()
    return grid


def main(win):
    grid = load_grid(FILENAME)
    run = True
    start = None
    end = None


    while run:
        draw(win, grid)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            # LEFT CLICK - make barrier
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                row, col = mouse_clicked_position(pos, TOTAL_ROWS)
                tile = grid[row][col]

                # First click
                if not start and tile != end:
                    start = tile
                    tile.make_start()

                # Second click
                if not end and tile != start:
                    end = tile
                    tile.make_end()

                # Third click
                if tile != end and tile != start:
                    tile.make_barrier()

            # RIGHT CLICK - reset Tile
            if pygame.mouse.get_pressed()[2]:
                pos = pygame.mouse.get_pos()
                row, col = mouse_clicked_position(pos, TOTAL_ROWS)
                tile = grid[row][col]
                tile.reset()

            
             # Key down, start algorithm
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and start and end:
                    for row in grid:
                        for tile in row:
                            tile.update_neighbours(grid)
                    # Lambda calls an anonymous function
                    # Allows for calling this specifik draw in a_star.
                    a_star(lambda: draw(win, grid),
                           grid, start, end)
                if event.key == pygame.K_r:
                    grid = reset_grid(grid)
                    start = None
                    end = None
                

    pygame.quit()


if __name__ == "__main__":
    pygame.init()
    main(WIN)
