from code.algorithms.steponeandtwo import randomgrid
from code.algorithms.stepthreeandfour import algomanhattan
from code.classes.standardobjects import batteries, houses
from code.classes.output import output
from code.visualisation import random, manhattan

if __name__ == "__main__":

    # prompt user for neighbourhood
    neighbourhood = input("Enter neighbourhood (1, 2 or 3):  ")

    # load the houses and batteries
    houses = houses.Houses(f'data/wijk{neighbourhood}_huizen.csv')
    batteries = batteries.Batteries(f'data/wijk{neighbourhood}_batterijen.csv')

    section = input("With cable overlap enter 1. Without cable overlap enter 2: ")


    if int(section) == 1:
        algo = input("Choose algorithm. For random, enter 1. For find_nearest, enter 2.: ")

        if int(algo) == 1:
            randomgrid = randomgrid.Randomgrid(houses, batteries)
            all_houses, price = randomgrid.randomgrid

        else:
            pass

    elif int(section) == 2:
        algo = input("Choose algorithm. For manhattan, enter 1. For find_nearest, enter 2.")
        number_iterations = input("Enter number of iterations:  ")
        if int(algo) == 1:
            steps_back = input("Enter steps back: ")
            algomanhattan = algomanhattan.Closest_first(houses, batteries, int(number_iterations), int(steps_back))
            batteries, houses_connected, price = algomanhattan.closest_first

    else:
        print("Invalid input, run again.")


    # plot
    print("Total price:", price)
    if int(section) == 1:

        vis = random.Visual(all_houses, batteries.batteries)
        a,b,c,d = vis.get_values()
        vis.make_plot(a,b,c,d)

    elif int(section) == 2:
        manhattan.Visual(houses_connected, batteries)
