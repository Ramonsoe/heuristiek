import random
import copy

# from code.classes import houses
from code.classes.houses import Houses
from code.classes import batteries, houses


def random_battery(batteries):
    """Returns random batteries"""

    random_battery = random.choice(batteries)
    return random_battery

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
        random_house.connect_house()
        random_battery.new_spare_capacity(random_house)


    # def remove_house(random_house, houses):
    #     if random_house.check_connection():
    #         print("<><<>,.,mll;mer;lermb;lr")
<<<<<<< HEAD
    #         house.pop_house(random_house)
=======
    #         house.pop_house(random_house)
>>>>>>> ed4cb77d8af9559f89462bf8b4a91cd974433884
