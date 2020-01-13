import copy

# from code.classes import houses
from code.classes.houses import Houses
from code.classes import batteries, houses

class AreaDivider():

    def __init__(self, all_batteries, all_houses):

            self.all_houses = all_houses.houses
            self.all_batteries = all_batteries.batteries

            # self.houses_copy = copy.deepcopy(self.houses)
            self.max_x = 0
            self.max_y = 0

            self.divided = self.divide_area(self.all_houses)

            # self.connected = 0

    def divide_area(self, houses):
        """Divide grid into areas"""

        # bubble sort
        x_swap = True
        while x_swap:
            x_swap = False
            for i in range(len(houses) - 1):
                if houses[i].x_house > houses[i + 1].x_house:
                    max_y = houses[i].y_house
                    houses[i], houses[i + 1] = houses[i + 1], houses[i]
                    x_ = True

        y_swap = True
        while y_swap:
            y_swap = False
            for i in range(len(houses) - 1):
                if houses[i].x_house == houses[i + 1].x_house:
                    if houses[i].y_house > houses[i + 1].y_house:
                        houses[i], houses[i + 1] = houses[i + 1], houses[i]
                        y_swap = True

        length = len(houses) - 1
        max_x = houses[length].x_house
        # print (houses)

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
