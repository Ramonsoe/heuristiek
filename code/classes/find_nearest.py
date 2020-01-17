import copy

from code.algorithms import find_nearest as find

class FindNearest():

    def __init__(self, batteries, houses, factor):
        self.batteries = batteries.batteries
        self.houses = houses.houses
        self.connected_houses = []
        self.not_connected = []
        self.random_generated = []
        self.factor = factor / 100
        self.run()

    def run(self):
        self.houses = find.sort(self.houses)
        divide = find.divide_largest(self.houses, self.batteries, self.factor)
        self.houses = divide[0]
        self.batteries = divide[1]
        self.connected_houses = divide[2]
        self.not_connected = divide[3]
    #     batteries = copy.deepcopy(self.batteries)

    #     while len(self.random_generated) + len(self.connected_houses) != (len(self.houses)):
    #         self.make_random(batteries)
    #         if len(self.random_generated) + len(self.connected_houses) == (len(self.houses)):
    #             self.place_random()

    # def make_random(self, batteries):
    
    #     rand = find.find_random(self.not_connected, batteries, self.connected_houses)
    #     combination = rand[1]
    #     if len(combination) != 0:
    #         self.random_generated.append(combination)
    #         self.not_connected.remove(rand[2])

    # def place_random():
    #     for combination in self.random_generated:

    def output(self):
        return self.connected_houses, self.batteries


                        
