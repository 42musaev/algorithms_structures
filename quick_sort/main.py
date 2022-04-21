# Algorithm: quick sort

# The complexity of the algorithm depends on the input data and in
# the best case will be O(n×2log2n).
# In the worst case O(n^2).
# There is also an average value, which is O(n×log2n).

array = [4, 12, 5, 2, 10, 7, 6, 3, 11, 9, 1, 0, 8]


def quick_sort(array: list) -> list:
    if len(array) < 2:
        return array
    pivot = array[0]
    left = [i for i in array[1:] if i <= pivot]
    right = [i for i in array[1:] if i > pivot]

    return quick_sort(left) + [pivot] + quick_sort(right)


l = quick_sort(array)
