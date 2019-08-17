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
    sorted_list = sorted(input_list, reverse=True)
    item1 = ""
    item2 = ""
    for item in sorted_list:
        if len(item1) == 0 and len(item2) == 0:
            item1 += str(item)
        else:
            if len(item2) < len(item1):
                item2 += str(item)
            else:
                item1 += str(item)
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
