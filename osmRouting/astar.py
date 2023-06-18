import helpNew as hf
from heapq import heappop, heappush
import json

class Node:
    def __init__(self, id, x, y, parent, cost, heuristic):
        self.id = id
        self.x = x
        self.y = y
        self.parent = parent
        self.cost = cost
        self.heuristic = heuristic
    
    def __lt__ (self, other):
        return (self.cost + self.heuristic) < (other.cost + other.heuristic)
        
def a_star(start_id, end_id):
    start_coordinates = hf.get_lat_lon(start_id)
    end_coordinates = hf.get_lat_lon(end_id)

    h_cost = hf.get_heuristic(start_coordinates, end_coordinates)
    start_node = Node(start_id, start_coordinates[0], start_coordinates[1], None, 0, h_cost)
    
    queue = [start_node]
    node = heappop(queue)
    print(node)
    next_moves = hf.get_neighbors(node.id, end_id)
    print(json.dumps(next_moves, indent=2))

def main():
    start_id = "6821312"
    dest_id = "2571591346"
    a_star(start_id, dest_id)

if __name__ == "__main__":
    main()