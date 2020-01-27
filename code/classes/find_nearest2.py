import copy
from code.algorithms import find_nearest2 as find
from . import cableslayla2 as cables
from . import connect_to_battery
import gc

class FindNearest():

    def __init__(self, batteries, houses):
        self.batteries = batteries.batteries
        self.houses = houses.houses
        self.batteries_copy = []
        self.connected_houses = []
        self.not_connected = []
        self.random_generated = []
        self.run()
        gc.disable()

    def run(self):
        '''Start algorithm'''

        self.houses = find.sort(self.houses)
        find.run_divide(self.houses, self.batteries)

        # keep track of connected and unconnected houses
        self.make_connected_list()

        print(len(self.connected_houses), 'aan batterij')
        if (len(self.connected_houses)) != len(self.houses):
            self.restart()

        self.restart_cables()

        houses = find.sort_battery_houses(self.houses)
        self.houses = houses

        for house in self.houses:
            find.new_cables(house)
            
        self.make_connected_list()

        index = 0

        for house in self.houses:
            if house.connected == True:
                index += 1

        print('for real verbonden:', index)

    def output(self):
        return self.houses, self.batteries

    def restart_cables(self):
        '''Remove all attributes from houses and batteries to start over'''
        self.connected_houses = []

        for house in self.houses:
            house.cables = []
            house.all_cable_segments = []
            house.connected = False

    def make_connected_list(self):
        for house in self.houses:
            if house.battery == None:
                self.not_connected.append(house)
            else:
                self.connected_houses.append(house)

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

                        
