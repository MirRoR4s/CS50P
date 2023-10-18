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

In a file called `scourgify.py`, implement a program that:

- Expects the user to provide two command-line arguments:
    - the name of an existing CSV file to read as input, whose columns are assumed to be, in order, `name` and `house`, and
    - the name of a new CSV to write as output, whose columns should be, in order, `first`, `last`, and `house`.
- Converts that input to that output, splitting each `name` into a `first` name and `last` name. Assume that each student will have both a first name and last name.

If the user does not provide exactly two command-line arguments, or if the first cannot be read, the program should exit via `sys.exit` with an error message.

同样的程序，但是在 windows 上输出的文件会多出一个空行，很奇怪。

```python
import sys
import csv


def main():
    table = []
    length = len(sys.argv)

    if length != 3:
	    sys.exit("Too few command-line arguments") if length < 3 else sys.exit("Too many command-line arguments")
    else:
        # 输入 csv 文件名
        file_name = sys.argv[1]
        # 输出 csv 文件名
        after_csv_file_name = sys.argv[2]
        # 输入文件的扩展名必须是 csv
        if file_name.endswith("csv") is not True:
            sys.exit("Not a CSV file")
        try:
             file = open(file_name, "r")
             reader = csv.DictReader(file)
        except FileNotFoundError:
            sys.exit("File don't exist")
        else:
            for row in reader:
                (last, first), house = row['name'].replace(" ", "").split(","), row['house']
                table.append({"first": first, "last": last, "house": house})
            with open(after_csv_file_name, "w", newline='') as file1:
	            writer = csv.DictWriter(file1, fieldnames=["first", "last", "house"])
	            writer.writeheader()
	            for row in table:
		            writer.writerow(row)
            file.close()

main()
```

很奇怪，总在提示生成的 csv 文件格式不正确。我后面又阅读一篇题目的上下文，发现是弄错了 first 和 last 的顺序。在 before.csv 中第一项是 last 而非 first。

### [CS50 P-Shirt](https://cs50.harvard.edu/python/2022/psets/6/shirt/)

Hints

-   Note that you can determine a file's extension with `os.path.splitext`, per [docs.python.org/3/library/os.path.html#os.path.splitext](https://docs.python.org/3/library/os.path.html#os.path.splitext).-   Note that `open` can `raise` a `FileNotFoundError`, per [docs.python.org/3/library/exceptions.html#FileNotFoundError](https://docs.python.org/3/library/exceptions.html#FileNotFoundError).-   Note that the `Pillow` package comes with quite a few classes and methods, per [pypi.org/project/Pillow](https://pypi.org/project/Pillow/). You might find its [handbook](https://pillow.readthedocs.io/en/stable/handbook/) and [reference](https://pillow.readthedocs.io/en/stable/reference/) helpful to skim. You can install the package with:
    ```
    pip install Pillow

    ```

    You can open an image (e.g., `shirt.png`) with code like:

    ```
    shirt = Image.open("shirt.png")

    ```

    You can get the width and height, respectively, of that image as a `tuple` with code like:

    ```
    size = shirt.size

    ```

    And you can overlay that image on top of another (e.g., `photo`) with code like

    ```
    photo.paste(shirt, shirt)

    ```

    wherein the first `shirt` represents the image to overlay and the second `shirt` represents a "mask" indicating which pixels in `photo` to update.

    -   Note that you can open an image (e.g., `shirt.png`) in VS Code by running
    ```
    code shirt.png

    ```

    or by double-clicking its icon in VS Code's file explorer.

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
- 为了可以正常检查此题，需要下载对应的图片资源

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
    # 输入图片名
    input_images = sys.argv[1]
    # 输出图片名
    output_images = sys.argv[2]
    # 获取输入图片的扩展名
    input_ext = os.path.splitext(input_images)[-1]
    # 获取输出图片的扩展名
    output_ext = os.path.splitext(output_images)[-1]
    # 输入输出扩展名必须相同
    if input_ext != output_ext:
        sys.exit("Input and output have different extensions")
    try:
        shirt = Image.open("shirt.png")
        input = Image.open(input_images)
    except FileNotFoundError:
        sys.exit("Invalid input")
    else:
        # 获取衬衣图片的大小
        shirt_size = shirt.size
        # 将输入图片裁剪到衬衣图片大小
        resize_input = ImageOps.fit(input, shirt_size)
        # 将衬衣图片复制到裁剪图片上
        resize_input.paste(shirt, shirt)
        # 保存复制结果图片
        resize_input.save(output_images)


if __name__ == "__main__":
    main()
```
