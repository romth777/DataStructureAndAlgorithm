def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    if len(input_list) == 0:
        return []
    elif len(input_list) == 1:
        return [input_list[0]]

    item1 = ""
    item2 = ""
    max_index = max(input_list)
    min_index = min(input_list)
    for i in range(max_index, min_index - 1, -1):
        if i in input_list:
            if len(item1) == 0 and len(item2) == 0:
                item1 += str(i)
            else:
                if len(item2) < len(item1):
                    item2 += str(i)
                else:
                    item1 += str(i)
    return [int(item1), int(item2)]


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


test_function([[1, 2, 3, 4, 5], [542, 31]])
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])
test_function([[], []])
test_function([[0], [0]])
test_function([[0, 6, 2, 5, 9, 8], [962, 850]])
