import main_file

def test_1():
    '''
    Test Case Description: Testing func_1
    Test function        : func_1
    '''
    print("TC1: Begin")
    for crtIdx in range(1000):
        result = main_file.func_1()
        assert (9 <= result <= 28), "Error: function returns values out of bounds"
    print("End of Test Case 1")

def test_2():
    '''Test Case Description: Testing sum_of_two_integers
       Test function        : sum_of_two_integers
    '''
    print("TC2: Begin")
    result = main_file.sum_of_two_integers(5,6)
    assert result == 11, f"Expected 11, but got {result}"
    print("End of Test Case 2")
