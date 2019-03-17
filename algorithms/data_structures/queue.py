# FIFO

def betesz(lista, elem):
    lista.append(elem)


def kivesz(lista):
    if len(lista) == 0:
        return None
    
    elem = lista.pop(0)
    return elem
