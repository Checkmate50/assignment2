def sum_evens(lst):
    """
    Returns the sum of even integers in the given integer list `lst`
    Note that a negative number is even if its absolute value is even
    """
    result = 0
    for number in lst:
        if number % 2 == 0:
            result += number
    return result