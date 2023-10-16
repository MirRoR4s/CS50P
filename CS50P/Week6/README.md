# [Lecture 6](https://cs50.harvard.edu/python/2022/notes/6/#lecture-6)


## [File I/O](https://cs50.harvard.edu/python/2022/notes/6/#file-io)

#### 文件 io 
**问**：文件 io 是什么？

**答**：程序的一种能力，可以将文件作为输入或是输出。

---
#### 文件 io 作用

**问**：文件 io 有什么作用？

答：可以保存程序接收的信息

比如利用文件 io 保存下述代码 names 变量中的信息：

```python
names = []

for _ in range(3):
    names.append(input("What's your name?" ))

for name in sorted(names):
    print(f"hello, {name}")
```
---
## open
问：`open` 是什么？

答：open 是 python 的一个内置函数，用于打开文件并在程序中使用。具体地说在通过 open 打开文件之后就可以对文件进行读写操作。

---

#### 文件 io 的具体用法

答：具体如下代码所示：
```python
name = input("What's your name? ")
file = open("names.txt", "w")
file.write(name)
file.close()
```
上述代码以写启用模式（w）调用 open 打开了一个名为 names.txt 的文件，之后调用 write 方法向文件写入 name 变量的内容，最后的close 则是关闭已打开的文件。

---

#### 向文件追加写入

问：多次执行代码发现每次写入的内容都会覆盖之前写入的内容，如果我们想要在原内容的基础之上追加内容该怎么办？

**答**：具体如下代码所示:
```python
name = input("What's your name? ")

file = open("names.txt", "a")
file.write(name)
file.close()
```
只需要将 open 函数的第二个参数由 w 变为 a 即可，a 表示 **append。**

**问：** 继续执行上述代码多次，发现追加的 name 之间没有分隔符，如何解决这个问题？

**答：** 在调用 write 函数写入时再额外写入一个换行或是其他作为分隔符的字符即可，比如：
```python
name = input("What's your name? ")

file = open("names.txt", "a")
file.write(f"{name}\n")
file.close()
```

