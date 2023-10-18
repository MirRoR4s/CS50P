import re
import sys

def main():
    print(parse(input("HTML: ")))

def parse(s):
    """
    <iframe src="http://www.youtube.com/embed/xvFZjo5PgG0"></iframe>

    """
    pattern = r"\"https?://(w{3})?\.?youtube\.com/embed/(.*?)\""
    ans = re.search(pattern, s)
    
    return f"https://youtu.be/{ans.groups()[1]}" if ans is not None else None



if __name__ == "__main__":
    main()