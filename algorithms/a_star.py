# implement a potential (an estimate of the distance from the node to the end node)

"""
f(n) = g(n) + h(h) - total estiamed cost of path through node n
g(n) - cost so far to reach node n
h(n) - estimated cost from n to goal, a heuristic. 
    Manhattan distance heuristic
    Euclidean distance heuristic

    1. consider all adj nodes in a list -> filter out inaccessibles.
    2. pick the node with has the lowest cost: the estimated f(n)
    3. repeat recursivly.
"""
import math
from queue import PriorityQueue
import time

# TODO : Try both.
def manhattan_distance(node, goal):
    x1, y1 = node
    x2, y2 = goal
    return abs(x1 - x2) + abs(y1 - y2)

def euclidean_distance(node, goal):
    x1, y1 = node
    x2, y2 = goal
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)


def Astar(G, C, start_node, end_node):
    count = 0
    open_set = PriorityQueue()
    open_set.put((0, count, start_node))
    came_from = {}

    g_score = {node: float('inf') for node in G}
    f_score = {node: float('inf') for node in G}

    g_score[start_node] = 0
    f_score[start_node] = euclidean_distance(C[start_node], C[end_node])

def main():
    # Dictionary representing the graph.
    G = {
    'A': [('B', 6), ('F', 3)],
    'B': [('A', 6), ('C', 3), ('D', 2)],
    'C': [('B', 3), ('D', 1), ('E', 5)],
    'D': [('B', 2), ('C', 1), ('E', 8)],
    'E': [('C', 5), ('D', 8), ('I', 5), ('J', 5)],
    'F': [('A', 3), ('G', 1), ('H', 7)],
    'G': [('F', 1), ('I', 3)],
    'H': [('F', 7), ('I', 2)],
    'I': [('E', 5), ('G', 3), ('H', 2), ('J', 3)],
    }

    # Coordinates for each node.
    C = {
        'A': (0, 0),
        'B': (1, 1),
        'C': (2, 1),
        'D': (2, 0),
        'E': (3, 1),
        'F': (0, 2),
        'G': (1, 3),
        'H': (2, 3),
        'I': (3, 2),
        'J': (4, 1),
    }

    Astar(G, C, 'A', 'H')

if __name__ == "__main__":
    main()