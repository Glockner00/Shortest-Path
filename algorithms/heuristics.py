"""
A simple program for calculating the heuristic value for each node in a weighted graph.
"""

import math
def main():
    """
    How the graph represents nodes, adj nodes and values.
    graph = { 'current node' : { 'adj node' : [edge, heuristic]}}

    How the graph should look after calculating the heuristics.
    the heuristic of each node represents how far it is from the current
    node to the goal node (node F).

    graph = {
        'A': {'B': [2, 2], 'C': [3, 2]},
        'B': {'D': [3, 5], 'E': [1, 1]},
        'C': {'F': [2, 0]},
        'D': {},
        'E': {'F': [1, 0]},
        'F': {}
    }
    """
    # this graph only contains edge lengths.
    # TODO: calculate the heuristic value for each node and add it to the graph.
    graph = {
        'A': {'B': 2, 'C': 3},
        'B': {'D': 3, 'E': 1},
        'C': {'F': 2},
        'D': {},
        'E': {'F': 1},
        'F': {}
    }

    goal = 'F'  # Goal node

    # Calculate heuristic value for each node
    for node in graph:
        for adj_node in graph[node]:
            edge_length = graph[node][adj_node]
            heuristic = math.sqrt((ord(goal) - ord(adj_node)) ** 2)
            graph[node][adj_node] = [edge_length, int(heuristic)]

    for node in graph:
        for adj_node in graph[node]:
            print(node,"-->", adj_node, ":", graph[node][adj_node])

if __name__ == "__main__":
    main()
