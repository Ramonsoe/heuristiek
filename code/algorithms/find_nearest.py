
from code.classes import cables
import copy
import random

def sort(houses):
    """Sort houses from largest to smallest output"""

    # bubble sort
    swap = True
    while swap:
        swap = False
        for i in range(len(houses) - 1):
            if houses[i].output < houses[i + 1].output:
                houses[i], houses[i + 1] = houses[i + 1], houses[i]
                swap = True

    return houses

def divide_largest(houses, batteries, factor):
    connected_houses = []
    not_connected = []
    num_houses_to_connect = round(factor * len(houses))
    
    house_num = 0
    for house in houses:
        if house_num == num_houses_to_connect:
            break
        house_num += 1
        difference = 300 # magic number

        for battery in batteries:
            if len(battery.houses) > 0:
                for bat_house in battery.houses:

                    x_diff = abs(house.x_house - bat_house.x_house)
                    y_diff = abs(house.y_house - bat_house.y_house)

                    curr_diff = x_diff + y_diff

                    if battery.spare_capacity - house.output >= 0:
                        if curr_diff < difference:
                            difference = curr_diff
                            nearest_battery = bat_house.battery

            x_diff = abs(house.x_house - battery.x_battery)
            y_diff = abs(house.y_house - battery.y_battery)

            if battery.spare_capacity - house.output >= 0:
                curr_diff = x_diff + y_diff
                if curr_diff < difference:
                    difference = curr_diff
                    nearest_battery = battery

        if nearest_battery.spare_capacity - house.output >= 0:
            house.battery = nearest_battery
            house.connected = True
            nearest_battery.new_spare_capacity(house)
            nearest_battery.add_house(house)
            connected_houses.append(house)

    print ('Aantal huizen geplaatst:', len(connected_houses))

    for house in houses:
        if house.connected == False:
            not_connected.append(house)

    return houses, batteries, connected_houses, not_connected

def find_random(not_connected, batteries, connected):
    house = random.choice(not_connected)
    battery = random.choice(batteries)    
    combination = []
    if battery.calc_spare_capacity() - house.output >= 0:

        # house.battery = battery
        # battery.add_house(house)
        # print ('Added house:', house)
        combination = [battery, house]
        # connected.append(house)
        battery.spare_capacity -= house.output

    return connected, combination, house

def place_cables(house, battery):

    cable = cables.Cables(house, battery)
    house_coordinate, battery_coordinate = cable.get_all_coordinates()
    cable.make_cable_list(house_coordinate, battery_coordinate)
    cables_house = cable.make_cable_list(house_coordinate, battery_coordinate)
    house.add_cable(cables_house)
