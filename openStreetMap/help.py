import convertToGraphml as ctg

"""
<node id="6821312">
      <data key="d4">59.3064604</data>
      <data key="d5">14.4686764</data>
    </node>

line 27

all neighbours: 
6821302
288999779
2192637296
"""

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
    new_ids = []
    items = xmldoc.getElementsByTagName('edge')
    for edge in items:
        if(edge.getAttribute('source') == osmID):
            new_ids.append(edge.getAttribute('target'))
    return new_ids

def get_heuristic(current_node, destination_node):
    pass


id = "6821312"
print(get_neighbours(id))

