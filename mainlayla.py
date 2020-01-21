from code.algorithms import find_nearest as find
from code.classes import batteries, houses, find_nearest, price, change_cables
from code.classes import pricelayla as price
from code.visualisation import vis2
import pickle

# import sys
# sys.setrecursionlimit(100000000)


if __name__ == "__main__":

    # bats1 = batteries.Batteries('data/wijk1_batterijen.csv')
    # houses1 = houses.Houses('data/wijk1_huizen.csv')

    bats2 = batteries.Batteries('data/wijk2_batterijen.csv')
    houses2 = houses.Houses('data/wijk2_huizen.csv')

    bats3 = batteries.Batteries('data/wijk3_batterijen.csv')
    houses3 = houses.Houses('data/wijk3_huizen.csv')

    # factor is the percentage of houses to connect to nearest battery
    # other houses will be connected randomly

    bats1 = batteries.Batteries('data/wijk1_batterijen.csv')
    houses1 = houses.Houses('data/wijk1_huizen.csv')
    factor = 100

    finder = find_nearest.FindNearest(bats1, houses1, factor)
    outputs = finder.output()
    houses = outputs[0]
    batteries = outputs[1]

    price_results = price.Price(houses, batteries)
    total = price_results.total_price

    print ('Totaalprijs:', total)

    # vis2.Visual(houses, bats1)

    # with open('dumps/wijk1.pkl', 'wb') as output:
    #     pickle.dump(amazing_houses, output, pickle.HIGHEST_PROTOCOL)
    #     pickle.dump(best_batteries, output, pickle.HIGHEST_PROTOCOL)

    # with open('dumps/wijk1.pkl', 'rb') as file:
    #     data = pickle.load(file)
