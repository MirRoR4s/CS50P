import re
import sys

def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    """
    共有三种情况：
    1位数，0-9
    2位数，10-99
    3位数，100-255 = 100-199 200-249 250-255
    匹配这三种情况的任意一种就可以
    127.0.0.1
    255.255.255.255
    512.512.512.512
    """
    pattern = r"^((\d|\d{2}|1\d{2}|2[0-4]\d|25[0-5])\.){3}(\d|\d{2}|1\d{2}|2[0-4]\d|25[0-5])$"
    return False if re.search(pattern, ip) is None else True

if __name__ == "__main__":
    main()