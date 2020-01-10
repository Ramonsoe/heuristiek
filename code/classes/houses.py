import csv
from .house import House
import copy

class Houses():

    def __init__(self, house_file):
        self.houses = self.load_houses(house_file)
<<<<<<< HEAD
        self.connected = []
=======

        self.houses_copy = copy.deepcopy(self.houses)
        self.connected = 0
>>>>>>> ed4cb77d8af9559f89462bf8b4a91cd974433884

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
<<<<<<< HEAD
=======

    def connected_house(self):

        self.connected += 1

    def all_houses_connected(self):
        if self.connected != len(self.houses):
            return False
        return True

    def pop_house(self, house):
        # print(self.houses_copy)
        self.houses_copy.remove(house)
>>>>>>> ed4cb77d8af9559f89462bf8b4a91cd974433884
