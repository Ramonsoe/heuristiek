import random
import copy
from itertools import filterfalse


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
    """looks for the smallest distance between all unconnected houses and powersources"""

    # print(len(houses), len(powersources))

    # initialize

    # try:
    closest_house = houses[0]
    current_powersource = powersources[0]
    manhattan_distance = 10^6       # magic number

    # loop over all houses and powersources, if new smallest distance, change current powersource and house
    for house in houses:
        for powersource in powersources:

            house_distance = man_distance(house, powersource)

            if house_distance < manhattan_distance:

                manhattan_distance = house_distance

                closest_house = house

                current_powersource = powersource


    return closest_house, current_powersource
    # except:
    #     # print("adjust check_constraint")
    #     return False


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
    """remove house from list of unconnected houses"""

    houses.remove(house)

def clear_powersources(powersources):

    for powersource in powersources:

        try:
            for battery in powersource.batteries:
                battery.houses = []
                battery.spare_capacity = battery.capacity
        except:
            pass

    powersources.clear()

def show_results(batteries):
    for battery in batteries.batteries:
        print(f"({battery.x_battery}, {battery.y_battery})")
        print(battery.houses)

def add_powersource(newpowersources):

    ps = powersources.Powersources()
    ps.add_powersource(newpowersources)
    return ps.powersources_objects

def remove_powersources(battery, powersources):
    """function to remove powersources if capacity of battery is too low"""


    for powersource in reversed(powersources):

        try:

            if powersource == battery:
                powersources.remove(powersource)
        except:
            pass

        try:
            if powersource.battery == battery:
                powersources.remove(powersource)
        except:
            pass

    return powersources

def check_constraint(current_powersource, powersources, min_capacity):
    """function to check the sparecapacity for the current powersource to see if too low"""


    try:
        current_spare = current_powersource.spare_capacity
        battery = current_powersource
    except:
        pass

    try:
        current_spare = current_powersource.battery.spare_capacity
        battery = current_powersource.battery
    except:
        pass

    # reomve powersources from list of powersources if lower than 20 (magic number)
    if current_spare < 30:
        remove_powersources(battery, powersources)

def check_feasibility(houses_list, houses, powerlist):

    if len(houses_list) == 0:
        # print("halo")
        for i in range(30):
            random_connected = random.choice(houses.houses_connected)

            if random_connected in powerlist:
                powerlist.remove(random_connected)

                for cable in random_connected.cables[0]:
                    powerlist.remove(cable)


            houses_list.append(random_connected)

            battery = random_connected.battery

            if not battery in powerlist:
                powerlist.append(battery)

            battery.remove_house(random_connected)
            battery.restore_capacity(random_connected)
            houses.add_unconnected(random_connected)
            houses.house_unconnect(random_connected)


def connect_house_to_powersource(closest_house, current_powersource, houses, powersources):
    """stop het random huis in de battery"""
    try:
        spare_cap = current_powersource.spare_capacity
        battery = current_powersource
        battery_capacity = battery.spare_capacity
    except:
        pass

    try:
        battery = current_powersource.battery
        battery_capacity = current_powersource.battery.spare_capacity

    except:
        pass

    # take the outpout of the closest_house to check if it fits in bat
    house_output = closest_house.output
    # print(battery)

    # if house fits, take care of the following steps
    if (battery_capacity - house_output) >= 0:
        closest_house.connect_house(closest_house, battery)
        houses.connect_house(closest_house)
        battery.new_spare_capacity(closest_house)
        battery.add_house(closest_house)
        houses.remove_unconnected(closest_house)
