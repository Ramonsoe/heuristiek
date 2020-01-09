import csv
from .house import House


class Houses():

    def __init__(self, house_file):
        self.houses = self.load_houses(house_file)

    def load_houses(self, house_file):
        """load the houses from the input file into a list"""

        house_objects = []

        with open(house_file, "r") as csv_file:
            reader = csv.reader(csv_file)
            houses = list(reader)
            houses.pop(0)

            for house in houses:
                x = house[0]
                y = house[1].strip(' ')
                output = house[2].strip(' ')
                house_object = House(x, y, output)
                house_objects.append(house_object)
        
        return house_objects
