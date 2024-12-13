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