- 关于 open 函数的更多信息，参看 [open](https://docs.python.org/3/library/functions.html#open) 文档。

## with

#### 自动关闭已打开的文件
问：打开文件的时候总是容易忘记关闭文件，有什么办法可以帮助我们自动关闭文件吗？
答：利用with关键字即可。具体如下代码所示：
```python
name = input("What's your name?")

with open("names.txt", "a") as file:
	file.write(f"{name}\n")
```
#### 读取文件

问：前面讲了如何写入文件，那么又如何读取文件呢？
答：如下代码所示：
```python
with open("names.txt", "r") as file:
	lines = file.readlines()
for line in lines:
	print("hello", line)
```
- 上述代码 readlines 获得了 names.txt 的全部行并将其存储在了 lines 文件中。

#### 删除末尾无关换行符

问：运行上述代码发现输出十分凌乱，有很多多余的换行，如何解决这个问题？
答：可以利用 `rstrip` 方法删除末尾无关的换行符，具体如下：
```python
with open("names.txt", "r") as file:
    lines = file.readlines()

for line in lines:
    print("hello,", line.rstrip())
```

## CSV
问：`CSV` 是什么？

答：CSV 表示的是 `comma separated values` 的缩写，直译就是用逗号分隔的值。

如下是一个 CSV 文件的例子：

```python
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
- split 告诉编译器以逗号为分隔符分隔每一行的 cvs 值。

可以进一步简化代码如下：
```python
with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        print(f"{name} is in {house}")
```
- split 会返回两个值，一个是逗号前面的值，一个是逗号后面的值。

继续修改代码将 name 和 house 作为键值放入一个字典中，然后将字典加入 students 变量中：

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

#### 字典排序
问：现在想要根据 name 对 students 进行排序，但是 students 的元素变成了字典类型，如何解决这个问题？
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
只需要在调用 sorted 函数时告诉它如何寻找排序依据就可以了。sorted 函数接收一个名为 key 的参数（函数类型）用于指明排序依据，在这里我们的排序依据是 name，所以编写 `get_name` 函数返回name 即可。

如果说只打算简单地使用一次 `get_name`，那么还可以进一步地简化代码，具体如下：
```python
students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        students.append({"name": name, "house": house})

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is in {student['house']}")
```
- 此处不再显示地声明一个函数，而是直接给 key 参数传入一个匿名函数即 lambda 函数，该函数的意思是告诉 python 当前有一个匿名函数，接收一个名为 student 的参数并返回 student\["name"\]。

#### 利用 csv 库读取 csv 文件

如果 csv 值本身含有逗号该如何处理？此时无法简单地使用 split 进行分隔。
```python
Harry,"Number Four, Privet Drive"
Ron,The Burrow
Draco,Malfoy Manor
```

答：可以使用 python 内置的 csv 库来解决。

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
csv 库的 reader 对象可以用来读取 cvs 文件，不管 csv 的值是否含有逗号，都可以正常处理。
- row 是一个列表，里面包含着 csv 的 name 和 home。

目前是依靠程序自动识别 csv 哪一部分是 name，哪一部分是 home，但也可以在 csv 文件中显式地声明这一点：
```python
name,home
Harry,"Number Four, Privet Drive"
Ron,The Burrow
Draco,Malfoy Manor
```
首行的 name,home 就指明了接下来的 csv 结构。

可以用 csv 库的 `DictReader` 来替代 reader，这能提供更大的灵活性。
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

#### 如何利用 csv 库生成一个 csv 文件？
答：具体如下：
```python
import csv

name = input("What's your name? ")
home = input("Where's your home? ")

with open("students.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({"name": name, "home": home})
```
利用 csv 库的 DictWriter 方法。该方法接收两个参数，第一个参数是要写入的文件，第二个参数是 csv 的字段名。
之后调用 `writerow` 方法就可以写入了，注意要传入一个字典类型的参数。

## 二进制文件和PIL

问：gif 是什么？

答：一种图片类型，里面包含有很多个图片。这些图片会按序循环播放，这样就可以达到一种简单的视频效果。

问：如何把一些 gif 图片叠加起来形成一个新的 gif 图片？

答：利用 python PIL 库的 save 方法即可，具体代码如下：

```python
import sys

from PIL import Image

iamges = []

for arg in sys.argv[1:]:
    image = Image.open(arg)
    images.append(image)

images[0].save(
    "costumes.gif",
    save_all=True,
    append_images=[images[1]],  # see here 
    duration=200,
    loop=0
)
```
总结：

gif 不一定看起来是动态的，至少本节课给出的两个 gif 看起来是静态的。猜测是由于这两个 gif 中只含有一张图片，所以循环播放也看不出来什么变化。但是，但我们利用上述程序将两个 gif 叠加成一个新的 gif 后，就可以明显看出来新的 gif 是动态的了。

## 问题集

### [Lines of Code](https://cs50.harvard.edu/python/2022/psets/6/lines/)

问：程序的代码行数指什么？

答：指的是程序中排除注释和空行之外的总行数。

问：代码行数越多的程序就越复杂吗？

答：不一定，还要看代码的可读性怎么样。比如如下代码
```python
def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False
```
明显没有下面这个代码复杂，尽管第一个的行数是第二个的两倍以上。
```python
def is_even(n):
    return n % 2 == 0
```

问题描述：写一个程序识别 py 文件中所含的代码行数。不是 py 文件或文件不存在或未指明文件路径都要通过 `sys.exit` 退出！
  
- 可以假设注释都以 \# 开头，前面可能会有空格。
- 可以认为仅含空格的行则为空行。
- 补充：空行可能什么也没有，就只有一个换行？

```python
import sys


def main():
    length = len(sys.argv)

    if length == 1:
        sys.exit("Too few command-line arguments")
    elif length > 2:
        sys.exit("Too many command-line arguments")
    else:
        file_name = sys.argv[1]
        
        if file_name.endswith("py") is not True:
            sys.exit("Not a python file")
        
        line_number = 0
        
        try:
            with open(file_name, "r") as f:
                for line in f.readlines():
                    line = line.lstrip()
                    
                    if line.startswith("#") or is_blank(line):
                        continue
                    else:
                        line_number += 1
                        
            print(f"line number = {line_number}")

        except FileNotFoundError:
            sys.exit("File don't exist")


def is_blank(line):

    if len(line) == 0:
        return True

    for i in line:

        if i != ' ':
            return False

        return True


main()

```

### Pizza Py

**要求**：编写代码完成从 Pinocchio’s format 到 ASCII art  table formatted 的转换。

- 难度不大，注意仔细看 tabulate 库文档，有一些小的使用问题。

```python
import sys
from tabulate import tabulate
import csv

def main():
    table_list = []
    # headers1 = ["Sicilian Pizza", "Small", "Large"]
    # headers2 = ["Regular Pizza", "Small", "Large"]
    length = len(sys.argv)

    if length == 1:
        sys.exit("Too few command-line arguments")
    elif length > 2:
        sys.exit("Too many command-line arguments")
    else:
        file_name = sys.argv[1]
        
        if file_name.endswith("csv") is not True:
            sys.exit("Not a CSV file")
        
        try:
            with open(file_name, "r") as file:
                reader = csv.reader(file)
                for row in reader:
                    table_list.append(row)
            
            print(tabulate(table_list, headers="firstrow", tablefmt="grid"))
        
        except FileNotFoundError:
            sys.exit("File don't exist")

main()

```

### [Scourgify](https://cs50.harvard.edu/python/2022/psets/6/scourgify/#demo)

- 本题未通过测试


同样的程序，但是在 windows 上输出的文件会多出一个空行，很奇怪。
```python
import sys

import csv

def main():
    table = []
    length = len(sys.argv)

    if length < 2:
        sys.exit("Too few command-line arguments")
    elif length > 3:
        sys.exit("Too many command-line arguments")
    else:
        file_name = sys.argv[1]
        after_csv_file_name = sys.argv[2]
        if file_name.endswith("csv") is not True:
            sys.exit("Not a CSV file")
        
        try:
            with open(file_name, "r") as file:
                reader = csv.DictReader(file)
                
                for row in reader:
                    first, last= row['name'].split(',')
                    first, last = first.strip(), last.strip()
                    house = row['house']
                    table.append({"first": first, "last": last, "house": house})   
            
            with open(after_csv_file_name, "w") as file1:
                writer = csv.DictWriter(file1, fieldnames=["first", "last", "house"])
                writer.writeheader()
                for row in table:
                    writer.writerow(row)

        except FileNotFoundError:
            sys.exit("File don't exist")

main()
```
### [CS50 P-Shirt](https://cs50.harvard.edu/python/2022/psets/6/shirt/)

- 接收两个命令行参数，第一个是输入图片名，第二个是输出图片名。
- 用 `Image.open` 打开输入图片
- 用 `ImageOps.fit` 调整和裁剪输入图片的大小（和 `shirt.png` 一样大）
- 将 `shirt.png` 粘贴到调整后的图片中
- 用 `Image.save` 保存覆盖结果

不满足以下条件的，通过 `sys.exit` 退出：
- 两个命令行参数
- 输入和输出文件必须以 .jpg、.jpeg、.png 结尾，大小写不敏感
- 输入和输出文件的扩展名要相同
- 输入文件必须要存在

```python
import sys
from PIL import Image, ImageOps
import os


def main():
    length = len(sys.argv)

    if length < 3:
        sys.exit("Too few command-line arguments")
    elif length > 3:
        sys.exit("Too many command-line arguments")
    
    input_images = sys.argv[1]
    output_images = sys.argv[2]
    
    input_ext = os.path.splitext(input_images)[-1]
    output_ext = os.path.splitext(output_images)[-1]

    if input_ext != output_ext:
        sys.exit("Input and output have different extensions")

    try:
        shirt = Image.open("shirt.png")
        shirt_size = shirt.size
        input = Image.open(input_images)
        resize_input = ImageOps.fit(input, shirt_size)
        resize_input.paste(shirt, shirt)
        resize_input.save("test.png")
        
    except FileNotFoundError:
        sys.exit("Invalid input")



if __name__ == "__main__":
    main()

```
