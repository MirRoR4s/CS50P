面向对象编程鼓励我们把类的所有功能都定义在类中。在这个过程中，如果我们定义的代码出错了，或是用户从外部传入了错误的参数应该怎么办？比如用户实例化 Student 时没有传入 name。解决代码如下：
```python
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
在上述代码中，调用构造函数时检查是否提供了 name，以及 house 是否是一个有效的值。我们利用 **raise** 抛出了 ValueError 异常并打印了特定的错误消息。

python 允许我们编写特殊的函数来打印出类对象的属性，具体代码如下：

```python
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
注意，通过实现上述的 `__str__` 方法，我们就可以利用 print 打印一个对象。更具体地说，是打印这个对象的属性，或者是你期望的和该对象相关联的东西，具体取决于你对 `__str__` 方法的实现。

- `__str__` 是 python 类的内置方法

```python
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

不同于字典，类中含有一些函数，我们称之为方法。以上代码中我们实现了一个 `charm` 方法，该方法对于不同的 patronus 会返回不同的结果。同时也注意到 python 有直接处理 emojis 的能力！
![[Pasted image 20231010193419.png]]
