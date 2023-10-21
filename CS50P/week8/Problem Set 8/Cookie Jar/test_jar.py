from jar import Jar
import pytest

def test_init():
    with pytest.raises(ValueError):
        assert(Jar(-1))
    jar = Jar(13)
    assert jar.capacity == 13
    
def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"

def test_deposit():
    # 容量默认是 12
    jar = Jar()
    with pytest.raises(ValueError):
        # 存放 13 块饼干超过了容量，所以抛出异常
        jar.deposit(13)
    # 存放不超过容量的饼干数
    jar.deposit(1)
    assert jar.cookie_number == 1
    
def test_withdraw():
    # 初始化一个容量为 12 的饼干，当前实际饼干数为 0.
    jar = Jar()
    
    # 非法取饼干
    with pytest.raises(ValueError):
        jar.withdraw(1)
    
    # 正常取饼干
    jar.deposit(1)
    jar.withdraw(1)
    assert jar.cookie_number == 0
    