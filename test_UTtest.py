def add(a,b):
    return a+b

def UT_test_1_func_1():
    result = add(1, 2)
    assert result == 3, f"Expected 3, but got {result}"
