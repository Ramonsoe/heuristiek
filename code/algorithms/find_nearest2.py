
from code.classes import cableslayla2 as cables
import copy
import random

def sort(houses):
    """Shuffle the list for random results"""

    random.shuffle(houses)

    return houses

def sort_battery_houses(houses):
    """Shuffle the list for random results"""

    swap = True
    while swap:

        swap = False
        for i in range(len(houses) - 1):
            new_distance = calculate_distance(houses[i], houses[i].battery)
            newer_distance = calculate_distance(houses[i + 1], houses[i + 1].battery)
            if new_distance < newer_distance:
                houses[i], houses[i + 1] = houses[i + 1], houses[i]
                swap = True

    return houses

def run_divide(houses, batteries):
    for house in houses:
        get_sub_connections(houses)
        if house.connected == False:
            divide_houses(house, houses, batteries)

def divide_houses(house, houses, batteries):

    cable_house = None
    nearest = None

    smallest_distance = 300 # magic number

    for battery in batteries:

        if battery.check_availability(house) == True:

            # if battery has a list of already connected houses, iterate over these houses as well
            for bat_house in battery.houses:
                if house not in bat_house.connected_houses:
                    current_distance = calculate_distance(house, bat_house)

                    # change nearest battery when smaller distance is found
                    if current_distance < smallest_distance:
                        smallest_distance = current_distance
                        nearest = bat_house

                    # check cables as well
                    for cable in bat_house.all_cable_segments:
                        distance = calculate_distance(house, cable)
                        if distance < smallest_distance:
                            smallest_distance = distance
                            nearest = cable
                            cable_house = bat_house

            # check whether a battery itself is near(er than houses already iterated over)
            current_distance = calculate_distance(house, battery)
            if current_distance < smallest_distance:
                smallest_distance = current_distance
                nearest = battery

    # connect house to nearest battery or to the battery connected to nearest house
    make_connection(house, nearest, cable_house)

def make_connection(house, connection, cable_house):

    if hasattr(connection, 'output'):
        if connection.connected == True:
            house.connected = True
            for connected_house in house.connected_houses:
                connected_house.connected = True

        house.battery = connection.battery
        house.connected_houses.add(connection)
        house.connected_houses.update(connection.connected_houses)
        connection.connected_houses.add(house)
        connection.connected_houses.update(house.connected_houses)
        connection.battery.add_house(house)

        place_cables(house, connection)

    elif hasattr(connection, 'capacity'):
        house.battery = connection
        house.connected = True
        connection.add_house(house)

        place_cables(house, connection)

    elif hasattr(connection, 'x1'):

        if hasattr(cable_house, 'connected'):
            if cable_house.connected == True:
                house.connected = True
                for connected_house in house.connected_houses:
                    connected_house.connected = True
            house.battery = cable_house.battery
            
            house.connected_houses.add(cable_house)
            house.connected_houses.update(cable_house.connected_houses)
            cable_house.connected_houses.add(house)
            cable_house.connected_houses.update(house.connected_houses)
            cable_house.battery.add_house(house)


        place_cables(house, connection)
    return (connection)


def find_furthest(batteries):

    for battery in batteries:
        distance = 0 # magic number ff aanpassen
        for house in battery.houses:
            new_distance = calculate_distance(battery, house)
            if new_distance > distance:
                distance = new_distance
                furthest = house
        print(battery, furthest)

        make_connection(furthest, battery, battery)
        # run_cables(furthest, battery, batteries)

def run_cables(connection, battery, batteries):

    # for house in battery.houses:
    for house in battery.houses:
        distance = 1000000
        if house.connected == False:
            new_distance = calculate_distance(connection, house)
            if new_distance < distance:
                distance = new_distance
                nearest_house = house
        # print (nearest_house)
        connection = make_connection(connection, nearest_house, nearest_house)
        
def new_cables(house_to_connect):

    # get_sub_connections(houses)
    cable_house = None
    nearest = None
    smallest_distance = 300 # magic number

    for house in house_to_connect.battery.houses:
        if house not in house.connected_houses:
            current_distance = calculate_distance(house_to_connect, house)

            # change nearest battery when smaller distance is found
            if current_distance < smallest_distance:
                smallest_distance = current_distance
                nearest = house

    # check cables as well
    for cable in house.all_cable_segments:
        distance = calculate_distance(house_to_connect, cable)
        if distance < smallest_distance:
            smallest_distance = distance
            nearest = cable
            cable_house = house

    # check whether a battery itself is near(er than houses already iterated over)
    current_distance = calculate_distance(house_to_connect, house_to_connect.battery)
    if current_distance < smallest_distance:
        smallest_distance = current_distance
        nearest = house_to_connect.battery

    # connect house to nearest battery or to the battery connected to nearest house
    make_connection(house_to_connect, nearest, cable_house)

def calculate_distance(house, point):
    '''Return Manhattan distance of two coordinates'''

    if hasattr(point, 'x'):
        distance = abs(house.x - point.x) + abs(point.y - point.y)
        return distance

    else:
        distance = abs(house.x - (point.x1 + point.x2) / 2) + abs(house.y - (point.y1 + point.y2) / 2)
        return distance

def get_sub_connections(houses):

    connected = set()
    for house in houses:
        if house.connected == True:
            connected.update(house.connected_houses)

    for house in connected:
        house.connected = True
        for subhouse in house.connected_houses:
            subhouse.connected_houses.update(house.connected_houses)
            subhouse.connected = True
            for subsub in subhouse.connected_houses:
                subsub.connected = True

def place_cables(house, connection):

    cables.Cables(house, connection)

