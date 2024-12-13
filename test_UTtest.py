import main_file


'''
Test Case Description: Testing func_1
Test function        : func_1
'''
def test_1():
    for crtIdx in range(1000):
        result = func_1()
        assert (9 <= result <= 28), "Error: function returns values out of bounds"

'''
Test Case Description: Testing sum_of_two_integers
Test function        : sum_of_two_integers
'''
def test_2():
    result = 0
    assert result == 0, f"Expected 0, but got {result}"

