import convertToGraphml as ctg
import math
import json

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
            # TODO implment herustic method
            heuristic = get_heuristic(latlon_neighbor, get_lat_lon(destination_node))
            tmp[neighbor] = [latlon_neighbor, length, heuristic]
            neighbor_list.append(tmp)

    neighbor_info[osmID] = neighbor_list
    return neighbor_info

def get_heuristic(current_node, destination_node):
    print(destination_node)
    x1,y1 = current_node
    x2,y2 = destination_node
    return (math.sqrt(((x2-x1)**2)+((y2-y1)**2)))

id = "6821312"
dest_id = "2571591346"
print(json.dumps(get_neighbors(id, dest_id), indent=1))