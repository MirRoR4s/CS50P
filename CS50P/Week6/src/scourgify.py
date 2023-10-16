import sys

import csv

def main():
    table = []
    length = len(sys.argv)

    if length < 2:
        sys.exit("Too few command-line arguments")
    elif length > 3:
        sys.exit("Too many command-line arguments")
    else:
        file_name = sys.argv[1]
        after_csv_file_name = sys.argv[2]
        if file_name.endswith("csv") is not True:
            sys.exit("Not a CSV file")
        
        try:
            with open(file_name, "r") as file:
                reader = csv.DictReader(file)
                
                for row in reader:
                    first, last= row['name'].split(',')
                    house = row['house']
                    table.append({"first": first, "last": last, "house": house})   
            
            with open(after_csv_file_name, "w") as file1:
                writer = csv.DictWriter(file1, fieldnames=["first", "last", "house"])
                writer.writeheader()
                for row in table:
                    writer.writerow(row)

        except FileNotFoundError:
            sys.exit("File don't exist")

main()