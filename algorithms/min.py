def min(items):
    m = items[0]
    for item in items:
        if item < m:
            m = item
    return m


def min_generic(items, comparator):
    m = items[0]
    for item in items:
        if comparator(item, m) == -1:
            m = item
    return m
