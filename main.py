from algorithms.data_structures import queue 
from algorithms.data_structures import stack
from algorithms.data_structures import graph

from algorithms.max import max
from algorithms.min import min
from algorithms.sum import sum
from algorithms.search import search
from algorithms.sort import bubble
from algorithms.paths import find_path, find_shortest_path

# Ebben a fájlban az órán vett algoritmusok és adatszerkezetekhez tartozó
# példa függvényeket találsz. Ezeket használhatod ötletelésre, és tanulásra
# Ha ki szeretnéd próbálni valamelyiket, akkor csak hívd meg a megfelelő függvényt
# és nézd meg mi az eredménye a print függvénnyel

def queue_teszt():
    q = []

    queue.betesz(q, 1)
    queue.betesz(q, 2)
    queue.betesz(q, 3)

    return [
        queue.kivesz(q),
        queue.kivesz(q),
        queue.kivesz(q)
    ]


def stack_teszt():
    s = []

    stack.betesz(s, 1)
    stack.betesz(s, 2)
    stack.betesz(s, 3)

    return [
        stack.kivesz(s),
        stack.kivesz(s),
        stack.kivesz(s)
    ]


def graph_teszt():
    gr = graph.create_graph(10)
    
    graph.add_node(gr, 1)
    graph.add_node(gr, 2)
    graph.add_node(gr, 3)
    graph.add_node(gr, 4)

    graph.add_arc(gr, 1, 3)
    graph.add_arc(gr, 3, 2)
    graph.add_arc(gr, 1, 2)
    graph.add_arc(gr, 3, 4)
    graph.add_arc(gr, 1, 4)

    return gr


def min_teszt():
    adatok = [3, 4, 1, 7, 1, -1, 10, 100, 3]
    return min(adatok)


def max_teszt():
    adatok = [3, 1, 5, 7, 10, 23, 4, -1, 33]
    return max(adatok)


def sum_teszt():
    adatok = [3, 1, 5, 7, 10, 23, 4, -1, 33]
    return sum(adatok)


# Keresés
def search_teszt():
    adatok = [2, 4, 1, 5, 6, 7, 10]
    return search(adatok, 1)


# Rendezés
def sort_teszt():
    adatok = [3, 1, 5, 1, 6, 10, 11, 12, 45, -1, 0, 3]
    return bubble(adatok)
