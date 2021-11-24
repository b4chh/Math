

def bubble_sort(items):
    nb_cmp = 0
    n_items = len(items)

    for i in range(n_items):
        for j in range(n_items - i - 1):
            if items[i] > items[j]:
                items[i], items[j] = items[j], items[i]
            nb_cmp += 1
    return nb_cmp
