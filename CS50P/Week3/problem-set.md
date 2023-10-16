# [Problem Set 3](https://cs50.harvard.edu/python/2022/psets/3/)

## What to Do

1. Log into cs50.dev, which is a cloud-based version of Visual Studio Code (VS Code) that provides you with your very own “codespace” with everything that you need for the course pre-installed. No need to download and install VS Code or Python on your own Mac or PC!
Execute update50 in your codespace’s terminal window to ensure that your codespace is up-to-date; if prompted, click Rebuild now.
Submit all of the problems below:
Fuel Gauge
Felipe’s Taqueria
Grocery List
Outdated
When to Do It
By Wednesday, January 1, 2025 at 12:59 PM GMT+8.

## [Grocery List](https://cs50.harvard.edu/python/2022/psets/3/grocery/#grocery-list)

Suppose that you’re in the habit of making a list of items you need from the grocery store.

In a file called `grocery.py`, implement a program that prompts the user for items, one per line, until the user inputs control-d (which is a common way of ending one’s input to a program). Then output the user’s grocery list in all uppercase, sorted alphabetically by item, prefixing each line with the number of times the user inputted that item. No need to pluralize the items. Treat the user’s input case-insensitively.

**Hints**

- Note that you can detect when the user has inputted control-d by catching an [`EOFError`](https://docs.python.org/3/library/exceptions.html#EOFError) with code like:

```python
try:
    item = input()
except EOFError:
    ...
```

- Odds are you’ll want to store your grocery list as a `dict`.
- Note that a `dict` comes with quite a few methods, per [docs.python.org/3/library/stdtypes.html#mapping-types-dict](https://docs.python.org/3/library/stdtypes.html#mapping-types-dict), among them `get`, and supports operations like:

```python
d[key]
```

and

```python
if key in d:
    ...
```

wherein `d` is a `dict` and `key` is a `str`.

- Be sure to avoid or catch any [`KeyError`](https://docs.python.org/3/library/exceptions.html#KeyError).

### [Demo](https://cs50.harvard.edu/python/2022/psets/3/grocery/#demo)

### [Before You Begin](https://cs50.harvard.edu/python/2022/psets/3/grocery/#before-you-begin)

Log into [cs50.dev](https://cs50.dev/), click on your terminal window, and execute `cd` by itself. You should find that your terminal window’s prompt resembles the below:

```python
$
```

Next execute

```python
mkdir grocery
```

to make a folder called `grocery` in your codespace.

Then execute

```python
cd grocery
```

to change directories into that folder. You should now see your terminal prompt as `grocery/ $`. You can now execute

```python
code grocery.py
```

to make a file called `grocery.py` where you’ll write your program.

### [How to Test](https://cs50.harvard.edu/python/2022/psets/3/grocery/#how-to-test)

Here’s how to test your code manually:

- Run your program with `python grocery.py`. Type `mango` and press Enter, then type `strawberry` and press Enter, followed by control-d. Your program should output:

```python
1 MANGO
1 STRAWBERRY
```

- Run your program with `python grocery.py`. Type `milk` and press Enter, then type `milk` again and press Enter, followed by control-d. Your program should output:

```python
2 MILK
```

- Run your program with `python grocery.py`. Type `tortilla` and press Enter, then type `sweet potato` and press Enter, followed by control-d. Your program should output:

```python
1 SWEET POTATO
1 TORTILLA
```

You can execute the below to check your code using `check50`, a program that CS50 will use to test your code when you submit. But be sure to test it yourself as well!

```bash
check50 cs50/problems/2022/python/grocery
```

Green smilies mean your program has passed a test! Red frownies will indicate your program output something unexpected. Visit the URL that `check50` outputs to see the input `check50` handed to your program, what output it expected, and what output your program actually gave.

### [How to Submit](https://cs50.harvard.edu/python/2022/psets/3/grocery/#how-to-submit)

In your terminal, execute the below to submit your work.

```python
submit50 cs50/problems/2022/python/grocery
```

### 思路

- 定义一个字典，键是商品项的名称，值则是该商品项出现的次数。每一次用户输入一个商品项，如果字典里面没有该商品项就将其作为 key 加入字典，同时将该商品项出现的次数记为 1 并作为 value。如果字典里面已经有该商品项了，那么直接将相应的 value 加 1 即可。

```python
def main():
    item_table = {}

    while True:
        try:
            item = input().lower()
            tmp_item = item_table.get(item)

            if tmp_item is None:
                item_table.update({item: 1})
            else:
                item_table.update({item: tmp_item + 1})
        except EOFError:
            for key in sorted(item_table):
                print(f"{item_table[key]} {key.upper()}")
            break
main()
```
## [Outdated](https://cs50.harvard.edu/python/2022/psets/3/outdated/#outdated)

In the United States, dates are typically formatted in [month-day-year order](https://en.wikipedia.org/wiki/Date_and_time_notation_in_the_United_States) (MM/DD/YYYY), otherwise known as [middle-endian](https://en.wikipedia.org/wiki/Endianness#Middle-endian) order, which is arguably bad design. Dates in that format can’t be easily sorted because the date’s year comes last instead of first. Try sorting, for instance, `2/2/1800`, `3/3/1900`, and `1/1/2000` chronologically in any program (e.g., a spreadsheet). Dates in that format are also ambiguous. Harvard was [founded](https://www.harvard.edu/about/history/) on September 8, 1636, but 9/8/1636 could also be interpreted as August 9, 1636!

Fortunately, computers tend to use [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601), an international standard that prescribes that dates should be formatted in year-month-day (YYYY-MM-DD) order, no matter the country, formatting years with four digits, months with two digits, and days with two digits, “padding” each with leading zeroes as needed.

In a file called `outdated.py`, implement a program that prompts the user for a date, [anno Domini](https://en.wikipedia.org/wiki/Anno_Domini), in month-day-year order, formatted like `9/8/1636` or `September 8, 1636`, wherein the month in the latter might be any of the values in the `list` below:

```python
[
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
```

Then output that same date in `YYYY-MM-DD` format. If the user’s input is not a valid date in either format, prompt the user again. Assume that every month has no more than 31 days; no need to validate whether a month has 28, 29, 30, or 31 days.

**Hints**

- Recall that a `str` comes with quite a few methods, per [docs.python.org/3/library/stdtypes.html#string-methods](https://docs.python.org/3/library/stdtypes.html#string-methods), including `split`.
- Recall that a `list` comes with quite a few methods, per [docs.python.org/3/tutorial/datastructures.html#more-on-lists](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists), among which is `index`.
- Note that you can format an `int` with leading zeroes with code like

```python
    print(f"{n:02}")
```

wherein, if `n` is a single digit, it will be prefixed with one `0`, per [docs.python.org/3/library/string.html#format-string-syntax](https://docs.python.org/3/library/string.html#format-string-syntax).


### [Demo](https://cs50.harvard.edu/python/2022/psets/3/outdated/#demo)

### [Before You Begin](https://cs50.harvard.edu/python/2022/psets/3/outdated/#before-you-begin)

Log into [cs50.dev](https://cs50.dev/), click on your terminal window, and execute `cd` by itself. You should find that your terminal window’s prompt resembles the below:

```bash
$
```

Next execute

```bash
mkdir outdated
```

to make a folder called `outdated` in your codespace.

Then execute

```bash
cd outdated
```

to change directories into that folder. You should now see your terminal prompt as `outdated/ $`. You can now execute

```bash
code outdated.py
```

to make a file called `outdated.py` where you’ll write your program.

### [How to Test](https://cs50.harvard.edu/python/2022/psets/3/outdated/#how-to-test)

Here’s how to test your code manually:

- Run your program with `python outdated.py`. Type `9/8/1636` and press Enter. Your program should output:
    
```python
1636-09-08
```

- Run your program with `python outdated.py`. Type `September 8, 1636` and press Enter. Your program should output:

```python
1636-09-08
```

- Run your program with `python outdated.py`. Type `23/6/1912` and press Enter. Your program should reprompt the user.
- Run your program with `python outdated.py`. Type `December 80, 1980` and press Enter. Your program should reprompt the user.

You can execute the below to check your code using `check50`, a program that CS50 will use to test your code when you submit. But be sure to test it yourself as well!

```bash
check50 cs50/problems/2022/python/outdated
```

Green smilies mean your program has passed a test! Red frownies will indicate your program output something unexpected. Visit the URL that `check50` outputs to see the input `check50` handed to your program, what output it expected, and what output your program actually gave.

### [How to Submit](https://cs50.harvard.edu/python/2022/psets/3/outdated/#how-to-submit)

In your terminal, execute the below to submit your work.

```bash
submit50 cs50/problems/2022/python/outdated
```

### 思路

```python
def main():
    month_table = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
    while True:
        before_date = input("Date: ").strip()

        # xx/xx/xxxx
        if before_date[0].isdigit():
            try:
                m, d, y = before_date.split('/')
                m, d, y = int(m), int(d), int(y)
            except:
                pass
            else:
                if m < 1 or m > 12 or d > 31:
                    continue
                else:
                    print(f"{y}-{m:02}-{d:02}")
                    break
        # December 9, 1971
        else:
            try:
                m, d, y = before_date.split(' ')
                if ',' not in d:
                    continue
                month = month_table.index(m)
                if month == 0:
                    pass
                d = int(d.strip(','))
                y = int(y)
            except:
                pass
            else:
                if d > 31:
                    continue
                print(f"{y}-{month+1:02}-{d:02}")
                break
main() 
```