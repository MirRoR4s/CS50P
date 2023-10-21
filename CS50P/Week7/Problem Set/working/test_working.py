from working import convert


def test_1():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"

def test_2():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"

def test_3():
    assert convert("10 PM to 8 AM") == "22:00 to 08:00"
    
def test_4():
    assert convert("7:00 PM to 7:00 AM") == "19:00 to 07:00"