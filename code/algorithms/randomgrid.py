import random
import copy

# from code.classes import houses
from code.classes.houses import Houses
from code.classes import batteries, houses, cables, house


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

def connect_house_to_battery(random_house, random_battery):
    """stop het random huis in de battery"""

    battery_capacity = random_battery.spare_capacity
    house_output = random_house.output


    if (battery_capacity - house_output) >= 0:
        random_battery.add_house(random_house)
        random_house.connect_house(random_battery)
        random_battery.new_spare_capacity(random_house)

def place_cables(house, battery):

    cable = cables.Cables(house, battery)
    house_coordinate, battery_coordinate = cable.get_all_coordinates()
    house.cables.append(cable.make_cable_list(house_coordinate, battery_coordinate))
