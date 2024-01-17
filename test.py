import loops

def assert_equals(expected, result):
    """
    Returns 0 if the 'result' is what we 'expected' (if they are equal) and 1 otherwise
    If they are not equal, prints an error message
    """
    if expected == result:
        return 0
    print(f'>>> Test failed: expected {expected} but instead got result {result}')
    return 1

def test_sum_evens():
    """
    Ruturns the number of tests failed while testing sum_evens
    """
    failures = 0
    result = loops.sum_evens([1, 2, 3, 4])
    expected = 6
    result = loops.sum_evens([1, 4, 3, 4])
    expected = 8
    result = loops.sum_evens([-1, -2, 3, 4])
    expected = 2
    failures += assert_equals(expected, result)

    return failures
    
def test():
    """
    Runs all the tests in this file and prints which failed (if any)
    """
    total_failures = 0
    print('Testing sum_even')
    failures = test_sum_evens()
    total_failures += failures
    print(f'{failures} tests failed')
    print(f'Testing finished, {total_failures} tests failed in total')

if __name__ == "__main__":
    test()