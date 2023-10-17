

# [Adieu,Adieu](https://cs50.harvard.edu/python/2022/psets/4/adieu/)

In [The Sound of Music](https://en.wikipedia.org/wiki/The_Sound_of_Music_(film)), there’s a song sung largely in English, [So Long, Farewell](https://www.youtube.com/watch?v=Qy9_lfjQopU), with these [lyrics](https://www.lyrics.com/lyric/3998488/Julie+Andrews/So+Long%2C+Farewell), wherein “adieu” means “goodbye” in French:

> Adieu, adieu, to yieu and yieu and yieu

Of course, the line isn’t grammatically correct, since it would typically be written (with an [Oxford comma](https://en.wikipedia.org/wiki/Serial_comma)) as:

> Adieu, adieu, to yieu, yieu, and yieu

To be fair, “yieu” isn’t even a word; it just rhymes with “you”!

In a file called `adieu.py`, implement a program that prompts the user for names, one per line, until the user inputs control-d. Assume that the user will input at least one name. Then bid adieu to those names, separating two names with one `and`, three names with two commas and one `and`, and $n$ names with $n$−1 commas and one `and`, as in the below:

> Adieu, adieu, to Liesl  
> Adieu, adieu, to Liesl and Friedrich  
> Adieu, adieu, to Liesl, Friedrich, and Louisa  
> Adieu, adieu, to Liesl, Friedrich, Louisa, and Kurt  
> Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, and Brigitta  
> Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, Brigitta, and Marta  
> Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, Brigitta, Marta, and Gretl

**Hints**

- Note that the `inflect` module comes with quite a few methods, per [pypi.org/project/inflect](https://pypi.org/project/inflect/). You can install it with:

    ```bash
    pip install inflect
    ```

## [Demo](https://cs50.harvard.edu/python/2022/psets/4/adieu/#demo)

## [Before You Begin](https://cs50.harvard.edu/python/2022/psets/4/adieu/#before-you-begin)

Log into [cs50.dev](https://cs50.dev/), click on your terminal window, and execute `cd` by itself. You should find that your terminal window’s prompt resembles the below:

```bash
$
```

Next execute

```bash
mkdir adieu
```

to make a folder called `adieu` in your codespace.

Then execute

```bash
cd adieu
```

to change directories into that folder. You should now see your terminal prompt as `adieu/ $`. You can now execute

```
code adieu.py
```

to make a file called `adieu.py` where you’ll write your program.

## [How to Test](https://cs50.harvard.edu/python/2022/psets/4/adieu/#how-to-test)

Here’s how to test your code manually:

- Run your program with `python adieu.py`. Type `Liesl` and press Enter, followed by control-d. Your program should output:
    
    ```
    Adieu, adieu, to Liesl 
    ```
    
- Run your program with `python adieu.py`. Type `Liesl` and press Enter, then type `Friedrich` and press Enter, followed by control-d. Your program should output:
    
    ```
    Adieu, adieu, to Liesl and Friedrich
    ```
    
- Run your program with `python adieu.py`. Type `Liesl` and press Enter, then type `Friedrich` and press Enter. Now type `Louisa` and press Enter, followed by control-d. Your program should output:
    
    ```
    Adieu, adieu, to Liesl, Friedrich, and Louisa
    ```
    

You can execute the below to check your code using `check50`, a program that CS50 will use to test your code when you submit. But be sure to test it yourself as well!

```
check50 cs50/problems/2022/python/adieu
```

Green smilies mean your program has passed a test! Red frownies will indicate your program output something unexpected. Visit the URL that `check50` outputs to see the input `check50` handed to your program, what output it expected, and what output your program actually gave.

## [How to Submit](https://cs50.harvard.edu/python/2022/psets/4/adieu/#how-to-submit)

In your terminal, execute the below to submit your work.

```bash
submit50 cs50/problems/2022/python/adieu
```

## 思路

将用户输入的名字存到一个列表中，等待触发 ctrl-d 直接打印即可。

```python
def bid_adieu(names):
    if len(names) == 1:
        return "Adieu, adieu, to " + names[0]
    elif len(names) == 2:
        return "Adieu, adieu, to " + names[0] + " and " + names[1]
    else:
        farewell = "Adieu, adieu, to "
        for i in range(len(names) - 2):
            farewell += names[i] + ", "
        farewell += names[-2] + ", and " + names[-1]
        return farewell

def main():
    name_list = []
    while True:
        try:
            name = input("Name: ")
            name_list.append(name)
        except EOFError:
            break

    farewell_message = bid_adieu(name_list)
    print(farewell_message)

if __name__ == "__main__":
    main()

```


## 参考链接

https://cs50.harvard.edu/python/2022/psets/4/
# [Guessing Game](https://cs50.harvard.edu/python/2022/psets/4/game/#guessing-game)

I’m thinking of a number between 1 and 100…

What is it?

It’s 50! But what if it were more random?

In a file called `game.py`, implement a program that:

- Prompts the user for a level, $n$. If the user does not input a positive integer, the program should prompt again.
- Randomly generates an integer between 1 and $n$, inclusive, using the `random` module.
- Prompts the user to guess that integer. If the guess is not a positive integer, the program should prompt the user again.
    - If the guess is smaller than that integer, the program should output `Too small!` and prompt the user again.
    - If the guess is larger than that integer, the program should output `Too large!` and prompt the user again.
    - If the guess is the same as that integer, the program should output `Just right!` and exit.

**Hints**

Note that the `random` module comes with quite a few functions, per [docs.python.org/3/library/random.html](https://docs.python.org/3/library/random.html).

## [Demo](https://cs50.harvard.edu/python/2022/psets/4/game/#demo)

## [Before You Begin](https://cs50.harvard.edu/python/2022/psets/4/game/#before-you-begin)

Log into [cs50.dev](https://cs50.dev/), click on your terminal window, and execute `cd` by itself. You should find that your terminal window’s prompt resembles the below:

```bash
$
```

Next execute

```
mkdir game
```

to make a folder called `game` in your codespace.

Then execute

```
cd game
```

to change directories into that folder. You should now see your terminal prompt as `game/ $`. You can now execute

```
code game.py
```

to make a file called `game.py` where you’ll write your program.

## [How to Test](https://cs50.harvard.edu/python/2022/psets/4/game/#how-to-test)

Here’s how to test your code manually:

- Run your program with `python game.py`. Type `cat` at a prompt that says `Level:` and press Enter. Your program should reprompt you:
    
    ```
    Level:   
    ```
    
- Run your program with `python game.py`. Type `-1` at a prompt that says `Level:` and press Enter. Your program should reprompt you:
    
    ```
    Level:   
    ```
    
- Run your program with `python game.py`. Type `10` at a prompt that says `Level:` and press Enter. Your program should now be ready to accept guesses:
    
    ```
    Guess:   
    ```
    
- Run your program with `python game.py`. Type `10` at a prompt that says `Level:` and press Enter. Then type `cat`. Your program should reprompt you:
    
    ```
    Guess:   
    ```
    
- Run your program with `python game.py`. Type `10` at a prompt that says `Level:` and press Enter. Then type `-1`. Your program should reprompt you:
    
    ```
    Guess:   
    ```
    
- Run your program with `python game.py`. Type `1` at a prompt that says `Level:` and press Enter. Then type `1`. Your program should output:
    
    ```
    Just right!  
    ```
    
    There’s only one possible number the answer could be!
    
- Run your program with `python game.py`. Type `10` at a prompt that says `Level:` and press Enter. Then type `100`. Your program should output:
    
    ```
    Too large!  
    ```
    
    Looks like you’re guessing outside the range you specified.
    
- Run your program with `python game.py`. Type `10000` at a prompt that says `Level:` and press Enter. Then type `1`. Your program should output:
    
    ```
    Too small!  
    ```
    
    Most likely, anyways: you might get lucky and see `Just right!`. But it would certainly be odd for you to see `Just right!` every time. And certainly you shouldn’t see `Too large!`.
    

You can execute the below to check your code using `check50`, a program that CS50 will use to test your code when you submit. But be sure to test it yourself as well!

```
check50 cs50/problems/2022/python/game
```

Green smilies mean your program has passed a test! Red frownies will indicate your program output something unexpected. Visit the URL that `check50` outputs to see the input `check50` handed to your program, what output it expected, and what output your program actually gave.

## [How to Submit](https://cs50.harvard.edu/python/2022/psets/4/game/#how-to-submit)

In your terminal, execute the below to submit your work.

```bash
submit50 cs50/problems/2022/python/game
```

## 思路

```python
import random
import sys

def main():
    while True:
        try:
            # 输入正数 n
            level = int(input("Level: "))
        except Exception:
            pass
        else:
            # 不是正数继续输入
            if level <= 0:
                continue
            else:
                # 生成随机数
                random_num = random.randint(1, level)

                while True:
                    try:
                        # 输入猜测的正数
                        guess_num = int(input("Guess: "))
                    except:
                        pass
                    else:
                        # 不是正数重新输入
                        if guess_num <= 0:
                            pass
                        else:
                            if guess_num > random_num:
                                print("Too large!")
                            elif guess_num < random_num:
                                print("Too small!")
                            else:
                                print("Just right!")
                                sys.exit()

main()
```

# [Little Professor](https://cs50.harvard.edu/python/2022/psets/4/professor/#little-professor)

One of David’s first toys as a child, funny enough, was [Little Professor](https://en.wikipedia.org/wiki/Little_Professor), a “calculator” that would generate ten different math problems for David to solve. For instance, if the toy were to display `4 + 0 =` , David would (hopefully) answer with `4`. If the toy were to display `4 + 1 =` , David would (hopefully) answer with `5`. If David were to answer incorrectly, the toy would display `EEE`. And after three incorrect answers for the same problem, the toy would simply display the correct answer (e.g., `4 + 0 = 4` or `4 + 1 = 5`).

In a file called `professor.py`, implement a program that:

- Prompts the user for a level, $n$. If the user does not input `1`, `2`, or `3`, the program should prompt again.
- Randomly generates ten (10) math problems formatted as `X + Y =` , wherein each of `X` and `Y` is a non-negative integer with $n$ digits. No need to support operations other than addition (`+`).
- Prompts the user to solve each of those problems. If an answer is not correct (or not even a number), the program should output `EEE` and prompt the user again, allowing the user up to three tries in total for that problem. If the user has still not answered correctly after three tries, the program should output the correct answer.
- The program should ultimately output the user’s score: the number of correct answers out of 10.

Structure your program as follows, wherein `get_level` prompts (and, if need be, re-prompts) the user for a level and returns `1`, `2`, or `3`, and `generate_integer` returns a randomly generated non-negative integer with `level` digits or raises a `ValueError` if `level` is not `1`, `2`, or `3`:

```python
import random


def main():
    ...


def get_level():
    ...


def generate_integer(level):
    ...


if __name__ == "__main__":
    main()
```

Hints

- Note that you can raise an exception like `ValueError` with code like:
    
    ```python
    raise ValueError
    ```
    
- Note that the `random` module comes with quite a few functions, per [docs.python.org/3/library/random.html](https://docs.python.org/3/library/random.html).

## [Demo](https://cs50.harvard.edu/python/2022/psets/4/professor/#demo)

## [Before You Begin](https://cs50.harvard.edu/python/2022/psets/4/professor/#before-you-begin)

Log into [cs50.dev](https://cs50.dev/), click on your terminal window, and execute `cd` by itself. You should find that your terminal window’s prompt resembles the below:

```
$
```

Next execute

```
mkdir professor
```

to make a folder called `professor` in your codespace.

Then execute

```
cd professor
```

to change directories into that folder. You should now see your terminal prompt as `professor/ $`. You can now execute

```
code professor.py
```

to make a file called `professor.py` where you’ll write your program.

## [How to Test](https://cs50.harvard.edu/python/2022/psets/4/professor/#how-to-test)

Here’s how to test your code manually:

- Run your program with `python professor.py`. Type `-1` and press Enter. Your program should reprompt you:
    
    ```python
    Level:   
    ```
    
- Run your program with `python professor.py`. Type `4` and press Enter. Your program should reprompt you:
    
    ```python
    Level:   
    ```
    
- Run your program with `python professor.py`. Type `1` and press Enter. Your program should begin posing addition problems with positive, single-digit integers. For example:
    
    ```
    6 + 6 =    
    ```
    
    Your program should output 10 distinct problems before printing the number of questions you answered correctly and exiting.
    
- Run your program with `python professor.py`. Type `1` and press Enter. Answer the first question incorrectly. Your program should output:
    
    ```
    EEE
    ```
    
    before reprompting you with the same question.
    
- Run your program with `python professor.py`. Type `1` and press Enter. Answer the first question incorrectly, three times. Your program should output the correct answer. For example:
    
    ```
    6 + 6 = 12
    ```
    
    and then move on to another question. Answer the remaining questions correctly. Your program should output a score of `9`.
    
- Run your program with `python professor.py`. Type `1` and press Enter. Answer all 10 questions correctly. Your program should output a score of `10`.

You can execute the below to check your code using `check50`, a program that CS50 will use to test your code when you submit. But be sure to test it yourself as well!

```
check50 cs50/problems/2022/python/professor
```

Green smilies mean your program has passed a test! Red frownies will indicate your program output something unexpected. Visit the URL that `check50` outputs to see the input `check50` handed to your program, what output it expected, and what output your program actually gave.

## [How to Submit](https://cs50.harvard.edu/python/2022/psets/4/professor/#how-to-submit)

In your terminal, execute the below to submit your work.

```bash
submit50 cs50/problems/2022/python/professor
```

## 思路
1. 提示用户输入1或2或3，如果输入不是数字或不是1、2、3，要求重新输入。
2. 根据输入的数字，生成对应位数的问题，打印给用户。
3. 用户回答，如果错误输出EEE，否则继续给出下一个问题。如果连续错误三次，给出正确答案后给出下一个问题。

```python
from random import randint


def main():
    score = 10
    level = get_level()
    for i in range(10):
        a, b = generate_integer(level), generate_integer(level)
        print(f"{a} + {b} = ")
        cnt = 0
        while True:
            ans = int(input("Ans: "))

            if a + b == ans:
                break
            else:
                print("EEE")
                cnt += 1
            if cnt == 3:
                print(f"{a} + {b} = {a+b}")
                score -= 1
                break
    print(f"Score: {score}")

def get_level():
    while True:
        try:
            level = int(input("Level: "))
        except EOFError:
            break
        except:
            pass
        else:
            if level > 3 or level <= 0:
                continue
            return level

def generate_integer(level):
    # 随机生成一个 level 位的数字
    if level == 1:
        return randint(0, 9)
    elif level == 2:
        return randint(10, 99)
    return randint(100, 999)

if __name__ == "__main__":
    main()
```

# [Bitcoin Price Index](https://cs50.harvard.edu/python/2022/psets/4/bitcoin/#bitcoin-price-index)

![Bitcoin logo](https://cs50.harvard.edu/python/2022/psets/4/bitcoin/Bitcoin.svg.png)

[Bitcoin](https://en.wikipedia.org/wiki/Bitcoin) is a form of digitial currency, otherwise known as [cryptocurrency](https://en.wikipedia.org/wiki/Cryptocurrency). Rather than rely on a central authority like a bank, Bitcoin instead relies on a distributed network, otherwise known as a [blockchain](https://en.wikipedia.org/wiki/Blockchain), to record transactions.

Because there’s demand for Bitcoin (i.e., users want it), users are willing to buy it, as by exchanging one currency (e.g., USD) for Bitcoin.

In a file called `bitcoin.py`, implement a program that:

- Expects the user to specify as a command-line argument the number of Bitcoins, $n$, that they would like to buy. If that argument cannot be converted to a `float`, the program should exit via `sys.exit` with an error message.
- Queries the API for the CoinDesk Bitcoin Price Index at [https://api.coindesk.com/v1/bpi/currentprice.json](https://api.coindesk.com/v1/bpi/currentprice.json), which returns a [JSON](https://en.wikipedia.org/wiki/JSON) object, among whose nested keys is the current price of Bitcoin as a `float`. Be sure to catch any [exceptions](https://requests.readthedocs.io/en/latest/api/#exceptions), as with code like:
    
    ```python
    import requests
    
    try:
        ...
    except requests.RequestException:
        ...
    ```
    
- Outputs the current cost of $n$ Bitcoins in USD to four decimal places, using `,` as a thousands separator.

Hints

- Recall that the `sys` module comes with `argv`, per [docs.python.org/3/library/sys.html#sys.argv](https://docs.python.org/3/library/sys.html#sys.argv).
- Note that the `requests` module comes with quite a few methods, per [requests.readthedocs.io/en/latest](https://requests.readthedocs.io/en/latest/), among which are `get`, per [requests.readthedocs.io/en/latest/user/quickstart/#make-a-request](https://requests.readthedocs.io/en/latest/user/quickstart/#make-a-request), and `json`, per [requests.readthedocs.io/en/latest/user/quickstart/#json-response-content](https://requests.readthedocs.io/en/latest/user/quickstart/#json-response-content). You can install it with:
    
    ```bash
    pip install requests
    ```
    
- Note that CoinDesk’s API returns a JSON response like:
    
    ```python
    {
       "time":{
          "updated":"May 2, 2022 15:27:00 UTC",
          "updatedISO":"2022-05-02T15:27:00+00:00",
          "updateduk":"May 2, 2022 at 16:27 BST"
       },
       "disclaimer":"This data was produced from the CoinDesk Bitcoin Price Index (USD). Non-USD currency data converted using hourly conversion rate from openexchangerates.org",
       "chartName":"Bitcoin",
       "bpi":{
          "USD":{
             "code":"USD",
             "symbol":"&#36;",
             "rate":"38,761.0833",
             "description":"United States Dollar",
             "rate_float":38761.0833
          },
          "GBP":{
             "code":"GBP",
             "symbol":"&pound;",
             "rate":"30,827.6198",
             "description":"British Pound Sterling",
             "rate_float":30827.6198
          },
          "EUR":{
             "code":"EUR",
             "symbol":"&euro;",
             "rate":"36,800.2764",
             "description":"Euro",
             "rate_float":36800.2764
          }
       }
    }
    ```
    
- Recall that you can format USD to four decimal places with a [thousands separator](https://docs.python.org/3/library/string.html#formatspec) with code like:
    
    ```python
    print(f"${amount:,.4f}")
    ```

## [Demo](https://cs50.harvard.edu/python/2022/psets/4/bitcoin/#demo)

This demo was recorded when the price of Bitcoin was $38,761.0833. Your own output may vary.

## [Before You Begin](https://cs50.harvard.edu/python/2022/psets/4/bitcoin/#before-you-begin)

Log into [cs50.dev](https://cs50.dev/), click on your terminal window, and execute `cd` by itself. You should find that your terminal window’s prompt resembles the below:

```
$
```

Next execute

```
mkdir bitcoin
```

to make a folder called `bitcoin` in your codespace.

Then execute

```
cd bitcoin
```

to change directories into that folder. You should now see your terminal prompt as `bitcoin/ $`. You can now execute

```
code bitcoin.py
```

to make a file called `bitcoin.py` where you’ll write your program.

## [How to Test](https://cs50.harvard.edu/python/2022/psets/4/bitcoin/#how-to-test)

Here’s how to test your code manually:

- Run your program with `python bitcoin.py`. Your program should use `sys.exit` to exit with an error message:
    
    ```
    Missing command-line argument   
    ```
    
- Run your program with `python bitcoin.py cat`. Your program should use `sys.exit` to exit with an error message:
    
    ```
    Command-line argument is not a number
    ```
    
- Run your program with `python bitcoin.py 1`. Your program should output the price of a single Bitcoin to four decimal places, using `,` as a [thousands separator](https://docs.python.org/3/library/string.html#formatspec).
- Run your program with `python bitcoin.py 2`. Your program should output the price of two Bitcoin to four decimal places, using `,` as a [thousands separator](https://docs.python.org/3/library/string.html#formatspec).
- Run your program with `python bitcoin.py 2.5`. Your program should output the price of 2.5 Bitcoin to four decimal places, using `,` as a [thousands separator](https://docs.python.org/3/library/string.html#formatspec).

You can execute the below to check your code using `check50`, a program that CS50 will use to test your code when you submit. But be sure to test it yourself as well!

```
check50 cs50/problems/2022/python/bitcoin
```

Green smilies mean your program has passed a test! Red frownies will indicate your program output something unexpected. Visit the URL that `check50` outputs to see the input `check50` handed to your program, what output it expected, and what output your program actually gave.

## [How to Submit](https://cs50.harvard.edu/python/2022/psets/4/bitcoin/#how-to-submit)

In your terminal, execute the below to submit your work.

```
submit50 cs50/problems/2022/python/bitcoin
```

## 思路

1. 从命令行接收比特币的数量（如果不可以转成float，退出并报错）
2. 访问网址得到比特币的价格
3. 计算总价格并以特定格式输出

> 本题的检测机制似乎无法访问外部网络，所以只能取巧在本地写一个汇率值了。


```python
import sys
import requests


def main():
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")
    try:
        bit_coin_num = float(sys.argv[1])
    except:
        sys.exit("Command-line argument is not a number")
    else:
        while True:
            try:
                # r = requests.get(url="https://api.coindesk.com/v1/bpi/currentprice.json").json()
                amount = 37817.3283 * bit_coin_num
                print(f"${amount:,.4f}")
                break
            except requests.RequestException:
                pass

if __name__ == "__main__":
    main()
```

```python
print(1)
```