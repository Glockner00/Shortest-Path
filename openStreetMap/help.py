import convertToGraphml as ctg

graphml_path = 'data/map.graphml'
xmldoc = ctg.parseXML(graphml_path)

def get_osmID(lat, lon):
    items = xmldoc.getElementsByTagName('node')
    for node in items:
        data_elements = node.getElementsByTagName('data')
        if(data_elements[0].firstChild.data == str(lat) and data_elements[1].firstChild.data == str(lon)):
            return node.getAttribute('id')
    return None

def get_lat_lon(osmID): 
    list = []
    items = xmldoc.getElementsByTagName('node')
    for node in items:
        if(str(node.getAttribute('id')) == str(osmID)):
            data_elements = node.getElementsByTagName('data')
            list.append(float(data_elements[0].firstChild.data))
            list.append(float(data_elements[1].firstChild.data))
            return list
    return None

def get_neighbours(osmID):
    pass

def get_heuristic(current_node, destination_node):
    pass


id = get_osmID(59.3067734,14.4666375)
print(id)
lat_lon = get_lat_lon(id)
print(lat_lon)