def max(items):
    m = items[0]
    n = len(items)
    i = 0
    while i < n:
        if items[i] > m:
            m = items[i]
        i = i + 1
    return m


def max_generic(items, comparator):
    m = items[0]
    n = len(items)
    i = 0
    while i < n:
        if comparator(items[i], m) == 1:
            m = items[i]
        i = i + 1
    return m
