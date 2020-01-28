"""
functions.py

Layla Hoogeveen, Leon Brakkee and Ramon Soesan

File with all functions used in the random algorithms.
"""


import random
import copy
from code.classes.steponeandtwo import batteries, houses, cables, battery, house


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


def connect_house_to_battery(random_house, random_battery, houses, batteries):
    """stop het random huis in de battery"""

    battery_capacity = random_battery.spare_capacity
    house_output = random_house.output

    if (battery_capacity - house_output) >= 0:
        random_house.connect_house(random_house, random_battery)
        houses.connect_house(random_house)
        random_battery.new_spare_capacity(random_house)
        random_battery.add_house(random_house)
