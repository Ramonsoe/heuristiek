import copy
from code.algorithms import find_nearest3 as find
from . import cableslayla as cables
from . import connect_to_battery
import gc

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
        gc.disable()

    def run(self):
        '''Start algorithm'''

        # if not every house should be placed randomly
        if self.factor != 0:
            self.houses = find.sort(self.houses)
            find.divide_largest(self.houses, self.batteries, self.factor)

        # keep track of connected and unconnected houses
        for house in self.houses:
            if house.connected == False:
                self.not_connected.append(house)
            else:
                self.connected_houses.append(house)

        # copied list needed for trying out connections without actually affecting the real list of objects
        self.batteries_copy = copy.deepcopy(self.batteries)

        self.randomize()
        self.place_all()

    def randomize(self):
        '''Run the randomizing process'''

        # do not randomize when 100% of the houses should be placed in a non-random way
        if self.factor != 1:
            attempt = 0
            while len(self.random_generated) + len(self.connected_houses) != (len(self.houses)):
                length = len(self.random_generated)
                self.make_random(self.batteries_copy)

                # for each time the random_generated list has not been appended, increase attempt
                if length == len(self.random_generated):
                    attempt += 1

                # restart attempt if random_generated list has changed in length
                else:
                    attempt = 0

                # stop creating random connections after 100 unsuccesful attempts
                if attempt == 100:

                    # try again
                    self.restart_random()
                    break
            
            # place houses permanently when a connection for each previously unconnected house is found
            if len(self.random_generated) + len(self.connected_houses) == (len(self.houses)):
                self.place_random()

    def make_random(self, batteries):
        '''Find random solutions for house/battery connections'''
    
        rand = find.find_random(self.not_connected, self.batteries_copy, self.batteries)
        combination = rand[0]

        # only append to list if a random combination of house and battery has been found
        if len(combination) != 0:
            self.random_generated.append(combination)
            self.not_connected.remove(rand[1])

    def place_random(self):
        '''Place the random houses when a valid solution has been found'''

        for connection in self.random_generated:
            battery = connection[0]
            house = connection[1]
            find.make_connection(house, battery)
            self.connected_houses.append(house)

    def restart_random(self):
        '''Restart the randomizing process when no valid solution has been found'''

        # clear everything for a fresh start
        self.random_generated = []
        self.batteries_copy = copy.deepcopy(self.batteries)
        self.not_connected = []

        # not randomly placed houses remain the same
        for house in self.houses:
            if house.connected == False:
                self.not_connected.append(house)

        self.randomize()

    def output(self):
        return self.connected_houses, self.batteries

    def all_connected(self):
        '''Check whether all houses are connected'''

        connected_houses = 0
        connected_batteries = 0

        # check for the connected attribute
        for house in self.houses:
            if house.connected == True and house.battery is not None:
                connected_houses += 1

        # all houses should be in battery lists as well
        for battery in self.batteries:
            connected_batteries += len(battery.houses)

        # the sum of these two should be twice the number of houses
        if connected_houses + connected_batteries == 2 * len(self.houses):
            return True

        return False

    def place_all(self):
        '''Place cables for every house house'''

        # houses are from now on only connected if they have a(n) (in)direct cable connection to their battery
        for house in self.houses:
            house.connected = False

        # place cables from house to nearest (point connected to) battery
        for house in self.houses:
            cables.Cables(house, self.houses)

    def connect_all_to_battery(self):
        '''Connect all houses to batteries if they are not (in)directly connected yet'''
        
        index = 0
        for house in self.houses:
            if house.connected == False:
                connect_to_battery.ConnectToBattery(house, self.houses)
                index += 1

            if index % 10 == 0:
                print (index)

    def restart_all(self):
        '''Remove all attributes from houses and batteries to start over'''

        for house in self.houses:
            house.connected = False
            house.cables = []
            house.all_cable_segments = []
            house.battery = None
            house.distance_to_battery = None
        
        for battery in self.batteries:
            battery.houses = []
            battery.cables = []
            battery.spare_capacity = battery.capacity

                        
