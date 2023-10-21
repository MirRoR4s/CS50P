# cd && mkdir response && cd response && code response.py

from validator_collection import checkers

def main():
    print(validate(input("Email: ")))

def validate(email):
    return "Valid" if checkers.is_email(email) else "Invalid"


if __name__ == "__main__":
    main()
