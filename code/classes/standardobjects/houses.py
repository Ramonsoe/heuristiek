"""
houses.py

Layla Hoogeveen, Leon Brakkee and Ramon Soesan

File in which house objects are created and a list of houses is filled with these objects.
"""


import csv
from .house import House
import copy


class Houses():


    def __init__(self, house_file):

        self.houses = self.load_houses(house_file)
        self.houses_unconnected = self.copy_houses(self.houses)
        self.houses_connected = []


    def connect_house(self, house):
        """Connect house"""

        self.houses_connected.append(house)


    def house_unconnect(self, house):
        """Remove house from connected houses list"""

        self.houses_connected.remove(house)
        house.disconnect()


    def remove_unconnected(self, house):
        """Remove a house from unconnected houses"""

        for housee in self.houses_unconnected:
            if housee.output is house.output:
                self.houses_unconnected.remove(housee)


    def load_houses(self, house_file):
        """Load the houses from the input file into a list"""

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


    def copy_houses(self, houses):
        """Copy list of houses"""

        return copy.deepcopy(houses)


    def fill_unconnected(self):
        """Fill unconnected houses list with all houses"""

        self.houses_unconnected = self.copy_houses(self.houses)


    def add_unconnected(self, house):
        """Add house to unconnected houses list"""

        self.houses_unconnected.append(house)


    def empty_connected(self):
        """Clear connected houses list"""

        self.houses_connected.clear()
