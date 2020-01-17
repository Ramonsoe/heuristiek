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
        for battery in self.batteries:
            print (battery.calc_spare_capacity())
        self.batteries_copy = copy.deepcopy(self.batteries)
        self.randomize()
        
        print()

        print ('Aantal huizen geplaatst na random:', len(self.connected_houses))
        for battery in self.batteries:
            print (battery.calc_spare_capacity())

    def randomize(self):
        if self.factor != 1:
            index = 0
            while len(self.random_generated) + len(self.connected_houses) != (len(self.houses)):
                self.make_random(self.batteries_copy)
        
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

    def output(self):
        return self.connected_houses, self.batteries


                        
