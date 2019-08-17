def rotated_array_search_recurrent(input_list, number, left=0):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    if len(input_list) == 0:
        return -1
    if len(input_list) == 1 and input_list[0] != number:
        return -1
    center = (len(input_list)-1) // 2

    if input_list[center] == number:
        return center + left

    # If index 0 to center of target array is sorted
    if input_list[0] <= input_list[center]:
        # If the array is sorted and the number is in the sorted array then search into this array
        if (number >= input_list[0]) and (number <= input_list[center]):
            return rotated_array_search_recurrent(input_list[:center], number, left)
        # Otherwise switch target array to not sorted array
        return rotated_array_search_recurrent(input_list[center+1:], number, left+center+1)

    # Otherwise index center+1 to end of target array is sorted
    # If the array is sorted and the number is in the sorted array then search into this array
    if (number >= input_list[center+1]) and (number <= input_list[-1]):
        return rotated_array_search_recurrent(input_list[center+1:], number, left+center+1)
    # Otherwise switch target array to not sorted array
    return rotated_array_search_recurrent(input_list[:center], number, left)


def rotated_array_search(input_list, number, left=0):
    lower = 0
    upper = len(input_list) - 1

    if len(input_list) == 0:
        return -1
    if len(input_list) == 1 and input_list[0] != number:
        return -1
    center = (lower + upper) // 2
    if input_list[center] == number:
        return center + left

    while lower <= upper:
        center = (upper + lower) // 2

        # If index 0 to center of target array is sorted
        if input_list[lower] <= input_list[center]:
            # If the array is sorted and the number is in the sorted array then search into this array
            if (number >= input_list[lower]) and (number <= input_list[center]):
                return input_list.index(number)
            # Otherwise switch target array to not sorted array
            else:
                lower = center + 1
        # Otherwise index center+1 to end of target array is sorted
        else:
            # If the array is sorted and the number is in the sorted array then search into this array
            if (number >= input_list[center + 1]) and (number <= input_list[upper]):
                return input_list.index(number)
            # Otherwise switch target array to not sorted array
            else:
                upper = center - 1
    return -1


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1


def test_function_recurrent(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search_recurrent(input_list, number):
        print("Pass")
    else:
        print("Fail")


def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")


test_function_recurrent([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function_recurrent([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function_recurrent([[6, 7, 8, 1, 2, 3, 4], 8])
test_function_recurrent([[6, 7, 8, 1, 2, 3, 4], 1])
test_function_recurrent([[6, 7, 8, 1, 2, 3, 4], 10])
test_function_recurrent([[6, 7, 8, 9, 10, 11, 1], 1])
test_function_recurrent([[1, 6, 7, 8, 9, 10, 11], 1])
test_function_recurrent([[], 10])

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
test_function([[6, 7, 8, 9, 10, 11, 1], 1])
test_function([[1, 6, 7, 8, 9, 10, 11], 1])
test_function([[], 10])


