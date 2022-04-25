array = [i for i in range(1, 325)]


def binary_search(array: list, n: int):
    low = 0
    high = len(array) - 1

    while low <= high:
        mid = (low + high) // 2
        print(mid)

        if array[mid] == n:
            return mid
        if array[mid] > n:
            high = mid - 1
        elif array[mid] < n:
            low = mid + 1
    return None

# Complexity of the algorithm: O(log n)
