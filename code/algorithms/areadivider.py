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
        """Divide grid into areas"""

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

        self.divide_areas(houses, len(self.all_batteries))

    def divide_areas(self, houses, num_of_batteries):
        spare_cap = self.battery_capacity
        area_width = self.max_x / num_of_batteries
        spare_houses = []

        start_area = 0
        end_area = start_area + area_width
        area = []

        for house in houses:

            if house.x_house <= end_area:
                if spare_cap - house.output >= 0:
                    spare_cap = spare_cap - house.output
                    area.append(house)
                else:
                    spare_houses.append(house)

            else:

                # add area to dict
                area_object = Area()
                self.area_objects.append(area_object)
                area_object.houses = area
                area_object.spare_capacity = spare_cap
                spare_houses.append(house)

                # start new area
                start_area = end_area + 1
                end_area = start_area + area_width - 1
                spare_cap = self.battery_capacity
                area = []

        area_object = Area()
        self.area_objects.append(area_object)
        area_object.houses = area
        area_object.spare_capacity = spare_cap

        index = 0
        print ('Vóór het verdelen:')
        for area in self.area_objects:
            index += 1
            print ('batterij', index, '- capaciteit over:', area.spare_capacity, 'huizen verbonden', len(area.houses))

        self.divide_spares(spare_houses)

    def divide_spares(self, spares):

        x_difference = 300 # magic number
        y_difference = 300

        all_areas = self.area_objects
        areas = []
        used_spares = []
        smallest_output = 300 # magic number

        for spare in spares:
            if spare.output < smallest_output:
                smallest_output = spare.output

        for area in all_areas:
            if area.spare_capacity > smallest_output:
                areas.append(area)

        for spare_house in spares:
            options = []
            for area in areas:
                for house in area.houses:
                    if area.spare_capacity - spare_house.output >= 0:
                        options.append(house)

            for option in options:
                curr_x_diff = option.x_house - spare_house.x_house
                curr_y_diff = option.y_house - spare_house.y_house
                
                if curr_x_diff < x_difference and curr_x_diff < y_difference:
                    x_difference = curr_x_diff
                    best_option = option
                elif curr_y_diff < y_difference and curr_y_diff < x_difference:
                    y_difference = curr_y_diff
                    best_option = option

            for area in areas:
                if best_option in area.houses:
                    if area.spare_capacity - best_option.output >= 0:
                        area.append_houses(spare_house)
                        area.spare_capacity -= best_option.output
                        used_spares.append(spare_house)

        print ('Na het verdelen:')
        length = 0

        for house in spares:
            if house not in used_spares:
                for area in areas:
                    if area.spare_capacity - house.output >= 0:
                        area.append_houses(spare_house)
                        area.spare_capacity -= house.output

        houses_used = []
        for area in self.area_objects:
            for house in area.houses:
                houses_used.append(house)
            print (area)
            length += len(area.houses)
        
        
        print (length, 'huizen verdeeld')

    def random_house(houses):
        """Returns random battery if it's not connected"""

        while True:
            random_house = random.choice(houses)
            if not random_house.connected:
                return random_house

    def connect_house_to_battery(house, battery):
        """stop het random huis in de battery"""

        battery_capacity = random_battery.spare_capacity
        house_output = random_house.output


        if (battery_capacity - house_output) >= 0:
            random_battery.add_house(random_house)
            random_house.connect_house(random_battery)
            random_battery.new_spare_capacity(random_house)


class Area(object):

    def __init__(self):
        self.houses = []
        self.battery = None
        self.spare_capacity = 0
    
    def append_houses(self, house):
        self.houses.append(house)

    def __repr__(self):
        return f"Connected to: {self.battery}, spare capacity: {self.spare_capacity}, Number of houses: {len(self.houses)}"
