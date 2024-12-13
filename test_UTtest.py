def add(a,b):
    return a+b

def UT_test_1_func_1():
    # Test if add(1, 2) returns 3
    result = add(1, 2)
    assert result == 3, f"Expected 3, but got {result}"

def UT_test_2_sum_of_two_integers():
    # Test if add(-1, 1) returns 0
    result = add(-1, 1)
    assert result == 0, f"Expected 0, but got {result}"