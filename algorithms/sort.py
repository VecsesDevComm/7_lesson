def bubble(items):
    n = len(items)
    i = n

    while i > 0:
        j = 0
        
        while j < i - 1:
            if items[j] > items[j + 1]:
                tmp = items[j]
                items[j] = items[j + 1]
                items[j + 1] = tmp
            j = j + 1
        
        i = i - 1
    
    return items


def bubble_generic(items, comparator):
    n = len(items)
    i = n

    while i > 0:
        j = 0
        
        while j < i - 1:
            if comparator(items[j], items[j + 1]) == 1:
                tmp = items[j]
                items[j] = items[j + 1]
                items[j + 1] = tmp
            j = j + 1
        
        i = i - 1
    
    return items
