import copy

# from code.classes import houses
from code.classes.houses import Houses
from code.classes import batteries, houses

class AreaDivider():

    def __init__(self, all_batteries, all_houses):

            self.all_houses = all_houses.houses
            self.all_batteries = all_batteries.batteries

            # all batteries in one neighbourhood have the same capacity
            self.battery_capacity = all_batteries.batteries[0].capacity

            self.max_x = 0
            self.max_y = 0
            self.area_objects = []

            self.divided = self.sort(self.all_houses, self.all_batteries)

    def sort(self, houses, batteries):
        """Sort grid"""

        # bubble sort
        x_swap = True
        while x_swap:
            x_swap = False
            for i in range(len(houses) - 1):
                if houses[i].x_house > houses[i + 1].x_house:
                    houses[i], houses[i + 1] = houses[i + 1], houses[i]
                    x_swap = True

        y_swap = True
        while y_swap:
            y_swap = False
            for i in range(len(houses) - 1):
                if houses[i].y_house > self.max_y:
                    self.max_y = houses[i].y_house
                if houses[i].x_house == houses[i + 1].x_house:
                    if houses[i].y_house > houses[i + 1].y_house:
                        houses[i], houses[i + 1] = houses[i + 1], houses[i]
                        y_swap = True

        batx_swap = True
        while batx_swap:
            batx_swap = False
            for i in range(len(batteries) - 1):
                if batteries[i].x_battery > batteries[i + 1].x_battery:
                    batteries[i], batteries[i + 1] = batteries[i + 1], batteries[i]
                    batx_swap = True

        baty_swap = True
        while baty_swap:
            baty_swap = False
            for i in range(len(batteries) - 1):
                if batteries[i].x_battery == batteries[i + 1].x_battery:
                    if batteries[i].y_battery > batteries[i + 1].y_battery:
                        batteries[i], batteries[i + 1] = batteries[i + 1], batteries[i]
                        baty_swap = True

        self.all_houses = houses
        self.all_batteries = batteries
        self.max_x = houses[len(houses) - 1].x_house

        self.divide_areas(houses, batteries)

    def divide_areas(self, houses, batteries):

        spare_cap = self.battery_capacity
        spare_houses = []
        area = []
        areas = []

        for house in houses:
            if spare_cap - house.output >= 0:
                spare_cap = spare_cap - house.output
                area.append(house)
            else:
                area_object = Area()
                self.area_objects.append(area_object)
                area_object.houses = area
                area_object.spare_capacity = spare_cap
                area = []
                spare_cap = self.battery_capacity
                # spare_houses.append(house)
                # spare_houses.append(house)

        area_object = Area()
        self.area_objects.append(area_object)
        area_object.houses = area
        area_object.spare_capacity = spare_cap
        
        # areas.append(area)
        for area in self.area_objects:
            print (area)
                

        #     else:

        #         # add area to dict
        #         area_object = Area()
        #         self.area_objects.append(area_object)
        #         area_object.houses = area
        #         area_object.spare_capacity = spare_cap
        #         spare_houses.append(house)

        #         # start new area
        #         start_area = end_area + 1
        #         end_area = start_area + area_width - 1
        #         spare_cap = self.battery_capacity
        #         area = []

        # area_object = Area()
        # self.area_objects.append(area_object)
        # area_object.houses = area
        # area_object.spare_capacity = spare_cap

        # index = 0
        # print ('Vóór het verdelen:')
        # for area in self.area_objects:
        #     index += 1
        #     print ('batterij', index, '- capaciteit over:', area.spare_capacity, 'huizen verbonden', len(area.houses))

            

class Area(object):

    def __init__(self):
        self.houses = []
        self.battery = None
        self.spare_capacity = 0
    
    def append_houses(self, house):
        self.houses.append(house)

    def __repr__(self):
        return f"Connected to: {self.battery}, spare capacity: {self.spare_capacity}, Number of houses: {len(self.houses)}"
