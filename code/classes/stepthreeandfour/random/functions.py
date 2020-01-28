"""
functions.py

Layla Hoogeveen, Leon Brakkee and Ramon Soesan

File where all functions of the algomanhattan are coded.
"""


import random
import copy
from itertools import filterfalse
from code.classes.standardobjects import batteries, houses, battery, house, price, powersources, cablepoints


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


def get_closest_house(houses, powersources):
    """looks for the smallest distance between all unconnected houses and powersources"""

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


def man_distance(house, powersource):
    """ Returns manhattan distance of two coordinates """

    distance = abs(house.x - powersource.x) + abs(house.y - powersource.y)
    return distance


def remove_house(house, houses):
    """remove house from list of unconnected houses"""

    houses.remove(house)


def clear_powersources(powersources):
    """function where list of powersources is emptied"""

    # restore battery info for every battery in powersources to initial info
    for powersource in powersources:

        try:
            for battery in powersource.batteries:
                battery.houses = []
                battery.spare_capacity = battery.capacity
        except:
            pass

    # clear the list of powersources
    powersources.clear()

def connect_cable(house, powersource):

    cable_power = cablepoints.Cablepoints()
    cable = cable_power.place_cables(closest_house, current_powersource)
    print("iets")
    return cable


def calc_price(houses, batteries):

    pricetotal = price.Price(houses, batteries)

    return pricetotal


def append_powersource(powersources, closest_house):

    powersources.append(closest_house)


def append_cables(powersources, cables):

    for cable in cables:
        powersources.append(cable)

def copy_list(list):

    return copy.deepcopy(list)


def add_powersource(newpowersources):
    """add a new powersource to the list of powersources"""

    # use a function from pwersources.py
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

    # remove powersources from list of powersources if lower than 20 (magic number)
    if current_spare < min_capacity:
        remove_powersources(battery, powersources)


def check_feasibility(houses_list, houses, powerlist, steps_back):
    """function to check if a solution is stillfeasible, i.e. there are still houses left to match with powersources"""

    # if no houses, remove random houses
    if len(houses_list) == 0:

        # perform x times, where x is the user defined number of step backs
        for i in range(steps_back):
            random_connected = random.choice(houses.houses_connected)

            # remove selected house and its cables from powerlist
            if random_connected in powerlist:
                powerlist.remove(random_connected)

                for cable in random_connected.cables[0]:
                    powerlist.remove(cable)

            # append selected house to list of unconnected houses
            houses_list.append(random_connected)

            battery = random_connected.battery

            # check if battery of sleected house is still in powersources list
            if not battery in powerlist:
                powerlist.append(battery)

            # adjust battery and houses
            battery.remove_house(random_connected)
            battery.restore_capacity(random_connected)
            houses.add_unconnected(random_connected)
            houses.house_unconnect(random_connected)


def minimal_output(houses):
    """function to calculate the minimum outpout of all houses in a neighbourhood"""

    all_outputs = []
    for house in houses.houses_unconnected:
        all_outputs.append(house.output)

    return min(all_outputs)


def connect_house_to_powersource(closest_house, current_powersource, houses, powersources):
    """put the random house in a battery"""

    # use try except because the list of powersources consists out of both houses, batteries and cables
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

    # if house fits, take care of the following steps
    if (battery_capacity - house_output) >= 0:
        closest_house.connect_house(closest_house, battery)
        houses.connect_house(closest_house)
        battery.new_spare_capacity(closest_house)
        battery.add_house(closest_house)
        houses.remove_unconnected(closest_house)
