import re
import sys

def main():
    print(parse(input("HTML: ")))

def parse(s):
    pattern = r"\"https?://w{3}?\.?youtube\.com/embed/(.*)\""
    ans = re.search(pattern, s).groups()
    
    return ans[0] if ans is not None else None



if __name__ == "__main__":
    main()