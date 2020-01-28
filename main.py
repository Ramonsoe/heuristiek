from code.algorithms.steponeandtwo import randomgrid
from code.algorithms.stepthreeandfour import algomanhattan
from code.classes.steponeandtwo import batteries, houses, functions, price, cables, cable, house
from code.classes.stepthreeandfour import batteries, houses, price, powersources, cablepoints, house
from code.visualisation import random

if __name__ == "__main__":

    # prompt user for neighbourhood

    # prompt user for neighbourhood
    neighbourhood = input("Enter neighbourhood (1, 2 or 3):  ")

    # load the houses and batteries
    houses = houses.Houses(f'data/wijk{neighbourhood}_huizen.csv')
    batteries = batteries.Batteries(f'data/wijk{neighbourhood}_batterijen.csv')

    # running the algorithm
    randomgrid = randomgrid.Randomgrid(houses, batteries)
    all_houses, price = randomgrid.randomgrid

    # plot
    print("Total price:", price.price_total)
    all_houses = randomgrid.randomgrid
    vis = random.Visual(all_houses, batteries.batteries)
    a,b,c,d = vis.get_values()
    vis.make_plot(a,b,c,d)
