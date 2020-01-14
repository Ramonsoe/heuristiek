import copy

# from code.classes import houses
from code.classes.houses import Houses
from code.classes import batteries, houses

class AreaDivider():

    def __init__(self, all_batteries, all_houses):

            self.houses = all_houses.houses
            self.batteries = all_batteries.batteries

            # all batteries in one neighbourhood have the same capacity
            self.battery_capacity = all_batteries.batteries[0].capacity
            self.area_objects = []
            self.divided = self.sort()

    def sort(self):
        """Divide grid into areas"""

        # bubble sort
        swap = True
        while swap:
            swap = False
            for i in range(len(self.houses) - 1):
                if self.houses[i].output < self.houses[i + 1].output:
                    self.houses[i], self.houses[i + 1] = self.houses[i + 1], self.houses[i]
                    swap = True

        for house in self.houses:
            print (house.output)

class Area(object):

    def __init__(self):
        self.houses = []
        self.battery = None
        self.spare_capacity = 0
    
    def append_houses(self, house):
        self.houses.append(house)

    def __repr__(self):
        return f"Connected to: {self.battery}, spare capacity: {self.spare_capacity}, Number of houses: {len(self.houses)}"
