 
def add(a,b):
    return a+b

def test_1():
    # Test if add(1, 2) returns 3
    result = add(1, 2)
    assert result == 3, f"Expected 3, but got {result}"

def test_2():
    # Test if add(-1, 1) returns 0
    result = add(-1, 1)
    assert result == 0, f"Expected 0, but got {result}"

def test_3():
    # Test if add(0, 0) returns 0
    result = add(0, 0)
    assert result == 0, f"Expected 0, but got {result}"

def test_4():
    # Test if add(100, 200) returns 300
    result = add(100, 200)
    assert result == 300, f"Expected 300, but got {result}"