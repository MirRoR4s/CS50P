def main():
    user_input = input("Greeting: ")
    ans = value(user_input)
    print(ans)

def value(greeting):
    greeting = greeting.lower().strip()
    if greeting.startswith("hello"):
        return 0
    elif greeting.startswith("h"):
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()