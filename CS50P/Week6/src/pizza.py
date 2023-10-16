import sys
from tabulate import tabulate
import csv

def main():
    table_list = []
    headers1 = ["Sicilian Pizza", "Small", "Large"]
    headers2 = ["Regular Pizza", "Small", "Large"]
    length = len(sys.argv)

    if length == 1:
        sys.exit("Too few command-line arguments")
    elif length > 2:
        sys.exit("Too many command-line arguments")
    else:
        file_name = sys.argv[1]
        
        if file_name.endswith("csv") is not True:
            sys.exit("Not a CSV file")
        
        try:
            with open(file_name, "r") as file:
                reader = csv.reader(file)
                for row in reader:
                    table_list.append(row)
            
            print(tabulate(table_list, headers="firstrow", tablefmt="grid"))
            
            
                
                

        except FileNotFoundError:
            sys.exit("File don't exist")

main()