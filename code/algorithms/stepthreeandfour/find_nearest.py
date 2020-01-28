"""
find_nearest.py

Ramon Soesan, Leon Brakkee, Layla Hoogeveen

File in which an algorithm is coded. This algorithm selects random houses and connects it to the closest power source.
"""


import copy
from code.classes.standardobjects.price import Price
from code.classes.stepthreeandfour.find_nearest import functions as find


class FindNearest():
    """FindNearest algorithm"""
    
    def __init__(self, batteries, houses):
        self.batteries = batteries.batteries
        self.houses = houses.houses

        # needed for price calculation
        self.battery_objects = batteries

        self.connected_houses = []
        self.best_houses = None
        self.best_batteries = None
        self.n = 0

        # large number needed for comparison
        self.best_price = 10000000

    def run(self, n):
        """Start algorithm. N parameter is the number of times the code should be run"""

        self.n = n
        run = 0
        while run < self.n:

            self.houses = find.sort(self.houses)
            find.run_divide(self.houses, self.batteries)

            # keep track of connected and unconnected houses
            self.make_connected_list()

            if self.all_connected() == False:
                self.restart()

            else:
                run += 1
                self.save_best_grid()

    def make_connected_list(self):
        """Keep track of connected houses"""

        for house in self.houses:
            if house.battery != None:
                self.connected_houses.append(house)

    def output(self):
        """Output needed for visualisation"""

        return self.best_houses, self.best_batteries, self.best_price

    def all_connected(self):
        """Check whether all houses are connected"""

        connected_batteries = 0

        # all houses should be in battery lists
        for battery in self.batteries:
            connected_batteries += len(battery.houses)

        # the sum of these two should be twice the number of houses
        if len(self.connected_houses) + connected_batteries == 2 * len(self.houses):
            return True

        return False


    def restart(self):
            """Remove all attributes from houses and batteries to start over"""

            self.connected_houses = []
            for house in self.houses:
                house.connected = False
                house.cables = []
                house.battery = None
                house.connected_houses = set()

            for battery in self.batteries:
                battery.houses = []
                battery.cables = []
                battery.spare_capacity = battery.capacity


    def save_best_grid(self):
        """Save cheapest solution"""

        calc_price = Price(self.houses, self.battery_objects)
        current_price = calc_price.price_total

        # if price is smaller than the current best_price, make this solution the best
        if current_price < self.best_price:
            self.best_houses = copy.deepcopy(self.houses)
            self.best_batteries = copy.deepcopy(self.battery_objects)
            self.best_price = current_price
