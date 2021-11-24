def merge(items, left, right):
    cmp = 0
    while left and right:
        if left[0] <= right[0]:
            items[cmp] = left[0]
            left.pop(0)
        else:
            items[cmp] = right[0]
            right.pop(0)
        cmp += 1
    if len(left) != 0:
        for i in range(cmp, len(items)):
            items[i] = left[0]
            left.pop(0)
    if len(right) != 0:
        for i in range(cmp, len(items)):
            items[i] = right[0]
            right.pop(0)
    return cmp



def merge_sort(items):
    count_cmp = 0
    res_sec_cmp = 0
    res_first_cmp = 0
    size = len(items)

    if size == 1:
        return count_cmp
    
    middle_idx = size // 2    
    first_half = items[:middle_idx]
    second_half = items[middle_idx:]
    res_first_cmp = merge_sort(first_half)
    res_sec_cmp = merge_sort(second_half)
    tmp = merge(items, first_half, second_half)

    return res_first_cmp + res_sec_cmp + count_cmp  + tmp