# Средняя сложность быстрой сортировки равна O(n * log(n)),
# что быстрее сортировки слиянием, пузырькового метода и других популярных способов сортировки.
# Метод сортирует массивы любой величины.
def quicksort(arr):

    if len(arr) <= 1:

     return arr

    else:

        pivot = arr[0]

        left = [x for x in arr[1:] if x < pivot]

        right = [x for x in arr[1:] if x >= pivot]

        return quicksort(left) + [pivot] + quicksort(right)
