# [第8讲](https://cs50.harvard.edu/python/2022/notes/8/#lecture-8)

- [面向对象编程](https://cs50.harvard.edu/python/2022/notes/8/#object-oriented-programming)
- [课程](https://cs50.harvard.edu/python/2022/notes/8/#classes)
- [`raise`](https://cs50.harvard.edu/python/2022/notes/8/#raise)
- [装饰器](https://cs50.harvard.edu/python/2022/notes/8/#decorators)
- [连接到本课程之前的工作](https://cs50.harvard.edu/python/2022/notes/8/#connecting-to-previous-work-in-this-course)
- [类方法](https://cs50.harvard.edu/python/2022/notes/8/#class-methods)
- [静态方法](https://cs50.harvard.edu/python/2022/notes/8/#static-methods)
- [遗产](https://cs50.harvard.edu/python/2022/notes/8/#inheritance)
- [继承和例外](https://cs50.harvard.edu/python/2022/notes/8/#inheritance-and-exceptions)
- [运算符重载](https://cs50.harvard.edu/python/2022/notes/8/#operator-overloading)
- [加起来](https://cs50.harvard.edu/python/2022/notes/8/#summing-up)

## 面向对象编程

- 有很多不同的编程范式。当您学习其他语言时，您将开始识别类似的模式。
- 到目前为止，你已按部就班地完成了一系列的学习。
- 面向对象编程（OOP）是解决编程相关问题的一种引人注目的解决方案。
- 为了开始今天的课程，输入`code student.py`并在终端窗口中键入以下代码：

    ```python
    name = input("Name: ")
    house = input("House: ")
    print(f"{name} from {house}")
    ```
请注意，该程序遵循程序化、逐步的范例：与您在本课程的前面部分中看到的程序类似。

- 根据前几周的工作，我们可以创建函数来抽象出该程序的某些部分。
    ```python
    def main():
        name = get_name()
        house = get_house()
        print(f"{name} from {house}")
    
    
    def get_name():
        return input("Name: ")
    
    
    def get_house():
        return input("House: ")
    
    
    if __name__ == "__main__":
        main()
    ```
 
注意`get_name` 和 `get_house`是怎样抽象出我们 `main` 函数的一些需求。此外，请注意上面代码的最后几行告诉编译器如何运行该`main`函数。
 
- 我们可以通过将 `students` 以 `tuple` 类型存储来简化代码。 `tuple` 是一个值序列。与 `list` 不同的是， `tuple`不能被修改。在下面 `get_student()` 中我们返回两个值。
    ```python
    def main():
        name, house = get_student()
        print(f"{name} from {house}")
    
    
    def get_student():
        name = input("Name: ")
        house = input("House: ")
        return name, house
    
    
    if __name__ == "__main__":
        main()
    ```

    注意`get_student`返回`name, house`.

- 对 name 和 house 组成的 tuple 进行打包，以便我们能够将这两个变量返回到名为 `student` 的变量中。我们可以按如下方式修改我们的代码。
    ```python
    def main():
        student = get_student()
        print(f"{student[0]} from {student[1]}")
    
    
    def get_student():
        name = input("Name: ")
        house = input("House: ")
        return (name, house)
    
    
    if __name__ == "__main__":
        main()
    ```
    
    请注意，`(name, house)`明确告诉任何阅读我们代码的人我们正在返回一个 tuple 内的两个值。此外，请注意我们使用了`student[0]`、`student[1]`对 student 进行索引。
- `tuple`是不可变的，这意味着我们无法修改元组中的值。不变性是我们防御性编程的一种方式。
```python
    def main():
        student = get_student()
        if student[0] == "Padma":
            student[1] = "Ravenclaw"
        print(f"{student[0]} from {student[1]}")
    
    
    def get_student():
        name = input("Name: ")
        house = input("House: ")
        return name, house
    
    
    if __name__ == "__main__":
        main()
    ```

上述代码会产生错误。由于`tuple`是不可变的，所以无法重新分配`student[1]` 的值。
- 如果想为其他程序员提供灵活性，我们可以使用 `list`。具体如下所示：
```python
    def main():
        student = get_student()
        if student[0] == "Padma":
            student[1] = "Ravenclaw"
        print(f"{student[0]} from {student[1]}")
    
    
    def get_student():
        name = input("Name: ")
        house = input("House: ")
        return [name, house]
    
    
    if __name__ == "__main__":
        main()
    ```

请注意，列表是可变的。所以程序员可以对换 name 和 house 的顺序。在某些情况下，可能会决定使用此功能，以牺牲代码的安全性为代价提供更大的灵活性。毕竟，如果这些值的顺序是可变的，那么与您一起工作的程序员可能会在以后犯错误。

还可以利用字典实现上述的代码。回忆一下，字典能为我们提供键值对。
```python
    def main():
        student = get_student()
        print(f"{student['name']} from {student['house']}")
    
    
    def get_student():
        student = {}
        student["name"] = input("Name: ")
        student["house"] = input("House: ")
        return student
    
    
    if __name__ == "__main__":
        main()
    ```

请注意，在这种情况下，将返回两个键值对。这种方法的一个优点是我们可以使用键索引该字典。

尽管如此，还可以进一步改进我们的代码。注意到有一个不需要的变量。我们可以删除 `student = {}` 因为我们不需要创建一个空字典。

```python
    def main():
        student = get_student()
        print(f"{student['name']} from {student['house']}")
    
    
    def get_student():
        name = input("Name: ")
        house = input("House: ")
        return {"name": name, "house": house}
    
    
    if __name__ == "__main__":
        main()
    ```

请注意，我们可以在`return`语句中使用大括号来创建字典并在同一行中将其全部返回。

我们可以在代码的字典版本中提供 Padma 的特殊情况。

```python
    def main():
        student = get_student()
        if student["name"] == "Padma":
            student["house"] = "Ravenclaw"
        print(f"{student['name']} from {student['house']}")
    
    
    def get_student():
        name = input("Name: ")
        house = input("House: ")
        return {"name": name, "house": house}
    
    
    if __name__ == "__main__":
        main()
    ```

请注意，与我们之前对该代码的迭代类似，我们可以如何利用键名称来索引到我们的学生词典中。

## Classes

- 在面向对象编程中，通过类我们可以创建自己的数据类型，并为它们命名。
- 类就像数据类型的模具——我们可以在其中发明自己的数据类型并给它们命名。
- 我们可以如下修改代码来实现我们自己的类`Student`：

```python
    class Student:
        ...
    
    
    def main():
        student = get_student()
        print(f"{student.name} from {student.house}")
    
    
    def get_student():
        student = Student()
        student.name = input("Name: ")
        student.house = input("House: ")
        return student
    
    
    if __name__ == "__main__":
        main()
    ```

注意，按照惯例 `Student` 要大写。此外，注意 `...` 意味着我们稍后将返回来完成这部分代码。此外，请注意，在 中`get_student`，我们可以使用语法  `student = Student()` 来创建一个 Student 类的 student。此外，请注意，我们使用“点符号”来访问 Student 类的 student 属性。

每当您创建一个类并利用该蓝图来创建某些东西时，您就创建了所谓的“对象”或“实例”。在我们的代码中，`student`就是一个对象。

继续完善代码，这一次在类中定义两个属性，在后续创建类的实例时，也需要传入两个变量。
```python
    class Student:
        def __init__(self, name, house):
            self.name = name
            self.house = house
    
    
    def main():
        student = get_student()
        print(f"{student.name} from {student.house}")
    
    
    def get_student():
        name = input("Name: ")
        house = input("House: ")
        student = Student(name, house)
        return student
    
    
    if __name__ == "__main__":
        main()
    ```

请注意，在 `Student`，我们标准化了此类的属性。我们可以在 中创建一个`class Student`称为“方法”的函数，它确定类 的对象的行为`Student`。在此函数中，它接受`name`传递`house`给它的 和 并将这些变量分配给该对象。此外，请注意构造函数如何`student = Student(name, house)`在类中调用此函数`Student`并创建一个`student`. `self`指的是刚刚创建的当前对象。

- 我们可以将代码简化如下：
```python
    class Student:
        def __init__(self, name, house):
            self.name = name
            self.house = house
    
    
    def main():
        student = get_student()
        print(f"{student.name} from {student.house}")
    
    
    def get_student():
        name = input("Name: ")
        house = input("House: ")
        return Student(name, house)
    
    
    if __name__ == "__main__":
        main()
    ```
    
    请注意如何`return Student(name, house)`简化我们代码的先前迭代，其中构造函数语句在其自己的行上运行。
    
- 您可以在 Python 的[类](https://docs.python.org/3/tutorial/classes.html)文档中了解更多信息。

## [`raise`](https://cs50.harvard.edu/python/2022/notes/8/#raise)

- 面向对象的程序鼓励您将类的所有功能封装在类定义中。如果事情不顺利怎么办？如果有人尝试随机输入内容怎么办？如果有人试图创建一个没有名字的学生怎么办？修改您的代码如下：
    
    ```
    class Student:
        def __init__(self, name, house):
            if not name:
                raise ValueError("Missing name")
            if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
                raise ValueError("Invalid house")
            self.name = name
            self.house = house
    
    
    def main():
        student = get_student()
        print(f"{student.name} from {student.house}")
    
    
    def get_student():
        name = input("Name: ")
        house = input("House: ")
        return Student(name, house)
    
    
    if __name__ == "__main__":
        main()
    ```
    
    请注意我们现在如何检查是否提供了名称并指定了合适的房屋。事实证明，我们可以创建自己的异常，以提醒程序员注意由名为 的用户创建的潜在错误`raise`。在上面的例子中，我们提出了`ValueError`一条特定的错误消息。
    
- 碰巧的是，Python 允许您创建一个特定的函数，通过该函数可以打印对象的属性。修改您的代码如下：
    
    ```
    class Student:
        def __init__(self, name, house, patronus):
            if not name:
                raise ValueError("Missing name")
            if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
                raise ValueError("Invalid house")
            self.name = name
            self.house = house
            self.patronus = patronus
    
        def __str__(self):
            return f"{self.name} from {self.house}"
    
    
    def main():
        student = get_student()
        print(student)
    
    
    def get_student():
        name = input("Name: ")
        house = input("House: ")
        patronus = input("Patronus: ")
        return Student(name, house, patronus)
    
    
    if __name__ == "__main__":
        main()
    ```
    
    请注意如何`def __str__(self)`提供学生在被呼叫时返回的方法。因此，作为程序员，您现在可以打印对象、其属性或几乎任何您想要与该对象相关的内容。
    
- `__str__`是Python类附带的内置方法。碰巧我们也可以为类创建我们自己的方法！修改您的代码如下：
    
    ```
    class Student:
        def __init__(self, name, house, patronus=None):
            if not name:
                raise ValueError("Missing name")
            if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
                raise ValueError("Invalid house")
            if patronus and patronus not in ["Stag", "Otter", "Jack Russell terrier"]:
                raise ValueError("Invalid patronus")
            self.name = name
            self.house = house
            self.patronus = patronus
    
        def __str__(self):
            return f"{self.name} from {self.house}"
    
        def charm(self):
            match self.patronus:
                case "Stag":
                    return ""
                case "Otter":
                    return ""
                case "Jack Russell terrier":
                    return ""
                case _:
                    return ""
    
    
    def main():
        student = get_student()
        print("Expecto Patronum!")
        print(student.charm())
    
    
    def get_student():
        name = input("Name: ")
        house = input("House: ")
        patronus = input("Patronus: ") or None
        return Student(name, house, patronus)
    
    
    if __name__ == "__main__":
        main()
    ```
    
    注意我们如何定义我们自己的方法`charm`。与字典不同，类可以具有称为方法的内置函数。在这种情况下，我们定义我们的`charm`方法，其中特定情况有特定结果。此外，请注意 Python 能够直接在我们的代码中使用表情符号。
    
- 在继续之前，让我们删除我们的守护神代码。修改您的代码如下：
    
    ```
    class Student:
        def __init__(self, name, house):
            if not name:
                raise ValueError("Invalid name")
            if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
                raise ValueError("Invalid house")
            self.name = name
            self.house = house
    
        def __str__(self):
            return f"{self.name} from {self.house}"
    
    
    def main():
        student = get_student()
        student.house = "Number Four, Privet Drive"
        print(student)
    
    
    def get_student():
        name = input("Name: ")
        house = input("House: ")
        return Student(name, house)
    
    
    if __name__ == "__main__":
        main()
    ```
    
    请注意我们只有两个方法：`__init__`和`__str__`。
    

## [装饰器](https://cs50.harvard.edu/python/2022/notes/8/#decorators)

可以利用属性来加固代码，在 Python 中，通过使用装饰器函数来做到这一点。装饰器函数以 `@` 开头，具体代码如下：
```python
    class Student:
        def __init__(self, name, house):
            if not name:
                raise ValueError("Invalid name")
            self.name = name
            self.house = house
    
        def __str__(self):
            return f"{self.name} from {self.house}"
    
        # Getter for house
        @property
        def house(self):
            return self._house
    
        # Setter for house
        @house.setter
        def house(self, house):
            if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
                raise ValueError("Invalid house")
            self._house = house
    
    
    def main():
        student = get_student()
        print(student)
    
    
    def get_student():
        name = input("Name: ")
        house = input("House: ")
        return Student(name, house)
    
    
    if __name__ == "__main__":
        main()
    ```

- 除了房子的名称外，我们还可以保护学生的姓名。修改您的代码如下：
    
    ```
    class Student:
        def __init__(self, name, house):
            self.name = name
            self.house = house
    
        def __str__(self):
            return f"{self.name} from {self.house}"
    
        # Getter for name
        @property
        def name(self):
            return self._name
    
        # Setter for name
        @name.setter
        def name(self, name):
            if not name:
                raise ValueError("Invalid name")
            self._name = name
    
        @property
        def house(self):
            return self._house
    
        @house.setter
        def house(self, house):
            if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
                raise ValueError("Invalid house")
            self._house = house
    
    
    def main():
        student = get_student()
        print(student)
    
    
    def get_student():
        name = input("Name: ")
        house = input("House: ")
        return Student(name, house)
    
    
    if __name__ == "__main__":
        main()
    ```
    
    请注意，与前面的代码非常相似，我们为名称提供了 getter 和 setter。
    
- 您可以在 Python 的[方法](https://docs.python.org/3/tutorial/classes.html)文档中了解更多信息。

## [连接到本课程之前的工作](https://cs50.harvard.edu/python/2022/notes/8/#connecting-to-previous-work-in-this-course)

- 尽管在本课程的过去部分中没有明确说明，但您自始至终都在使用类和对象。
- 如果您深入研究 的文档`int`，您会发现它是一个带有构造函数的类。它是创建 类型对象的蓝图`int`。您可以在 Python 的 文档中了解更多信息[`int`](https://docs.python.org/3/library/functions.html#int)。
- 字符串也是一个类。如果您使用了`str.lower()`，则您正在使用类中的方法`str`。您可以在 Python 的 文档中了解更多信息[`str`](https://docs.python.org/3/library/stdtypes.html#str)。
- `list`也是一个类。查看 的文档`list`，您可以看到其中包含的方法，例如`list.append()`. 您可以在 Python 的 文档中了解更多信息[`list`](https://docs.python.org/3/library/stdtypes.html#list)。
- `dict`也是Python中的一个类。您可以在 Python 的 文档中了解更多信息[`dict`](https://docs.python.org/3/library/stdtypes.html#dict)。
- 要了解您一直以来如何使用类，请转到控制台并键入`code type.py`，然后编写如下代码：
    
    ```
    print(type(50))
    ```
    
    请注意，通过执行此代码，它将显示 的类`50`是`int`。
    
- 我们还可以将其应用到`str`以下方面：
    
    ```
    print(type("hello, world"))
    ```
    
    请注意执行此代码将如何表明它属于该类`str`。
    
- 我们还可以将其应用到`list`以下方面：
    
    ```
    print(type([]))
    ```
    
    请注意执行此代码将如何表明它属于该类`list`。
    
- 我们还可以将其应用于`list`使用 Python 内置`list`类的名称，如下所示：
    
    ```
    print(type(list()))
    ```
    
    请注意执行此代码将如何表明它属于该类`list`。
    
- 我们还可以将其应用到`dict`以下方面：
    
    ```
    print(type({}))
    ```
    
    请注意执行此代码将如何表明它属于该类`dict`。
    
- 我们还可以将其应用于`dict`使用 Python 内置类的名称，`dict`如下所示：
    
    ```
    print(type(dict()))
    ```
    
    请注意执行此代码将如何表明它属于该类`dict`。
    

## [类方法](https://cs50.harvard.edu/python/2022/notes/8/#class-methods)

- 有时，我们想向类本身添加功能，而不是向该类的实例添加功能。
- `@classmethod`是一个函数，我们可以使用它向整个类添加功能。
- _这是不_使用类方法的示例。在终端窗口中，键入`code hat.py`并编码如下：
    
    ```
    import random
    
    
    class Hat:
        def __init__(self):
            self.houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
    
        def sort(self, name):
            print(name, "is in", random.choice(self.houses))
    
    
    hat = Hat()
    hat.sort("Harry")
    ```
    
    请注意，当我们将学生的姓名传递给分院帽时，它会告诉我们哪个学院分配给了该学生。请注意，`hat = Hat()`实例化了一个`hat`. 功能始终由类的_实例_`sort`处理。通过执行，我们将学生的姓名传递给我们所调用的特定实例的方法。`Hat``hat.sort("Harry")``sort``Hat``hat`
    
- 不过，我们可能希望在不创建排序帽的特定实例的情况下运行该`sort`函数（毕竟只有一个！）。我们可以修改我们的代码如下：
    
    ```
    import random
    
    
    class Hat:
    
        houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
    
        @classmethod
        def sort(cls, name):
            print(name, "is in", random.choice(cls.houses))
    
    
    Hat.sort("Harry")
    ```
    
    请注意如何`__init__`删除该方法，因为我们不需要在代码中的任何位置实例化帽子。`self`因此，不再相关并被删除。我们将其指定`sort`为 a `@classmethod`，替换`self`为`cls`。最后，请注意`Hat`这段代码末尾附近如何按照约定大写，因为这是我们类的名称。
    
- 回到`students.py`我们可以修改我们的代码如下，解决一些与`@classmethod`s 相关的错过的机会：
    
    ```
    class Student:
        def __init__(self, name, house):
            self.name = name
            self.house = house
    
        def __str__(self):
            return f"{self.name} from {self.house}"
    
        @classmethod
        def get(cls):
            name = input("Name: ")
            house = input("House: ")
            return cls(name, house)
    
    
    def main():
        student = Student.get()
        print(student)
    
    
    if __name__ == "__main__":
        main()
    ```
    
    请注意，它`get_student`已被删除并创建了一个`@classmethod`调用。`get`现在无需先创建学生即可调用此方法。
    

## [静态方法](https://cs50.harvard.edu/python/2022/notes/8/#static-methods)

- 事实证明，除了`@classmethod`与实例方法不同的 s 之外，还有其他类型的方法。
- 使用`@staticmethod`可能是您可能希望探索的东西。虽然本课程没有明确介绍，但欢迎您去了解有关静态方法及其与类方法的区别的更多信息。

## [遗产](https://cs50.harvard.edu/python/2022/notes/8/#inheritance)

- 继承也许是面向对象编程最强大的功能。
- 碰巧您可以创建一个类，“继承”另一个类的方法、变量和属性。
- 在终端中，执行`code wizard.py`. 代码如下：
    
    ```
    class Wizard:
        def __init__(self, name):
            if not name:
                raise ValueError("Missing name")
            self.name = name
    
        ...
    
    
    class Student(Wizard):
        def __init__(self, name, house):
            super().__init__(name)
            self.house = house
    
        ...
    
    
    class Professor(Wizard):
        def __init__(self, name, subject):
            super().__init__(name)
            self.subject = subject
    
        ...
    
    
    wizard = Wizard("Albus")
    student = Student("Harry", "Gryffindor")
    professor = Professor("Severus", "Defense Against the Dark Arts")
    ...
    ```
    
    请注意，上面有一个名为 的类`Wizard`，还有一个名为 的类`Student`。此外，请注意有一个名为 的类`Professor`。学生和教授都有名字。而且，学生和教授都是巫师。因此， 和`Student`都`Professor`继承了 的特点`Wizard`。在“子”类中`Student`，`Student`可以继承“父”或“超”类`Wizard`作为行`super().__init__(name)`运行`init`的方法`Wizard`。最后，请注意此代码的最后几行创建了一个名为 Albus 的向导、一个名为 Harry 的学生，等等。
    

## [继承和例外](https://cs50.harvard.edu/python/2022/notes/8/#inheritance-and-exceptions)

- 虽然我们刚刚介绍了继承，但我们在使用异常的过程中一直在使用继承。
- 碰巧的是，例外情况出现在层次结构中，其中有子类、父类和祖父母类。如下图所示：
    
    ```
    BaseException
     +-- KeyboardInterrupt
     +-- Exception
          +-- ArithmeticError
          |    +-- ZeroDivisionError
          +-- AssertionError
          +-- AttributeError
          +-- EOFError
          +-- ImportError
          |    +-- ModuleNotFoundError
          +-- LookupError
          |    +-- KeyError
          +-- NameError
          +-- SyntaxError
          |    +-- IndentationError
          +-- ValueError
     ...
    ```
    
- 您可以在 Python 的[异常](https://docs.python.org/3/library/exceptions.html)文档中了解更多信息。

## [运算符重载](https://cs50.harvard.edu/python/2022/notes/8/#operator-overloading)

- 一些运算符（例如`+`和 ）`-`可以“重载”，这样它们就可以具有除简单算术之外的更多功能。
- 在终端窗口中，输入`code vault.py`。然后，代码如下：
    
    ```
    class Vault:
        def __init__(self, galleons=0, sickles=0, knuts=0):
            self.galleons = galleons
            self.sickles = sickles
            self.knuts = knuts
    
        def __str__(self):
            return f"{self.galleons} Galleons, {self.sickles} Sickles, {self.knuts} Knuts"
    
        def __add__(self, other):
            galleons = self.galleons + other.galleons
            sickles = self.sickles + other.sickles
            knuts = self.knuts + other.knuts
            return Vault(galleons, sickles, knuts)
    
    
    potter = Vault(100, 50, 25)
    print(potter)
    
    weasley = Vault(25, 50, 100)
    print(weasley)
    
    total = potter + weasley
    print(total)
    ```
    
    请注意该方法如何`__str__`返回格式化字符串。此外，请注意该方法如何`__add__`允许将两个保管库的值相加。`self`是操作数左边的内容`+`。`other`才是正确的`+`。
    
- [您可以在 Python 的运算符重载](https://docs.python.org/3/reference/datamodel.html#special-method-names)文档中了解更多信息。

## [加起来](https://cs50.harvard.edu/python/2022/notes/8/#summing-up)

现在，您已经通过面向对象编程学到了全新的能力水平。

- 面向对象编程
- 课程
- `raise`
- 类方法
- 静态方法
- 遗产
- 运算符重载