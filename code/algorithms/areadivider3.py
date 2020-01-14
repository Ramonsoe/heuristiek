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
        self.connected_houses = []
        self.sort()

    def sort(self):
        """Sort houses from largest to smallest output"""

        # bubble sort
        swap = True
        while swap:
            swap = False
            for i in range(len(self.houses) - 1):
                if self.houses[i].output < self.houses[i + 1].output:
                    self.houses[i], self.houses[i + 1] = self.houses[i + 1], self.houses[i]
                    swap = True

        # for house in self.houses:
        #     print ('output:', house.output, 'coordinates:', house.x_house, ',', house.y_house)

        self.divide_largest()

    def divide_largest(self):

        num_houses = len(self.houses)
        not_connected = []
        index = 0

        for house in self.houses:

            x_difference = 300 # magic number
            y_difference = 300
            for battery in self.batteries:
                for bat_house in battery.houses:

                    curr_x_diff = house.x_house - bat_house.x_house
                    curr_y_diff = house.y_house - bat_house.y_house

                    # prevent negative numbers are treated as smaller differences
                    if curr_x_diff < 0:
                        curr_x_diff *= -1
                    if curr_y_diff < 0:
                        curr_y_diff *= -1

                    if battery.spare_capacity - house.output >= 0:
                        if curr_x_diff < x_difference and curr_x_diff < y_difference:
                            x_difference = curr_x_diff
                            nearest_battery = battery
                        elif curr_y_diff < y_difference and curr_y_diff < x_difference:
                            y_difference = curr_y_diff
                            nearest_battery = battery
                
                curr_x_diff = house.x_house - battery.x_battery
                curr_y_diff = house.y_house - battery.y_battery


                if curr_x_diff < 0:
                        curr_x_diff *= -1
                if curr_y_diff < 0:
                        curr_y_diff *= -1
                if battery.spare_capacity - house.output >= 0:
                    if curr_x_diff < x_difference and curr_x_diff < y_difference:
                        x_difference = curr_x_diff
                        nearest_battery = battery
                    elif curr_y_diff < y_difference and curr_y_diff < x_difference:
                        y_difference = curr_y_diff
                        nearest_battery = battery

            if nearest_battery.spare_capacity - house.output >= 0:
                house.battery = nearest_battery
                house.connected = True
                nearest_battery.spare_capacity -= house.output
                nearest_battery.add_house(house)
                self.connected_houses.append(house)

            index += 1

        print ('spare capacities:')
        houses_in_batteries = 0
        for bat in self.batteries:
            print (bat.spare_capacity)
            houses_in_batteries += len(bat.houses)

        print ()
        print ('Aantal huizen geplaatst:', houses_in_batteries)

        not_connected = []

        for house in self.houses:
            if house.connected == False:
                not_connected.append(house)

        # print ()
        # print ('Spares verdelen...')
        # print ()
        # self.divide_spares(not_connected)

    # def divide_spares(self, not_connected):
    #     x_diff = 300 # magic number
    #     y_diff = 300 
    #     largest_spare_cap = -1
    #     for battery in self.batteries:
    #         if battery.spare_capacity > largest_spare_cap:
    #             largest_spare_cap = battery.spare_capacity
    #             bat_most_spare = battery

    #     for spare in not_connected:
    #         options = []
    #         difference = largest_spare_cap - spare.output
    #         for house in self.connected_houses:
    #             if spare.output - house.output >= difference:
    #                 if house.battery.spare_capacity - difference >= 0:
    #                     options.append(house)
            
    #         curr_x_diff = spare.x_house - battery.x_battery
    #         curr_y_diff = house.y_house - battery.y_battery
    #         for option in options:
    #             if curr_x_diff < x_difference and curr_x_diff < y_difference:
    #                 x_difference = curr_x_diff
    #                 nearest_battery = battery
    #             elif curr_y_diff < y_difference and curr_y_diff < x_difference:
    #                 y_difference = curr_y_diff
    #                 nearest_battery = battery


            
    def output(self):

        return self.connected_houses, self.batteries

# class Area(object):

#     def __init__(self):
#         self.houses = []
#         self.battery = None
#         self.spare_capacity = 0
    
#     def append_houses(self, house):
#         self.houses.append(house)

#     def __repr__(self):
#         return f"Connected to: {self.battery}, spare capacity: {self.spare_capacity}, Number of houses: {len(self.houses)}"
