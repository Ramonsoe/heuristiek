import random
import copy

# from code.classes import houses
from code.classes.houses import Houses
from code.classes import batteries, houses, cables, battery, house


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

def get_closest_house(houses, powersources):

    closest_house = None
    current_powersource = None
    manhattan_distance = 10^6       # magic number

    for house in houses.houses_copy:

        for powersource in powersources:

            house_distance = man_distance(house, powersource)

            if house_distance < manhattan_distance:

                manhattan_distance = house_distance

                closest_house = house

                current_powersource = powersource

    return closest_house, current_powersource

def man_distance(house, powersource):
    """ Returns manhattan distance of two coordinates """

    distance = abs(house.x - powersource.x) + abs(house.y - powersource.y)
    return distance


def distance_all(house, batteries):

    all_distances = {}

    for battery in batteries:

        distance = abs(house.x_house - battery.x_battery) + abs(house.y_house - battery.y_battery)
        all_distances[battery] = distance

    return all_distances

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
        random_house.connect_house(random_battery)
        houses.connect_house(random_house)
        random_battery.new_spare_capacity(random_house)
        random_battery.add_house(random_house)
