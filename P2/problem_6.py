import math
def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    if len(ints) == 0:
        return (None, None)

    item_max = -math.inf
    item_min = math.inf

    for item in ints:
        if item > item_max:
            item_max = item
        if item < item_min:
            item_min = item
    return (item_min, item_max)


## Example Test Case of Ten Integers
import random
random.seed(0)

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")
print ("Pass" if ((None, None) == get_min_max([])) else "Fail")
print ("Pass" if ((0, 0) == get_min_max([0] * 10)) else "Fail")