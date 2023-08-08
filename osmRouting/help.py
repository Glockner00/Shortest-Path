import convertToGraphml as ctg
import math
import astar as a

graphml_path = 'data/map.graphml'
xmldoc = ctg.parseXML(graphml_path)
items = xmldoc.getElementsByTagName('node')

def get_osmID(lat, lon):
    for node in items:
        data_elements = node.getElementsByTagName('data')
        if(data_elements[0].firstChild.data == str(lat) and data_elements[1].firstChild.data == str(lon)):
            return node.getAttribute('id')
    return None

def get_lat_lon(osmID): 
    list = []
    for node in items:
        if(str(node.getAttribute('id')) == str(osmID)):
            data_elements = node.getElementsByTagName('data')
            list.append(float(data_elements[0].firstChild.data))
            list.append(float(data_elements[1].firstChild.data))
            return list
    return None

def get_neighbors(osmID, destination_node):
    neighbor_info = {}
    neighbor_list = []
    length = 0

    item = xmldoc.getElementsByTagName('edge')
    for edge in item:
        if edge.getAttribute('source') == osmID:
            tmp = {}
            neighbor = edge.getAttribute('target')
            data_elements = edge.getElementsByTagName('data')
            for data in data_elements:
                if data.getAttribute('key') == "d14":
                    length = data.firstChild.data
            
            latlon_neighbor = get_lat_lon(neighbor)
            heuristic = get_heuristic1(latlon_neighbor, get_lat_lon(destination_node))
            tmp[neighbor] = [latlon_neighbor, length, heuristic]
            neighbor_list.append(tmp)

    neighbor_info[osmID] = neighbor_list
    return neighbor_info

def get_heuristic(current_node, destination_node):
    x1,y1 = current_node
    x2,y2 = destination_node
    return (math.sqrt(((x2-x1)**2)+((y2-y1)**2)))

def get_heuristic1(current_node, destination_node):
    x1,y1 = current_node
    x2,y2 = destination_node
    return abs(x2 - x1) + abs(y2 - y1)

def get_information1(neighbors):
    id = 0
    h = 0
    cost = 0
    for k, v in neighbors.items():
        for element in v:
            for key, value in element.items():
                id = key
                cost = value[1]
                h = value[2]
    return id, h ,cost

def get_information(neighbor):
    id = 0
    h = 0
    cost = 0
    for k, v in neighbor.items():
        id = k
        h = v[2]
        cost = v[1]
    return id, get_lat_lon(id), float(cost), float(h)


def get_urlpath_parameter(start, end):
    path = "color:0x0000ff|weight:5|"
    f_dist, came_from, t = a.astar(start, end)
    if f_dist is not None:
        current_node_id = get_osmID(end[0], end[1])
        astar_path = [current_node_id]
        while current_node_id != get_osmID(start[0], start[1]):
            current_node_id = came_from[current_node_id]
            astar_path.append(current_node_id)
        astar_path.reverse()

        for node_id in astar_path:
            coordinate = get_lat_lon(node_id)
            path += f"{coordinate[0]},{coordinate[1]}|"
        path = path[:-1]
    return path    