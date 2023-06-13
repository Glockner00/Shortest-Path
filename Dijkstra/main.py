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
"""

def selectMinVertex(value, processed):
    pass



def dijkstra(graph):
    pass 



if __name__ == "__main__":
    graph = [[0, 1, 4, 0, 0, 0],
             [1, 0, 4, 2, 7, 0],
             [4, 4, 0, 3, 5, 0],
             [0, 2, 3, 0, 4, 6],
             [0, 7, 5, 4, 0, 7],
             [0, 0, 0, 6, 7, 0]]
    dijkstra(graph)
