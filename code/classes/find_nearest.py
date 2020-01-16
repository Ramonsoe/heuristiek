import copy

from code.algorithms import find_nearest as find

class FindNearest():

    def __init__(self, batteries, houses, factor):
        self.batteries = batteries.batteries
        self.houses = houses.houses
        self.connected_houses = []
        self.not_connected = []
        self.factor = factor / 100

        self.run()

    def run(self):
        self.houses = find.sort(self.houses)
        divide = find.divide_largest(self.houses, self.batteries, self.factor)
        self.houses = divide[0]
        self.batteries = divide[1]
        self.connected_houses = divide[2]
        self.not_connected = divide[3]

        # while len(self.not_connected) > 0:
        #     find.random(self.not_connected, self.batteries)

        for house in self.connected_houses:
            find.place_cables(house, house.battery)

    def output(self):
        return self.connected_houses, self.batteries


                        
