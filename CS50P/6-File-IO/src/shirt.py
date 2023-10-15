import sys
from PIL import Image, ImageOps
import os


def main():
    length = len(sys.argv)

    if length < 3:
        sys.exit("Too few command-line arguments")
    elif length > 3:
        sys.exit("Too many command-line arguments")
    
    input_images = sys.argv[1]
    output_images = sys.argv[2]
    
    input_ext = os.path.splitext(input_images)[-1]
    output_ext = os.path.splitext(output_images)[-1]

    if input_ext != output_ext:
        sys.exit("Input and output have different extensions")

    try:
        shirt = Image.open("shirt.png")
        shirt_size = shirt.size
        input = Image.open(input_images)
        resize_input = ImageOps.fit(input, shirt_size)
        resize_input.paste(shirt, shirt)
        resize_input.save("test.png")
        
        
        
        
        
        
    except FileNotFoundError:
        sys.exit("Invalid input")



if __name__ == "__main__":
    main()