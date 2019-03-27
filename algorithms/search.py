def search(items, x):
    for item in items:
        if item == x:
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
    for item in items:
        if item == x:
            return item
    return None


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