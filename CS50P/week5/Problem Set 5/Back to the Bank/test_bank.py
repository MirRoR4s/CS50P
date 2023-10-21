# cd && mkdir test_bank && cd test_bank && code bank.py && code test_bank.py
from bank import value


def test_normal0():
    assert value("hello") == 0

def test_normal1():
    assert value("hi") == 20

def test_normal3():
    assert value("zzzzz") == 100

def test_case_insensitively():
    assert value("HELLO") == 0
