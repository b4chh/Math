def selection_sort(items):
    cmp_nb = 0
    min_pos = 0

    for i in range(0, len(items)):
        min_pos = i
        for x in range(i + 1, len(items)):
            if items[x] < items[min_pos]:
                min_pos = x
            cmp_nb += 1
        items[i], items[min_pos] = items[min_pos], items[i]
    return cmp_nb
