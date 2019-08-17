def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    lower = 0
    upper = number
    while lower <= upper:
        r1 = (upper + lower) // 2
        r2 = r1 + 1
        if r1**2 == number:
            return r1
        else:
            if (r1**2 < number) and (r2**2 > number):
                return r1
        if number < r1**2:
            upper = r1 - 1
        else:
            lower = r1 + 1
    return -1


print("Pass" if  (3 == sqrt(9)) else "Fail")
print("Pass" if  (0 == sqrt(0)) else "Fail")
print("Pass" if  (4 == sqrt(16)) else "Fail")
print("Pass" if  (1 == sqrt(1)) else "Fail")
print("Pass" if  (5 == sqrt(27)) else "Fail")