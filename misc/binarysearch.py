def binary_search(array, target):
    '''Write a function that implements the binary search algorithm using iteration

    args:
      array: a sorted array of items of the same type
      target: the element you're searching for

    returns:
      int: the index of the target, if found, in the source
      -1: if the target is not found
    '''
    lower = 0
    upper = len(array) - 1
    while lower <= upper:
        i = (upper + lower) // 2
        if array[i] == target:
            return i
        else:
            if target < array[i]:
                upper = i - 1
            else:
                lower = i + 1
    return -1


def binary_search_recursive(array, target, start_index, end_index):
    '''Write a function that implements the binary search algorithm using recursion

    args:
      array: a sorted array of items of the same type
      target: the element you're searching for

    returns:
      int: the index of the target, if found, in the source
      -1: if the target is not found
    '''
    if start_index > end_index:
        return -1

    mid_index = (start_index + end_index) // 2
    if mid_index >= len(array):
        return -1
    mid_element = array[mid_index]

    if target == mid_element:
        return mid_index
    elif target > mid_element:
        return binary_search_recursive(array, target, mid_index + 1, end_index)
    else:
        return binary_search_recursive(array, target, start_index, mid_index - 1)


if __name__ == "__main__":
    array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    target = 6
    print(binary_search(array, target))
    print(binary_search_recursive(array, target, 0, len(array)))
    target = 11
    print(binary_search(array, target))
    print(binary_search_recursive(array, target, 0, len(array)))

    array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    target = 4
    print(binary_search(array, target))
    print(binary_search_recursive(array, target, 0, len(array)))
