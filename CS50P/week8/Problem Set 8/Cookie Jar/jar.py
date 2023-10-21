# cd & mkdir jar && cd jar && code jar.py && code test_jar.py
class Jar:
    """
    注意 capacity 被定义成了 Jar 类的 Property，所以我给类的 capacity 属性加上了下划线。
    """
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError
        self._capacity = capacity
        self.cookie_number = 0

    def __str__(self):
        return self.cookie_number * '🍪'

    def deposit(self, n):
        if self.cookie_number + n > self.capacity:
            raise ValueError
        self.cookie_number += n

    def withdraw(self, n):
        if n > self.cookie_number:
            raise ValueError
        self.cookie_number -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self.cookie_number

def main():
    jar = Jar(capacity=12)
    
if __name__ == "__main__":
    main()