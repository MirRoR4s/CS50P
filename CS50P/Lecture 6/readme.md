# [Lecture 6](https://cs50.harvard.edu/python/2022/notes/6/#lecture-6)


## [File I/O](https://cs50.harvard.edu/python/2022/notes/6/#file-io)

**问**：文件io是什么？
**答**：程序的一种能力，可以将文件作为输入或是输出。

**问**：文件io有什么作用？
答：可以保存程序接收的信息

比如利用文件io保存下述代码的 names 列表中的信息：
```python
names = []

for _ in range(3):
    names.append(input("What's your name?" ))

for name in sorted(names):
    print(f"hello, {name}")
```

## open
问：open 是什么？
答：open是python的一个内置函数，允许我们打开文件并在程序中使用它。具体地说在通过open打开文件之后就可以对文件进行读写操作。

1. 问：怎样在程序中使用文件io操作？
答：具体如下代码所示：
```python
name = input("What's your name? ")

file = open("names.txt", "w")
file.write(name)
file.close()
```
上述代码利用open以写启用模式打开了一个名为names.txt的文件，之后调用write方法向文件中写入了name，最后的close则是关闭已打开的文件。

2. 问：多次执行代码发现每次写入的内容都会覆盖之前写入的内容，如果我们想要在原内容的基础之上追加内容该怎么办？
**答：** 具体如下代码所示:
```python
name = input("What's your name? ")

file = open("names.txt", "a")
file.write(name)
file.close()
```
只需要将open函数的第二个参数由w变为a即可，a表示append。

**3. 问：** 继续执行上述代码多次，发现追加的名字之间没有分隔符，如何解决这个问题？
**答：** 在调用write函数写入时再额外写入一个换行或是其他作为分隔符的字符即可，比如：
```python
name = input("What's your name? ")

file = open("names.txt", "a")
file.write(f"{name}\n")
file.close()
```

- 关于open函数的更多信息，参看[open](https://docs.python.org/3/library/functions.html#open)文档。

## with
问：打开文件的时候总是容易忘记关闭文件，有什么办法可以帮助我们自动关闭文件吗？
答：利用with关键字即可。具体如下代码所示：
```python
name = input("What's your name?")

with open("names.txt", "a") as file:
	file.write(f"{name}\n")
```

问：前面讲了如何写入文件，那么又如何读取文件呢？
答：如下代码所示：
```python
with open("names.txt", "r") as file:
	lines = file.readlines()
for line in lines:
	print("hello", line)
```
- 上述代码 readlines 获得了 names.txt 的全部行并将其存储在了 lines 文件中。

问：运行上述代码发现输出十分凌乱，有很多多余的换行，如何解决这个问题？
答：可以利用 rstrip 方法删除末尾无关的换行符，具体如下：
```python
with open("names.txt", "r") as file:
    lines = file.readlines()

for line in lines:
    print("hello,", line.rstrip())
```

## CVS
问：CVS是什么？
答：CVS表示的是comma separated values的缩写，直译就是用逗号分隔值。

先编写一个CVS文件作为后面学习的例子：
```text
Hermoine,Gryffindor
Harry,Gryffindor
Ron,Gryffindor
Draco,Slytherin
```

现在编写如下代码：
```python
with open("students.csv") as file:
    for line in file:
        row = line.rstrip().split(",")
        print(f"{row[0]} is in {row[1]}")
```
- split 告诉编译器以逗号作为分隔符去分隔每一行的cvs值。

可以进一步简化代码如下：
```python
with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        print(f"{name} is in {house}")
```
- split 会返回两个值，一个是逗号前面的值，一个是逗号后面的值。

继续修改代码将name和house作为键值放入一个字典中，然后将字典加入学生列表：
```python
students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {"name": name, "house": house}
        students.append(student)

for student in students:
    print(f"{student['name']} is in {student['house']}")
```

问：现在想要根据name对students进行排序，但是students的元素变成了字典类型，如何解决这个问题？
答：具体如下代码所示：
```python
students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        students.append({"name": name, "house": house})


def get_name(student):
    return student["name"]


for student in sorted(students, key=get_name):
    print(f"{student['name']} is in {student['house']}")
```
只需要在调用sorted函数时告诉它如何寻找排序依据就可以了。sorted函数接收一个名为key的参数（函数类型）用于指明排序依据，在这里我们的排序依据是student的name，所以编写get_name函数返回name即可。

如果说只打算简单地使用一次get_name，那么还可以进一步地简化上述代码，具体如下：
```python
students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        students.append({"name": name, "house": house})

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is in {student['house']}")
```
- 此处不再显示地声明一个函数，而是直接给key参数传入一个匿名函数即lambda 函数，该函数的意思是告诉python当前有一个匿名函数，接收一个名为student的参数并返回student["name"]。

问：如果CSV文件变成了下面这样子，如何去处理？此时split用逗号作为分隔符肯定会出问题。
```python
Harry,"Number Four, Privet Drive"
Ron,The Burrow
Draco,Malfoy Manor
```

答：可以使用python内置的csv库来解决。
```python
import csv

students = []

with open("students.csv") as file:
    reader = csv.reader(file)
    for row in reader:
        students.append({"name": row[0], "home": row[1]})

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is from {student['home']}")
```
csv库有个reader对象可以用来读取cvs文件，不管csv的home部分是否含有逗号，都可以正常处理。
row是一个列表，里面包含着cvs的name和home。

目前是依靠程序自动识别csv哪一部分是name，哪一部分是home，不过可以在csv文件中显式地声明这一点：
```python
name,home
Harry,"Number Four, Privet Drive"
Ron,The Burrow
Draco,Malfoy Manor
```
首行name,home就指明了接下来的csv结构。

现在可以用 csv 库的 DictReader 来替代 reader，这能提供更大的灵活性。
```python
import csv

students = []

with open("students.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append({"name": row["name"], "home": row["home"]})

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is in {student['home']}")
```

问：如何写入一个csv文件？
答：具体如下：
```python
import csv

name = input("What's your name? ")
home = input("Where's your home? ")

with open("students.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({"name": name, "home": home})
```
利用cvs库的DictWriter方法。该方法接收两个参数，第一个参数是要写入的文件，第二个参数是要写入的csv的字段名。
之后调用 writerow 方法就可以写入了，注意要传入一个字典类型的参数。
