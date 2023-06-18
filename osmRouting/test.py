import help as hf
from heapq import heappop, heappush
import json

class Node:
    def __init__(self, x, y, parent, cost, heuristic):
        self.x = x
        self.y = y
        self.parent = parent
        self.cost = cost
        self.heuristic = heuristic
    
    def __lt__ (self, other):
        return (self.cost + self.heuristic) < (other.cost + other.heuristic)
    
def a_star(start_id, end_id):
    dist = {}
    h_cost = hf.get_heuristic(hf.get_lat_lon(start_id), hf.get_lat_lon(end_id))
    x,y = hf.get_lat_lon(start_id)
    start_node = Node(x,y, None, 0, h_cost)

    queue = [start_node]
    neighbors = hf.get_neighbors(start_id, end_id)
    

    for k, v in neighbors.items():
        for element in v:
            id, h, cost = hf.get_information(element)
            print("id: ", id, "cost: ", cost, "h: ", h, "\n")


def main():
    start_id = "6821312"
    dest_id = "2571591346"
    a_star(start_id, dest_id)

if __name__ == "__main__":
    main()