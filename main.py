from code.algorithms import randomgrid, areadivider
from code.classes import batteries, houses
# from code.visualisation import *

if __name__ == "__main__":

    bats1 = batteries.Batteries('data/wijk1_batterijen.csv')
    houses1 = houses.Houses('data/wijk1_huizen.csv')

    bats2 = batteries.Batteries('data/wijk2_batterijen.csv')
    houses2 = houses.Houses('data/wijk2_huizen.csv')

    bats3 = batteries.Batteries('data/wijk3_batterijen.csv')
    houses3 = houses.Houses('data/wijk3_huizen.csv')

    bat = batteries.Batteries('data/wijk1_batterijen.csv')
    house = houses.Houses('data/wijk1_huizen.csv')

    house1 = areadivider.AreaDivider(bats1, houses1)
    # house1.divide_area()

    # for battery in bat.batteries:
    #     count = 0
    #     if house.houses_copy is None:
    #         exit()
    #     length_houses = len(house.houses_copy)

    #     while count < 100 and len(house.houses_copy) != 0:
    #         # random huis
    #         house1 = randomgrid.random_house(house.houses_copy)

    #         # voeg huis toe
    #         randomgrid.connect_house_to_battery(house1, battery)
    #         print (house1)

    #         # verwijder huis van lijst
    #         if house1.check_connection():
    #             house.pop_house(house1)

    #         previous_length = length_houses
    #         length_houses = len(house.houses_copy)
    #         if previous_length == length_houses:
    #             count += 1
    #         else:
    #             count = 0

    #     print(len(battery.houses))

    # if len(house.houses_copy) == 0:
    #     print("succes")
    # else:
    #     print("failure")
