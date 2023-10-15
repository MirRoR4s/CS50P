import sys


def main():
    length = len(sys.argv)

    if length == 1:
        sys.exit("Too few command-line arguments")
    elif length > 2:
        sys.exit("Too many command-line arguments")
    else:
        file_name = sys.argv[1]
        
        if file_name.endswith("py") is not True:
            sys.exit("Not a python file")
        
        line_number = 0
        
        try:
            with open(file_name, "r") as f:
                for line in f.readlines():
                    line = line.lstrip()
                    
                    if line.startswith("#") or is_blank(line):
                        continue
                    else:
                        line_number += 1
                        
            print(f"line number = {line_number}")

        except FileNotFoundError:
            sys.exit("File don't exist")


def is_blank(line):
    if len(line) == 0:
        return True

    for i in line:

        if i != ' ':
            return False

        return True


main()