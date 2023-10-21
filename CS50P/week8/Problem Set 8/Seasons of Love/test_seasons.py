from seasons import convert
import pytest


def test_normal():
    assert convert("2003-10-20") == "Ten million, five hundred twenty thousand, six hundred forty minutes"
    
def test_exit_program_output(capfd):
    with pytest.raises(SystemExit):
        convert("February 6th, 1998")
    # out, err = capfd.readouterr()
    # assert out.strip() == "Invalid date"
