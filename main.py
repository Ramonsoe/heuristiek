from code.algorithms import randomgrid
from code.classes import batteries, houses
# from code.visualisation import *

if __name__ == "__main__":

    # bat = Batteries()

    bat = batteries.Batteries('data/wijk1_batterijen.csv')
    # house = Houses()
    house = houses.Houses('data/wijk1_huizen.csv')
    # print(house)
    # algorithms

    # bat1 = randomgrid.random_battery(bat.batteries)
    # house1 = randomgrid.random_house(house.houses_copy)
    # print(">>>",house1)
    # randomgrid.connect_house_to_battery(house1, bat1)

    # while house.all_houses_connected() == False:
    #     # try:
    #     bat1 = randomgrid.random_battery(bat.batteries)
    #     house1 = randomgrid.random_house(house.houses_copy)
    #     randomgrid.connect_house_to_battery(house1, bat1)
    #     # randomgrid.remove_house(house1, houses.houses_copy)
    #     # print("<><><><><", house1.check_connection())
    #     if house1.check_connection():
    #         house.pop_house(house1)
    #     print(len(house.houses_copy))

    for battery in bat.batteries:
        print(battery)
        count = 0
        if house.houses_copy is None:
            exit()
        length_houses = len(house.houses_copy)

        while count < 100 and len(house.houses_copy) != 0:
            # random huis
            house1 = randomgrid.random_house(house.houses_copy)

            # voeg huis toe
            randomgrid.connect_house_to_battery(house1, battery)

            # verwijder huis van lijst
            if house1.check_connection():
                house.pop_house(house1)

            previous_length = length_houses
            length_houses = len(house.houses_copy)
            if previous_length == length_houses:
                count += 1
            else:
                count = 0

        print(len(battery.houses))

    if len(house.houses_copy) == 0:
        print("succes")
    else:
        print("failure")