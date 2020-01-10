import random


def random_battery(batteries):
    """pak een random batterij met genoeg spare capacity"""

    random_battery = random.choice(batteries)
    return random_battery

def random_house(houses):
    """pak een random huis die nog niet connected is"""

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

        print(random_battery.houses)
        print(random_battery.spare_capacity)
