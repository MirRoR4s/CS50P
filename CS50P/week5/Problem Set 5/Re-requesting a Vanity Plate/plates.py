# cd && mkdir test_plates && cd test_plates && code plates.py && code test_plates.py
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    ans1 =  s[:2].isalpha() and  2 <= len(s) <= 6 and s.isalnum()
    cnt = True
    ans2 = True

    for i in range(1, len(s)-1):
        if s[i].isdigit():
            ans2 = False if s[i-1].isdigit() or s[i+1].isdigit() else True
            # 如果是第一个数字
            if cnt is True:
                cnt = False
                ans2 = True if s[i] != '0' else False
    return ans1 and ans2

if __name__ == "__main__":
    main()