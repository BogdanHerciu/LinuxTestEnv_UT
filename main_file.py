import random

#################################
# # # # # # Main file # # # # # # 
#################################

def func_1():
	''' This function should return a random number between 9 and 28 '''
	return random.randint(9, 28)
def sum_of_two_integers(a,b):
	''' This function returns the sum of a and b'''
	return a+b

# Protect executable code with this block
if __name__ == "__main__":
    print(func_1())
    print(sum_of_two_integers(6, 8))






    