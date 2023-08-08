"""
How the algorithm works.

set all the weights between the nodes. --> 2d-array, graph.
set arrays: value = 0(source-node), inf ,inf ,inf ,inf ,inf
			parent = -1, -1, -1, -1, -1, -1 (currently no parents)
            processed = False, False, False, False, False

for nodes-1 itterations.

    1.	pick a minimum value node that is not yet processed.
	2.	mark the minumum node as processed.
	3.	udate all the adj verticies. The nodes moves from U-->V.
		if (value[U](weight at current node.) + graph[U][V](weight to the new node) < value[V](current weight at new node)):
			update
        else:
			continue

    # Three conditions to consider
    # 1. The edge is present from U to j.
    # 2. The vertex j is not included in the shortest path graph
    # 3. The edge weight is smaller than the current edge weight.
"""

import sys
import time

# Returns the node that has the smallest value. --> processing.
def selectMinVertex(value, processed, V):
    minimum = sys.maxsize
    node = None
    for i in range(V):
        if not processed[i] and value[i] < minimum:
            node = i
            minimum = value[i]
    return node


def dijkstra(graph, V):
    parent = [-1] * V         # Stores each node's parent.
    value = [sys.maxsize] * V # Stores shortest path to each node.
    processed = [False] * V   # Determines which node to be processed.

    parent[0] = -1  # The first element is the start node
    value[0] = 0    # Which means that the start-node has no value.

    start_time = time.time()  # Start the timer

    for i in range(V - 1):
        U = selectMinVertex(value, processed, V)
        processed[U] = True
        for j in range(V):
            if (graph[U][j] != 0
                and not processed[j]
                and value[U] != sys.maxsize
                and (value[U] + graph[U][j] < value[j])):
                    value[j] = value[U] + graph[U][j]
                    parent[j] = U

    end_time = time.time()  # Stop the timer

    print("\nVisualization of the algorithm.")
    for i in range(1, V):
        if parent[i] != -1:
            print(f"U --> V: {parent[i]} --> {i} weight = {graph[parent[i]][i]}")

    # Print shortest path from node 1 to node 5
    path = []
    node = 5
    total_weight = value[5]
    while node != -1:
        path.append(node)
        node = parent[node]
    path.reverse()
    print("\nShortest path:", path)
    print("Total weight:", total_weight)
    print("Execution time:", end_time - start_time, "seconds")


def main():
    V = 6
    graph = [[0, 1, 4, 0, 0, 0],
             [1, 0, 4, 2, 7, 0],
             [4, 4, 0, 3, 5, 0],
             [0, 2, 3, 0, 4, 6],
             [0, 7, 5, 4, 0, 7],
             [0, 0, 0, 6, 7, 0]]
    dijkstra(graph, V)


if __name__ == "__main__":
    main()
