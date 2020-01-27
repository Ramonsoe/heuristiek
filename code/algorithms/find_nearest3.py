
from code.classes import cableslayla as cables
import copy
import random

def sort(houses):
    """Sort houses from largest to smallest output"""

    # random.shuffle(houses)

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

    num_houses_to_connect = round(factor * len(houses))
    
    house_num = 0
    for house in houses:
        nearest_battery = None

        # stop connecting houses to batteries when factor % of the houses is connected
        if house_num == num_houses_to_connect:
            break

        house_num += 1
        smallest_distance = 300 # magic number

        for battery in batteries:
            
            if battery.check_availability(house) == True:

                # if battery has a list of already connected houses, iterate over these houses as well
                if len(battery.houses) > 0:
                    for bat_house in battery.houses:
                        current_distance = calculate_distance(house, bat_house)

                        # change nearest battery when smaller distance is found
                        if current_distance < smallest_distance:
                            smallest_distance = current_distance
                            nearest_battery = bat_house.battery

                # check whether a battery itself is near(er than houses already iterated over)
                current_distance = calculate_distance(house, battery)
                if current_distance < smallest_distance:
                    smallest_distance = current_distance
                    nearest_battery = battery

        # connect house to nearest battery or to the battery connected to nearest house
        if nearest_battery is not None:
            make_connection(house, nearest_battery)

def make_connection(house, battery):

    house.battery = battery
    house.connected = True
    battery.add_house(house)
    # place_cables(house, battery)

 
def calculate_distance(house, connection_to_house):

    x_distance = abs(house.x - connection_to_house.x)
    y_distance = abs(house.y - connection_to_house.y)
    current_distance = x_distance + y_distance

    return current_distance


def find_random(not_connected, copy_batteries, batteries):
    house = random.choice(not_connected)
    
    battery = random.choice(copy_batteries)
    index = copy_batteries.index(battery) 
    combination = []
    
    if battery.check_availability(house):

        battery.spare_capacity -= house.output
        combination = [batteries[index], house]

    return combination, house, batteries

# def place_cables(house, battery):

#     cables.Cables(house, battery)

