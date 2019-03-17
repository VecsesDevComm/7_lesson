from algorithms.data_structures import graph

def find_path(g, start, end, path = None):
    if path is None:
        path = []
    
    path = path + [start]
    if start == end:
        return path
    
    if start not in graph.get_nodes(g):
        return None
    
    for node in graph.get_nodes_from(g, start):
        if node not in path:
            new_path = find_path(g, node, end, path)
            if new_path:
                return new_path
    
    return None


def find_shortest_path(g, start, end, path = None):
    if path is None:
        path = []
    
    path = path + [start]
    if start == end:
        return path
    
    if start not in graph.get_nodes(g):
        return None
    
    shortest = None
    for node in graph.get_nodes_from(g, start):
        if node not in path:
            new_path = find_shortest_path(g, node, end, path)
            if new_path:
                if not shortest or len(new_path) < len(shortest):
                    shortest = new_path
    
    return shortest
