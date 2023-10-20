import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    """编写正则表达式，识别合法的时间格式。
    如果表达式未匹配上，则认为是非法的时间格式！（前提是表达式必须正确）
    9:00 AM to 5:00 PM
    9 AM to 5 PM
    匹配上之后也不一定就合法，还要判断数值范围。


    Args:
        s (_type_): _description_
    """
    pattern1 = r"^(([1-9]|1[0-2])\:([0-5]\d{1})) ([AP]M) to (([1-9]|1[0-2])\:([0-5]\d{1})) ([AP]M)$"
    pattern2 = r"^([1-9]|1[0-2]) ([AP]M) to ([1-9]|1[0-2]) ([AP]M)$"  # 10 PM to 8 AM
    ans = re.search(pattern1, s)
    if ans is not None:
        res = ans.groups() # ('9:00', '9', '00', 'AM', '5:00', '5', '00', 'PM')
        h1, m1 = res[0].split(':')
        h2, m2 = res[4].split(':')
        h1, h2 = int(h1), int(h2)
        h1 = convert_hour(res[3], h1)
        h2 = convert_hour(res[-1], h2)
        
        return f"{h1:02}:{m1} to {h2:02}:{m2}"
    ans1 = re.search(pattern2, s)

    if ans1 is not None:
        res = ans1.groups()  # ('10', 'PM', '8', 'AM')
        h1, h2 = int(res[0]), int(res[2])
        h1, h2 = convert_hour(res[1], h1), convert_hour(res[-1], h2) 

        return f"{h1:02}:00 to {h2:02}:00"

    raise ValueError

def convert_hour(meridiem, h):
    
    if meridiem == 'PM':
        h = (h + 12) % 24
        h += 12 if h == 0 else 0
    else:
        h = (h - 12) % 12
    return h
    

if __name__ == "__main__":
    main()