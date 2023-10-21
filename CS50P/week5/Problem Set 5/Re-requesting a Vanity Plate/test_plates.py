from plates import is_valid


def test_1():
    assert is_valid("CS50") == True

def test_2():
    assert is_valid("CS05") == False

def test_3():
    assert is_valid("CS50P") == False
    
def test_4():
    assert is_valid("PI3.14") == False

def test_5():
    assert is_valid("H") == False
    