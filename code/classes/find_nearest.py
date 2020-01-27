import copy
from code.algorithms import find_nearest as find
from . import cableslayla2 as cables
import gc

class FindNearest():

    def __init__(self, batteries, houses):
        self.batteries = batteries.batteries
        self.houses = houses.houses
        self.connected_houses = []
        self.run()
        gc.disable()

    def run(self):
        '''Start algorithm'''

        # if not every house should be placed randomly
        self.houses = find.sort(self.houses)
        find.run_divide(self.houses, self.batteries)

        # keep track of connected and unconnected houses
        self.make_connected_list()

        if (len(self.connected_houses)) != len(self.houses):
            self.restart()

    def make_connected_list(self):

        for house in self.houses:
            if house.battery != None:
                self.connected_houses.append(house)

    def output(self):
        return self.houses, self.batteries

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

    def restart(self):
            '''Remove all attributes from houses and batteries to start over'''

            self.connected_houses = []
            for house in self.houses:
                house.connected = False
                house.cables = []
                house.all_cable_segments = []
                house.battery = None
                house.connected_houses = set()
            
            for battery in self.batteries:
                battery.houses = []
                battery.cables = []
                battery.cable_objects = []
                battery.spare_capacity = battery.capacity
            
            self.run()

                        
