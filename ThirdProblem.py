# Сложность сортировки слиянием равна O(n * log(n)) во всех случаях, независимо от того, отсортирован он, или нет.
# Если длина массива равна 1, то он отсортирован, если нет, мы делим массив на две части,
# затем рекурсивно сортируются, а затем сливаются в готовый отсортированный массив.
def mergeSort(array):
    length = len(array)
    if length == 1:
        return array
    left = array[:(length // 2)]
    right = array[(length // 2):]
    left = mergeSort(left)
    right = mergeSort(right)
    i = 0
    j = 0
    newArray = []
    while i != len(left) and j != len(right):
        if left[i] < right[j]:
            newArray.append(left[i])
            i += 1
        else:
            newArray.append(right[j])
            j += 1
    while i != len(left):
        newArray.append(left[i])
        i += 1
    while j != len(right):
        newArray.append(right[j])
        j += 1
    return newArray
