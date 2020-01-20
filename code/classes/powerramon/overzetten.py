import random
import copy

# from code.classes import houses
from code.classes.houses import Houses
from code.classes import batteries, houses, cables, battery, house


def random_powersource(powersources):
    """Returns random batteries"""

    random_powersource = random.choice(powersources)
    return random_powersource

def random_house(houses):
    """Returns random battery if it's not connected"""

    while True:
        random_house = random.choice(houses)
        if not random_house.connected:
            return random_house

def remove_house(house, houses):
    houses.remove(house)

def clean_batteries(batteries):
    for battery in batteries.batteries:
        battery.houses = []
        battery.spare_capacity = battery.capacity

def show_results(batteries):
    for battery in batteries.batteries:
        print(f"({battery.x_battery}, {battery.y_battery})")
        print(battery.houses)

def connect_house_to_battery(random_house, random_battery, houses, batteries):
    """stop het random huis in de battery"""

    battery_capacity = random_battery.spare_capacity
    house_output = random_house.output


    if (battery_capacity - house_output) >= 0:
        # print(house.add_house(random_battery))
        random_house.connect_house(random_house, random_battery)
        houses.connect_house(random_house)
        random_battery.new_spare_capacity(random_house)
        random_battery.add_house(random_house)
