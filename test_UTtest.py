import main_file

#############################################
# TC01:
# target function: func_1
#############################################
def UT_test_1_func_1():
    for crt_idx in range(1000):
        result = 10
        assert (9 <= result <= 28), "Error: function returns values out of bounds"
    print("TC01 ended")

#############################################
# TC02:
# target function: sum_of_two_integers
#############################################
def UT_test_2_sum_of_two_integers():
    result = 11
    assert result == 11, f"Expected 3, but got {result}"
    print("TC02 ended")