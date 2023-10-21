"""
将 YYYY-MM-DD 格式的日期转换成到目前的时间为止所过的分钟数
可能会遇见的一些问题：
1. 闰年会多一天，也就是多 1440 分钟，所以要判断有多少个闰年。
2. 如何获取当前的时间？
3. 需要计算当前的时间和用户输入的时间之间的差值，如何计算？
- 答案都在提示中！
cd && mkdir seasons && cd seasons && code seasons.py
code test_seasons.py
"""
import sys
from datetime import date
import inflect


def main():
    print(convert(input("Date of Birth: ")))


def convert(s):
    p = inflect.engine()
    # 获取今天的日期，格式如 2003-10-20
    today = date.today()
    try:
        user_date = date.fromisoformat(s)
    except:
        sys.exit("Invalid date")
    else:
        # 获取分钟数，格式如 123
        minutes = round((today - user_date).total_seconds()) // 60
        # 将数字形式的分钟数转为英文
        return f"{(p.number_to_words(minutes, andword='')).capitalize()} minutes"


if __name__ == "__main__":
    main()
