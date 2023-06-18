from collections import defaultdict
import convertToGraphml as ctg
import json

graphml_path = 'data/map.graphml'
xmldoc = ctg.parseXML(graphml_path)

def get_osmID(lat, lon):
    for node in xmldoc.getElementsByTagName('node'):
        data_elements = node.getElementsByTagName('data')
        if (data_elements[0].firstChild.data == str(lat)
            and data_elements[1].firstChild.data == str(lon)):
            return node.getAttribute('id')
    return None

def get_lat_lon(osmID):
    for node in xmldoc.getElementsByTagName('node'):
        if node.getAttribute('id') == str(osmID):
            data_elements = node.getElementsByTagName('data')
            lat = float(data_elements[0].firstChild.data)
            lon = float(data_elements[1].firstChild.data)
            return lat, lon
    return None

def get_neighbors(osmID):
    neighbor_info = defaultdict(list)  # initilized with an empty list.
    item = xmldoc.getElementsByTagName('edge')
    neighbor_edges = [edge for edge in item if edge.getAttribute('source') == osmID]

    for edge in neighbor_edges:
        neighbor = edge.getAttribute('target')
        data_elements = edge.getElementsByTagName('data')
        length = next(data.firstChild.data for data in data_elements if data.getAttribute('key') == 'd14')
        latlon_neighbor = get_lat_lon(neighbor)
        heuristic = get_heuristic(latlon_neighbor, destination_node=0)
        neighbor_info[osmID].append((neighbor, latlon_neighbor, length, heuristic))

    return neighbor_info

def get_heuristic(current_node, destination_node):
    return 0

id = "6821312"
my_dict = (get_neighbors(id))

#print(json.dumps(get_neighbors(id), indent=1))