def quick_sort(items):  
    cmp_count = 0
    if (len(items) <= 1):
        return cmp_count
    pivot = items[0]
    lower = []
    higher = []

    for i in range(1, len(items)):
        cmp_count += 1
        if items[i] < pivot:
            lower.append(items[i])
        else:
            higher.append(items[i])

    return quick_sort(lower) + cmp_count + quick_sort(higher)
