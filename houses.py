import csv
from Huizen_Batterijen import *

class Houses():

    def __init__(self):
        self.houses = []

    def parse_houses(self):
        with open("Huizen_Batterijen/wijk1_huizen.csv", "r") as csv_file:
            reader = csv.reader(csv_file)
            self.houses = list(reader)
            self.houses.pop(0)

            
            for house in self.houses:
                x = house[0]
                y = house[1]
                output = house[2]

                housing = House(x, y, output)

                print(housing)

class House(object):

    def __init__(self, x, y, output):

        self.x_house = x
        self.y_house = y
        self.output = output

    def __str__(self):

        return f"x-coordinate: {self.x_house}, y-coordinate: {self.y_house}, output: {self.output}"




if __name__ == "__main__":
    house = Houses()
    house.parse_houses()
