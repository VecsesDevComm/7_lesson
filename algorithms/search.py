def search(items, value):
    for item in items:
        if item == value:
            return item
    return None

# search_by_key(y2005, 'Country', 'HU')
def search_by_key(items, key, value):
    for item in items:
        if item[key] == value:
            return item
    return None

def binary_search(items, item):
    n = len(items)
    bal = 0
    jobb = n - 1
    
    while bal <= jobb:
        kozep = (bal + jobb) // 2
        
        if item > items[kozep]:
            bal = kozep + 1
        elif item < items[kozep]:
            jobb = kozep - 1
        else:
            return kozep
    
    return -1


def search_generic(items, x, comparator):
    for index, item in enumerate(items):
        if comparator(items, x) == 0:
            return index
    return -1


def binary_search_generic(items, item, comparator):
    n = len(items)
    bal = 0
    jobb = n - 1
    while bal <= jobb:
        kozep = (bal + jobb) // 2
        if item > items[kozep]:
            bal = kozep + 1
        elif item < items[kozep]:
            jobb = kozep - 1
        else:
            return kozep
    return -1