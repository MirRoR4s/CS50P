# cd && mkdir test_fuel && cd test_fuel && code test_fuel.py && code fuel.py
import pytest
from fuel import convert, gauge

def test_int():
    with pytest.raises(ValueError):
        assert convert("a/b")
        assert convert("a/1")
        assert convert("1/a")
        assert convert("1.5/b")

def test_value():
    with pytest.raises(ValueError):
        assert convert("5/4")

def test_zero():
    with pytest.raises(ZeroDivisionError):
        assert convert("1/0")

def test_normal():
    assert convert("1/4") == 25

def test_E():
    assert gauge(0.5) == "E"
    assert gauge(1) == "E"

def test_F():
    assert gauge(99) == "F"
    assert gauge(100) == "F"

def test_Z():
    assert gauge(75) == '75%'
