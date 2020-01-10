from code.algorithms import randomgrid
from code.classes import batteries, houses
# from code.visualisation import *

if __name__ == "__main__":

    # bat = Batteries()
    bat = batteries.Batteries('data/wijk1_batterijen.csv')
    # house = Houses()
    house = houses.Houses('data/wijk1_huizen.csv')

    # algorithms

    bat1 = randomgrid.random_battery(bat.batteries)
    house1 = randomgrid.random_house(house.houses)
    randomgrid.connect_house_to_battery(house1, bat1)

    while House.all_houses_connected() == False:
        randomgrid.connect_house_to_battery(house1, bat1)
