import copy
from code.algorithms import find_nearest as find

class FindNearest():

    def __init__(self, batteries, houses, factor):
        self.batteries = batteries.batteries
        self.houses = houses.houses
        self.batteries_copy = []
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
        self.batteries_copy = copy.deepcopy(self.batteries)
        print('Number of connected houses:', len(self.connected_houses))
        
        self.randomize()
        print('Number of connected houses after randomizing:', len(self.connected_houses))
        

    def randomize(self):
        if self.factor != 1:
            index = 0
            while len(self.random_generated) + len(self.connected_houses) != (len(self.houses)):
                length = len(self.random_generated)
                self.make_random(self.batteries_copy)

                if length == len(self.random_generated):
                    index += 1
                else:
                    index = 0

                # stop creating random connections after 100 unsuccesful attempts
                if index == 100:
                    self.restart()
                    break

            if len(self.random_generated) + len(self.connected_houses) == (len(self.houses)):
                self.place_random()

    def make_random(self, batteries):
    
        rand = find.find_random(self.not_connected, self.batteries_copy, self.batteries)
        combination = rand[0]
        if len(combination) != 0:
            self.random_generated.append(combination)
            self.not_connected.remove(rand[1])

    def place_random(self):
        for connection in self.random_generated:
            battery = connection[0]
            house = connection[1]
            find.make_connection(house, battery)
            self.connected_houses.append(house)

    def restart(self):
        self.random_generated = []
        self.batteries_copy = copy.deepcopy(self.batteries)
        self.not_connected = []

        for house in self.houses:
            if house.connected == False:
                self.not_connected.append(house)

        self.randomize()

    def output(self):
        return self.connected_houses, self.batteries


                        
