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

            self.houses_copy = copy.deepcopy(self.all_houses)
            self.max_x = 0
            self.max_y = 0
            self.areas = {}

            self.divided = self.sort(self.all_houses, self.all_batteries)

            # self.connected = 0

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
                # print (start_area, end_area)
                if spare_cap - house.output >= 0:
                    spare_cap = spare_cap - house.output
                    area.append(house)
                else:
                    spare_houses.append(house)

            else:

                # add area to dict
                self.areas[spare_cap] = area
                spare_houses.append(house)
                # start new area
                start_area = end_area + 1
                end_area = start_area + area_width - 1
                spare_cap = self.battery_capacity
                area = []

        self.areas[spare_cap] = area

        index = 0
        for area in self.areas:
            index += 1
            print ('batterij', index, 'capaciteit over:', area)

        all = 0
        for area in self.areas.values():
            all += len(area)
        
        print ('huizen verdeeld:', all)

        print ('spares:', len(spare_houses))

        self.divide_spares(self.areas, spare_houses)

    def divide_spares(self, areas, spares):

        x_difference = 0
        y_difference = 0
        for spare_house in spares:
            options = []
            for cap, houses in areas.items():
                for house in houses:
                    if cap - house.output >= 0:
                        options.append(spare_house)

            # for option in options:

            x_swap = True
            while x_swap:
                x_swap = False
                for i in range(len(houses) - 1):
                    if houses[i].x_house > houses[i + 1].x_house:
                        houses[i], houses[i + 1] = houses[i + 1], houses[i]
                        x_swap = True
                # if x_difference > option.x_house - spare_house.x_house:
                #     hallo = 0
                # elif 
                # x_difference = option.x_house - spare_house.x_house
                # y_difference = option.y_house - spare_house.y_house

                        # print ('poep')
                # if area.value 
                # print (cap, houses)
                # print (house.output, house.x_house, ',', house.y_house)
        pass


    def random_house(houses):
        """Returns random battery if it's not connected"""

        while True:
            random_house = random.choice(houses)
            if not random_house.connected:
                return random_house

    def connect_house_to_battery(random_house, random_battery):
        """stop het random huis in de battery"""

        battery_capacity = random_battery.spare_capacity
        house_output = random_house.output


        if (battery_capacity - house_output) >= 0:
            random_battery.add_house(random_house)
            random_house.connect_house(random_battery)
            random_battery.new_spare_capacity(random_house)


        # def remove_house(random_house, houses):
        #     if random_house.check_connection():
        #         print("<><<>,.,mll;mer;lermb;lr")
        #         house.pop_house(random_house)
