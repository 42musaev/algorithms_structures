"""
name: sorting by selection
complexity: O(n * n)
"""

arr = [42, 23213, 12, 0, 4, 2, 1, 22, 4]


def find_small_element(arr: list) -> int:
    small_element = arr[0]
    small_element_index = 0

    for i in range(1, len(arr)):
        if arr[i] < small_element:
            small_element = arr[i]
            small_element_index = i
    return small_element_index


def select_in_sort(arr: list) -> list:
    new_list = []

    for i in range(len(arr)):
        small_element = find_small_element(arr)
        new_list.append(arr.pop(small_element))
    return new_list
