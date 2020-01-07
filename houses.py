import csv
from Huizen_Batterijen import *

class Houses():

    def __init__(self):
        self.houses = []

    def parse_houses(self):
        with open("Huizen_Batterijen/wijk1_huizen.csv", "r") as csv_file:
            reader = csv.reader(csv_file)
            houses = list(reader)
            houses.pop(0)
            
            for house in houses:
                info = []

                dict = {}
                dict['x'] = house[0]
                dict['y'] = house[1].strip(' ')
                dict['location'] = f"{dict['x'],dict['y']}"
                dict['output'] = house[2].strip(' ')
                info.append(dict)
                self.houses.append(info)
            
            return (self.houses)
            # print (self.houses)

if __name__ == "__main__":
    house = Houses()
    house.parse_houses()

