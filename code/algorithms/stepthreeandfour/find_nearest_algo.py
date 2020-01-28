
from code.classes.powerramon import cablepoints
import copy
import random

def sort(houses):
    """Shuffle the list for random results"""

    random.shuffle(houses)

    return houses

def run_divide(houses, batteries):
    for house in houses:
        divide_houses(house, batteries, houses)

def divide_houses(house, batteries, houses):

    cable_house = None
    nearest = None
    smallest_distance = 300 # magic number

    for battery in batteries:
        if battery.check_availability(house) == True:

            for bat_house in battery.houses:

                # if house not in bat_house.connected_houses and house != bat_house:
                #     current_distance = calculate_distance(house, bat_house)

                #     # change nearest battery when smaller distance is found
                #     if current_distance < smallest_distance:
                #         smallest_distance = current_distance
                #         nearest = bat_house

                #     # check cables as well
                #     for cable in bat_house.cables:
                #         if len(bat_house.cables) != 0:
                #             distance = calculate_distance(house, cable)
                #             if distance != None:
                #                 if distance < smallest_distance:
                #                     smallest_distance = distance
                #                     nearest = cable
                #                     cable_house = bat_house

            # check whether a battery itself is near(er than houses already iterated over)
            current_distance = calculate_distance(house, battery)
            if current_distance < smallest_distance:
                smallest_distance = current_distance
                nearest = battery

    # connect house to nearest battery or to the battery connected to nearest house
    if nearest is not None:
        make_connection(house, nearest, cable_house)

def make_connection(house, connection, cable_house):
    '''Place cables from house to nearest point'''

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

    else:

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
 
def calculate_distance(house, point):
    '''Return Manhattan distance of two coordinates'''

    # print (house, point)
    if hasattr(point, 'x'):
        distance = abs(house.x - point.x) + abs(house.y - point.y)
        return distance

    # else:
    #     distance = abs(house.x - (point.x1 + point.x2) / 2) + abs(house.y - (point.y1 + point.y2) / 2)
    #     return distance

def place_cables(house, connection):
    cable = cablepoints.Cablepoints()
    cable.place_cables(house, connection)

