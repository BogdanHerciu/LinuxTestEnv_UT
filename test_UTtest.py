 
def add(a,b):
    return a+b

def test_1():
    result = add(1, 2)
    assert result == 3, f"Expected 3, but got {result}"

def test_2():
    result = add(-1, 1)
    assert result == 0, f"Expected 0, but got {result}"

