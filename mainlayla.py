from code.algorithms import randomgrid, areadivider3, find_nearest as find
from code.classes import batteries, houses, randomgrid, find_nearest, price


if __name__ == "__main__":

    bats1 = batteries.Batteries('data/wijk1_batterijen.csv')
    houses1 = houses.Houses('data/wijk1_huizen.csv')

    bats2 = batteries.Batteries('data/wijk2_batterijen.csv')
    houses2 = houses.Houses('data/wijk2_huizen.csv')

    bats3 = batteries.Batteries('data/wijk3_batterijen.csv')
    houses3 = houses.Houses('data/wijk3_huizen.csv')

    # factor is the percentage of houses to connect to nearest battery
    # other houses will be connected randomly

    factor = 75
    finder = find_nearest.FindNearest(bats1, houses1, factor)
    outputs = finder.output()

    houses = outputs[0]
    batteries = outputs[1]

    
