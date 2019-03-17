def create_graph(size):
    return { 'memory': [0] * size, 'gr': {} }


def add_node(graph, node):
    graph['memory'][node] = { 'data': node }
    graph['gr'][node] = []
    return graph


def add_arc(graph, start, end):
    if end not in graph['gr'][start]:
        graph['gr'][start].append(end)
    
    if start not in graph['gr'][end]:
        graph['gr'][end].append(start)
    
    return graph


def set_data(graph, node, data):
    if node not in graph['gr']:
        return None
    
    graph['memory'][node]['data'] = data


def get_nodes(graph):
    return graph['gr']


def get_nodes_from(graph, node):
    if not node in graph['gr']:
        return None
    return graph['gr'][node]
