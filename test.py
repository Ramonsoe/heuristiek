import csv
from Huizen_Batterijen import *

def read_file():
    with open("Huizen_Batterijen/wijk1_huizen.csv", "r") as csv_file:
        reader = csv.reader(csv_file)
        list_results = list(reader)
        print (list_results)

if __name__ == "__main__":
    read_file()