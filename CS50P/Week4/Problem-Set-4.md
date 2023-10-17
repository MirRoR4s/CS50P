

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