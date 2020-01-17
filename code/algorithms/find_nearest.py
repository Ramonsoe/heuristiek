
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

        # stop connecting houses to batteries when factor % of the houses is connected
        if house_num == num_houses_to_connect:
            break

        house_num += 1
        smallest_distance = 300 # magic number

        for battery in batteries:
            
            if check_availability(house, battery) == True:

                # if battery has a list of already connected houses, iterate over these houses as well
                if len(battery.houses) > 0:
                    for bat_house in battery.houses:
                        current_distance = calculate_houses_distance(house, bat_house)

                        # change nearest battery when smaller distance is found
                        if current_distance < smallest_distance:
                            smallest_distance = current_distance
                            nearest_battery = bat_house.battery

                # check whether a battery itself is near(er than houses already iterated over)
                current_distance = calculate_battery_distance(house, battery)
                if current_distance < smallest_distance:
                    smallest_distance = current_distance
                    nearest_battery = battery

        # connect house to nearest battery or to the battery connected to nearest house
        make_connection(house, nearest_battery)
        connected_houses.append(house)

    print ('Aantal huizen geplaatst:', len(connected_houses))

    # list of unconnected house needed for random placement later on
    for house in houses:
        if house.connected == False:
            not_connected.append(house)

    return houses, batteries, connected_houses, not_connected

def make_connection(house, battery):

    house.battery = battery
    house.connected = True
    battery.new_spare_capacity(house)
    battery.add_house(house)
    place_cables(house, battery)

def check_availability(house, battery):

    if battery.spare_capacity - house.output >= 0:
        return True
    return False
 
def calculate_houses_distance(house, connection_to_house):

    x_distance = abs(house.x_house - connection_to_house.x_house)
    y_distance = abs(house.y_house - connection_to_house.y_house)
    current_distance = x_distance + y_distance

    return current_distance

def calculate_battery_distance(house, battery):

    x_distance = abs(house.x_house - battery.x_battery)
    y_distance = abs(house.y_house - battery.y_battery)
    current_distance = x_distance + y_distance

    return current_distance

def find_random(not_connected, copy_batteries, batteries):
    house = random.choice(not_connected)
    battery = random.choice(copy_batteries)
    index = copy_batteries.index(battery) 
    combination = []
    
    if check_availability(house, battery):

        battery.spare_capacity -= house.output
        combination = [batteries[index], house]

    return combination, house, batteries

def place_cables(house, battery):

    cable = cables.Cables(house, battery)

