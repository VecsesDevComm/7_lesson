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
    m = [items[0]]
    n = len(items)
    i = 1
    while i < n:
        cmp = comparator(items[i], m[0])
        if cmp == 1:
            m = [items[i]]
        elif cmp == 0:
            m.append(items[i])
        i = i + 1
    return m


def max_by_key(items, key):
    m = [items[0]]
    n = len(items)
    i = 1

    while i < n:
        if items[i][key] > m[0][key]:
            m = [items[i]]
        elif items[i][key] == m[0][key]:
            m.append(items[i])
        
        i = i + 1

    return m
