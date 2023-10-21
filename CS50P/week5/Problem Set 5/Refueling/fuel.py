def main():
    fraction = input("Fraction: ")
    print(gauge(convert(fraction)))
		
def convert(fraction):
    try:
        x, y = fraction.split("/")
        x, y = int(x), int(y)
        if x >= y and y !=0 :
            raise ValueError
        if y == 0:
            raise ZeroDivisionError
    except ValueError:
        raise ValueError
    else:
        return round((x / y) * 100)

def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"
    
if __name__ == "__main__":
    main()
