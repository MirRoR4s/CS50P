# [Lecture 5](https://cs50.harvard.edu/python/2022/notes/5/#lecture-5)

- [Unit Tests](https://cs50.harvard.edu/python/2022/notes/5/#unit-tests)
- [`assert`](https://cs50.harvard.edu/python/2022/notes/5/#assert)
- [`pytest`](https://cs50.harvard.edu/python/2022/notes/5/#pytest)
- [Testing Strings](https://cs50.harvard.edu/python/2022/notes/5/#testing-strings)
- [Organizing Tests into Folders](https://cs50.harvard.edu/python/2022/notes/5/#organizing-tests-into-folders)
- [Summing Up](https://cs50.harvard.edu/python/2022/notes/5/#summing-up)

## [Unit Tests](https://cs50.harvard.edu/python/2022/notes/5/#unit-tests)

- 编写代码测试程序是一件很常见的事情。
- 在 calculator.py 编辑如下代码：

    
    ```python
    def main():
        x = int(input("What's x? "))
        print("x squared is", square(x))
    
    
    def square(n):
        return n * n
    
    
    if __name__ == "__main__":
        main()
    ```
    
- 考虑为什么我们想要编写一个测试函数来验证上述 square 函数的正确性？
- 在 test_calculator.py 中编写如下的测试代码：
    
    ```python
    from calculator import square
    
    
    def main():
        test_square()
    
    
    def test_square():
        if square(2) != 4:
            print("2 squared was not 4")
        if square(3) != 9:
            print("3 squared was not 9")
    
    
    if __name__ == "__main__":
        main()
    ```
代码第一行导入 squre 函数，在 test_square 函数中编写了几个条件来测试 squre 函数的正确性。
- 根据惯例，一般将测试函数命名为 test_ + 被测函数名。
    
    
现在如果想要测试更多的条件，就要新增一个 if 语句，这样代码很快就会变得臃肿。有什么办法可以在不显著增加代码量的情况下扩展我们的测试能力吗？


## [`assert`](https://cs50.harvard.edu/python/2022/notes/5/#assert)

- assert 允许我们告诉编译器某些断言为真，这可以用在我们的测试代码test_square.py 中：
    
    ```python
    from calculator import square
    
    
    def main():
        test_square()
    
    
    def test_square():
        assert square(2) == 4
        assert square(3) == 9
    
    
    if __name__ == "__main__":
        main()
    ```
此处通过 assert 作出 square(2) 等于 4 和 square(3) 等于 9 的断言。利用 assert 代码的行数从 4 行变成了 2 行，减小了一部分代码量。
    
现在故意编写一个错误的 square 函数并进行测试：
    
```python
    def main():
        x = int(input("What's x? "))
        print("x squared is", square(x))
    
    
    def square(n):
        return n + n
    
    
    if __name__ == "__main__":
        main()
```
- 注意这里是将乘法符号换成了加法符号。

现在运行 test_square.py 编译器抛出了断言错误，告诉我们某个条件没有得到满足。
    
- Now running `python test_square.py` in the console window, you will notice that an `AssertionError` is raised by the compiler. Essentially, this is the compiler telling us that one of our conditions was not met.
- One of the challenges that we are now facing is that our code could become even more burdensome if we wanted to provide more descriptive error output to our users. Plausibly, we could code as follows:
    
```
    from calculator import square
    
    
    def main():
        test_square()
    
    
    def test_square():
        try:
            assert square(2) == 4
        except AssertionError:
            print("2 squared is not 4")
        try:
            assert square(3) == 9
        except AssertionError:
            print("3 squared is not 9")
        try:
            assert square(-2) == 4
        except AssertionError:
            print("-2 squared is not 4")
        try:
            assert square(-3) == 9
        except AssertionError:
            print("-3 squared is not 9")
        try:
            assert square(0) == 0
        except AssertionError:
            print("0 squared is not 0")
    
    
    if __name__ == "__main__":
        main()
```
    
    Notice that running this code will produce multiple errors. However, it’s not producing all the errors above. This is a good illustration that it’s worth testing multiple cases such that you might catch situations where there are coding mistakes.
    
- The above code illustrates a major challenge: How could we make it easier to test your code without dozens of lines of code like the above?

You can learn more in Python’s documentation of [`assert`](https://docs.python.org/3/reference/simple_stmts.html#assert).

## [`pytest`](https://cs50.harvard.edu/python/2022/notes/5/#pytest)

问：pytest 是什么？

答：pytest 是一个第三方库，允许对程序进行单元测试，即可以对程序内的函数进行测试。

问：如何才能使用 pytest？

答：终端键入 pip install pytest 即可安装使用 pytest。

问：怎样用 pytest 对程序进行单元测试？

答：以如下代码为例，在测试函数里利用 assert 进行断言即可。如果断言错误 pytest 就会告诉我们。


```python
from calculator import square
    
    
def test_assert():
    assert square(2) == 4
    assert square(3) == 9
    assert square(-2) == 4
    assert square(-3) == 9
    assert square(0) == 0
```
 
 问：当遇见第一个失败的测试 pytest 就会停下来，有什么好的解决办法？

 答：以如下代码为例：

    
```python
    def main():
        x = int(input("What's x? "))
        print("x squared is", square(x))
    
    
    def square(n):
        return n + n
    
    
    if __name__ == "__main__":
        main()
```
- 这里故意将乘法改成加法，人为制造错误方便测试。
    
解决的办法就是编写多个测试函数，将不同的测试条件分别进行测试。
    
```python
    from calculator import square
    
    
    def test_positive():
        assert square(2) == 4
        assert square(3) == 9
    
    
    def test_negative():
        assert square(-2) == 4
        assert square(-3) == 9
    
    
    def test_zero():
        assert square(0) == 0
```
现在 pytest 会对每个函数都进行测试，即使某个函数发生了错误也不影响其他函数的执行。
    
> 更多信息可以参看 [pytest](https://docs.pytest.org/en/7.1.x/getting-started.html) 的文档。



## [Organizing Tests into Folders](https://cs50.harvard.edu/python/2022/notes/5/#organizing-tests-into-folders)

问：如果我有多个测试文件，并将这些文件放在一个 test 文件夹里，怎样可以通过 pytest test 自动运行文件夹里的测试文件们呢？

答：在 test 文件夹编写一个 __init__.py 文件即可，内容即使为空也可以。具体的缘由和 python 的导入机制有关。具体参看此处-[导入机制](https://docs.pytest.org/en/7.1.x/explanation/pythonpath.html?highlight=folder#pytest-import-mechanisms-and-sys-path-pythonpath).

