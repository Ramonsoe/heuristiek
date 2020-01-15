import copy

# from code.classes import houses
from code.classes.houses import Houses
from code.classes import batteries, houses

from code.algorithms import randomgrid


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
                randomgrid.place_cables(house,nearest_battery)
                self.connected_houses.append(house)


        not_connected = []

        for house in self.houses:
            if house.connected == False:
                not_connected.append(house)

        # if len(not_connected) > 0:

        #     print ()
        #     print ('Spares verdelen...')
        #     print ()
        #     # self.divide_spares(not_connected)
        #     self.spares(not_connected)


    def spares(self, not_connected):

        num_houses = len(self.houses)

        # while len(self.connected_houses) < num_houses:
        for spare in not_connected:

            largest_spare = 0 # magic number
            for battery in self.batteries:
                if battery.spare_cap > largest_spare:
                    largest_spare = battery.spare_cap
                    bat_largest_spare = battery

            options = []

            distance = 300 # magic number
            for all_house in self.connected_houses:
                for house_large in bat_largest_spare.houses:
                    if all_house.battery != bat_largest_spare:
                        if all_house.battery.spare_cap + all_house.output - house_large.output >= 0:
                            if house_large.battery.spare_cap - all_house.output + house_large.output >= spare.output:
                                curr_distance = abs(abs(all_house.x_house) - abs(house_large.x_house)) + abs(abs(all_house.y_house) - abs(house_large.y_house))
                                if curr_distance < distance:
                                    distance = curr_distance
                                    options.append(house_large)
                                    house_1 = house_large
                                    house_2 = all_house
                                    combi = [house_1, house_2]
                                    options.append(combi)


            battery_for_spare = house_1.battery
            # print (house_1)
            house_1.battery.remove_house(house_1)
            print (house_1)
            house_2.battery.add_house(house_1)
            house_2.battery.remove_house(house_2)
            house_1.battery.add_house(house_2)

            battery_for_spare.add_house(spare)
            spare.battery = battery_for_spare
            spare.connected = True
            self.connected_houses.append(spare)

        print('spare capacities:')

        for bat in self.batteries:
            print (bat.spare_capacity)
        print ('Aantal huizen geplaatst:', len(self.connected_houses))


    def output(self):

        return self.connected_houses, self.batteries
