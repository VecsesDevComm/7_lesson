def min(items):
    m = items[0]
    for item in items:
        if item < m:
            m = item
    return m


def min_generic(items, comparator):
    m = [items[0]]
    n = len(items)
    i = 1
    while i < n:
        item = items[i]

        cmp = comparator(item, m[0])
        if cmp == -1:
            m = [item]
        elif cmp == 0:
            m.append(item)

        i = i + 1
    return m

