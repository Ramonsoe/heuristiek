import random
import copy

# from code.classes import houses
from code.classes.houses import Houses

# from code.classes.powerramon.powersources
from code.classes.powerramon import batteries, houses, cables, battery, house, powersources, cablepoints


def random_powersource(powersources):
    """Returns random batteries"""

    random_powersource = random.choice(powersource)
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

    for house in houses:

        try:
            for battery in powersources.batteries:
                powersource = battery

                house_distance = man_distance(house, powersource)

                if house_distance < manhattan_distance:

                    manhattan_distance = house_distance

                    closest_house = house

                    current_powersource = powersource
        except:
            pass

        try:
            for powersource in powersources:

                house_distance = man_distance(house, powersource)

                if house_distance < manhattan_distance:

                    manhattan_distance = house_distance

                    closest_house = house

                    current_powersource = powersource
        except:
            pass
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

def clear_powersources(powersources):

    for powersource in powersources:

        try:
            for battery in powersource.batteries:
                battery.houses = []
                battery.spare_capacity = battery.capacity
        except:
            pass

    powersources.powersource_objects.clear()

def show_results(batteries):
    for battery in batteries.batteries:
        print(f"({battery.x_battery}, {battery.y_battery})")
        print(battery.houses)

def add_powersource(newpowersources):

    ps = powersources.Powersources()
    ps.add_powersource(newpowersources)

def connect_house_to_powersource(closest_house, current_powersource, houses, powersources):
    """stop het random huis in de battery"""



    try:
        spare_cap = current_powersource.spare_capacity
        battery = current_powersource
    except:

        pass

    try:
        battery = current_powersource.battery
    except:
        pass

    # print(closest_house)
    house_output = closest_house.output
    battery_capacity = battery.spare_capacity


    if (battery_capacity - house_output) >= 0:
        closest_house.connect_house(closest_house, battery)
        houses.connect_house(closest_house)
        battery.new_spare_capacity(closest_house)
        battery.add_house(closest_house)
