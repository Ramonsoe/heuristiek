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
        self.not_connected = []
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

        for house in self.houses:
            difference = 300 # magic number

            for battery in self.batteries:
                if len(battery.houses) > 0:
                    for bat_house in battery.houses:

                        x_diff = house.x_house - bat_house.x_house
                        y_diff = house.y_house - bat_house.y_house

                        # prevent negative numbers are treated as smaller differences
                        if x_diff < 0:
                            x_diff *= -1
                        if y_diff < 0:
                            y_diff *= -1

                        curr_diff = x_diff + y_diff

                        if battery.spare_capacity - house.output >= 0:
                            if curr_diff < difference:
                                difference = curr_diff
                                nearest_battery = bat_house.battery

                x_diff = house.x_house - battery.x_battery
                y_diff = house.y_house - battery.y_battery
                if x_diff < 0:
                        x_diff *= -1
                if y_diff < 0:
                        y_diff *= -1

                if battery.spare_capacity - house.output >= 0:
                    curr_diff = x_diff + y_diff
                    if curr_diff < difference:
                        difference = curr_diff
                        nearest_battery = battery

            if nearest_battery.spare_capacity - house.output >= 0:
                house.battery = nearest_battery
                house.connected = True
                nearest_battery.spare_capacity -= house.output
                nearest_battery.add_house(house)
                randomgrid.place
                self.connected_houses.append(house)

        print ('spare capacities:')
        for bat in self.batteries:
            print (bat.spare_cap)
            # print (len(bat.houses))
            # print (bat.spare_cap)
            # print ()

        print ()
        print ('Aantal huizen geplaatst:', len(self.connected_houses))


        for house in self.houses:
            if house.connected == False:
                self.not_connected.append(house)

        # if len(not_connected) > 0:

            print ()
            print ('Spares verdelen...')
            print ()
            # self.divide_spares(not_connected)
        if len(self.not_connected) > 0:
            print ()
            print ('Spares verdelen...')
            print ()
            self.spares()


    def spares(self):

        num_houses = len(self.houses)

        # while len(self.connected_houses) < num_houses:
        # for spare in not_connected:

        spare = self.not_connected[0]

        # largest_spare = 0 # magic number
        # for battery in self.batteries:
        #     if battery.spare_cap > largest_spare:
        #         largest_spare = battery.spare_cap
        #         bat_largest_spare = battery

        # capacity_difference = abs(largest_spare - spare.output)
        # print (capacity_difference)
        options = []

        # for battery in self.bat
        copy_houses = copy.deepcopy(self.connected_houses)
        distance = 300 # magic number
        for all_house in self.connected_houses:
            for house_large in copy_houses:
                if all_house.battery != house_large.battery:
                    if all_house.battery.spare_cap + all_house.output - house_large.output >= 0:
                        if house_large.battery.spare_cap - all_house.output + house_large.output >= spare.output:
                            curr_distance = abs(abs(all_house.x_house) - abs(house_large.x_house)) + abs(abs(all_house.y_house) - abs(house_large.y_house))
                            if curr_distance < distance:
                                distance = curr_distance
                                house_1 = house_large
                                house_2 = all_house
                                combi = [house_1, house_2]
                                options.append(combi)

        for option in options:
            house_1 = option[0]
            house_2 = option[1]
            if house_2.battery.spare_cap + house_2.output - house_1.output >= 0:
                if house_1.battery.spare_cap - house_2.output + house_1.output >= spare.output:
                    battery_for_spare = house_1.battery

                    for house in house_1.battery.houses:
                        if house == house_1:
                            house_1.battery.remove_house(house)

                    house_1.battery.add_house(house_2)
                    house_2.battery.add_house(house_1)

                    for house in house_2.battery.houses:
                        if house == house_2:
                            house_2.battery.remove_house(house)

                    house_1.battery = house_2.battery
                    house_2.battery = battery_for_spare
                    battery_for_spare.add_house(spare)
                    spare.battery = battery_for_spare
                    spare.connected = True
                    self.connected_houses.append(spare)
                    self.not_connected.pop(0)

        
        # print (not_connected[1])
        print('spare capacities:')
            
        for bat in self.batteries:
            print (bat.spare_cap)
        print ('Aantal huizen geplaatst:', len(self.connected_houses))
                        

    # def divide_spares(self, not_connected):

    #     while len(self.connected_houses) < 150:
            
    #         for spare in not_connected:
                
    #             largest_spare_cap = -1 # magic number
    #             for battery in self.batteries:
    #                 if battery.spare_capacity > largest_spare_cap:
    #                     largest_spare_cap = battery.spare_capacity
    #                     bat_most_spare = battery

    #             largest_output = 0
    #             for house in bat_most_spare.houses:
    #                 if house.output > largest_output:
    #                     largest_output = house.output
    #                     largest_house = house
                    
    #             bat_most_spare.houses.remove(largest_house)

    #             options = []

    #             for battery in self.batteries:
    #                 for house in battery.houses:
    #                     # difference_large = abs(abs(largest_spare_cap) + abs(largest_house.output) - abs(house.output))
    #                     # difference_new = abs(abs(battery.spare_capacity) + abs(house.output) - abs(largest_house.output))
    #                     if battery.spare_capacity - house.output + largest_house.output >= spare.output:
    #                         if bat_most_spare.spare_capacity - house.output + largest_house.output >= 0:
    #                             # if difference_large >= 0 and difference_new >= 0:
    #                             # if bat_most_spare.spare_capacity >= spare.output:
    #                             options.append(house)

    #             distance = 300 # magic number

    #             # print (len(options))
    #             # for house in options:
    #             #     curr_diff = abs(abs(house.x_house) - abs(spare.x_house)) + abs(abs(house.y_house) - abs(spare.y_house))
    #             #     if curr_diff < distance:
    #             #         distance = curr_diff
    #             #         nearest_house = house

    #             for house in options:

    #                 nearest_house = house
    #                 nearest_house_bat = nearest_house.battery
    #                 nearest_house.battery.houses.remove(nearest_house)
    #                 nearest_house_output = nearest_house.output

    #                 largest_house_bat = largest_house.battery
    #                 largest_house_output = largest_house.output

    #                 nearest_house.battery = largest_house_bat
    #                 largest_house.battery = nearest_house_bat

    #                 nearest_house_bat.spare_capacity = nearest_house_bat.spare_capacity + nearest_house_output - largest_house_output
    #                 largest_house_bat = largest_house_bat.spare_capacity + largest_house_output - nearest_house_output


    #                 for battery in self.batteries:
    #                     # print (battery.spare_capacity - spare.output)
    #                     if battery.spare_capacity - spare.output > 0:
    #                         battery.spare_capacity -= spare.output
    #                         battery.add_house(spare)
    #                         spare.connected = True
    #                         spare.battery = battery
    #                         self.connected_houses.append(spare)
    #                         break
    #                     else:
    #                         continue

    #         print (len(self.connected_houses))
    #         # for battery in self.batteries:
    #         #     print (battery.spare_capacity)

            
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
