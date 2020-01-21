from code.algorithms import find_nearest as find
from code.classes import batteries, houses, find_nearest, price
from code.classes import pricelayla as price
from code.visualisation import vis2, format_cables
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

    factor = 0
    def compare_prices(batteries, houses, factor):
        finder = find_nearest.FindNearest(batteries, houses, factor)
        outputs = finder.output()
        houses = outputs[0]
        batteries = outputs[1]
        # print ('factor:', factor)
        # print('price:')
        calculate_price = price.Price(houses, batteries)
        return calculate_price, houses, batteries

    # factor = 100
    # bats1 = batteries.Batteries('data/wijk1_batterijen.csv')
    # houses1 = houses.Houses('data/wijk1_huizen.csv')
    # output = compare_prices(bats1, houses1, factor)
    # price_per_factor = output[0]
    # houses_output = output[1]
    # batteries_output = output[2]
    # total_price = price_per_factor.total_price()
    # print (total_price)

    factor = 100
    index = 0
    # opper_index = 0
    smallest_price = 10000000

    while factor <= 100:
        # print (factor)
        index = 0
        
        while index < 1:
            bats1 = batteries.Batteries('data/wijk1_batterijen.csv')
            houses1 = houses.Houses('data/wijk1_huizen.csv')

            output = compare_prices(bats1, houses1, factor)
            price_per_factor = output[0]
            houses_output = output[1]
            batteries_output = output[2]
            total_price = price_per_factor.total_price()

            if total_price < smallest_price:
                best_houses = houses_output
                amazing_houses = houses1
                best_batteries = bats1
                smallest_price = total_price
                best_factor = factor
                cables = price_per_factor.cables()

            index += 1

        factor += 1

    
    print()
    print('best option:')
    print(smallest_price)
    print('factor:', factor)


    print (cables)
    formatted = format_cables.FormatCables(best_houses)


    vis2.Visual(best_houses, best_batteries, formatted.x, formatted.y)

    with open('dumps/wijk1.pkl', 'wb') as output:
        pickle.dump(amazing_houses, output, pickle.HIGHEST_PROTOCOL)
        pickle.dump(best_batteries, output, pickle.HIGHEST_PROTOCOL)

    with open('dumps/wijk1.pkl', 'rb') as file:
        data = pickle.load(file)
