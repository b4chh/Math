
def insertion_sort(array):
    size_array = len(array)
    count_cmp = 0

    for i in range(1, size_array):
        for x in range(0, i):
            count_cmp += 1
            if array[i] < array[x]:
                array.insert(x, array[i])
                array.pop(i + 1)
                break
    return count_cmp