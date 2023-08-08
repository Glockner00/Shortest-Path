import help as hf
from heapq import heappop, heappush
import time
"""
start node : id=6821302 latlon = 59.3067734 14.4666375
end node   : id= 936792883 latlon = 59.3092168 14.4834248

f is the total cost for the node
g is the distance between the current node an the start-node
h is the estimated distance from the current node to the end node.

59.3092150, 14.4846030
59.31070446765066, 14.47589119099817
f = g + h
"""
def astar(start_node, end_node):
    start_id = hf.get_osmID(start_node[0], start_node[1])
    f_dist = {}
    f_dist[start_id] = 0
    g_dist = {}
    g_dist[start_id] = 0
    came_from = {}
    came_from[start_id] = 0
    queue = [(0, start_id)]

    start_time = time.time()
    while queue:
        current_f_distance, current_node_id = heappop(queue)
        if current_node_id == hf.get_osmID(end_node[0], end_node[1]):
            print("Found destination")
            end_time = time.time()
            final_time = end_time - start_time
            return f_dist, came_from, final_time


        neighbors = hf.get_neighbors(current_node_id, hf.get_osmID(end_node[0], end_node[1]))
        for k, v in neighbors.items():
            for element in v:
                neighbor_id, neighbor_latlon, neighbor_edge_cost, neighbor_h = hf.get_information(element)
                temp_g_distance = g_dist[current_node_id] + neighbor_edge_cost
                if temp_g_distance < g_dist.get(neighbor_id, float('inf')):
                    g_dist[neighbor_id] = temp_g_distance
                    f_dist[neighbor_id] = temp_g_distance + neighbor_h
                    came_from[neighbor_id] = current_node_id
                    heappush(queue, (f_dist[neighbor_id], neighbor_id))
    return None, None, None


def information():
    start = (59.3067734,14.4666375)
    end = (59.3092168,14.4834248)
    f_dist, came_from, t = astar(start, end)

    current_node_id = hf.get_osmID(end[0], end[1])
    distance = f_dist[current_node_id]

    print("\n")
    if f_dist is not None:
        current_node_id = hf.get_osmID(end[0], end[1])
        astar_path = [current_node_id]
        while current_node_id != hf.get_osmID(start[0], start[1]):
            current_node_id = came_from[current_node_id]
            astar_path.append(current_node_id)
        astar_path.reverse()

        for node_id in astar_path:
            lat, lon = hf.get_lat_lon(node_id)
            print("node id:",node_id, "lat/lon:",lat, lon)

    distance_in_km = distance / 1000
    formatted_distance = "{:.1f}".format(distance_in_km)

    print("\nDistance:", formatted_distance, "km")
    print("Number of nodes in the shortest path:", len(astar_path))
    print("Execution time : ", t, " seconds")


def main():
    information()

if __name__ == "__main__":
    main()
