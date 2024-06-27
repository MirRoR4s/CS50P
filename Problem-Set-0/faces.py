"""
- 实现函数 convert，接收一个字符串并将字符串中的 `:)` 转为🙂、`:(` 转为 🙁，其余部分则保持不变。
- 实现函数 main，提示用户输入并将输入传递给 convert 函数，最后打印 convert 函数的结果。
"""

def main():
    user_input = input("Please input something, ")
    user_output = convert(user_input)
    print(user_output)


def convert(user_input):
    return user_input.replace(":(", "🙁").replace(":)", "🙂")

main()