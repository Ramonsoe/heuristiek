from code.algorithms.steponeandtwo import randomgrid
from code.algorithms.stepthreeandfour import algomanhattan, find_nearest
from code.classes.standardobjects import batteries, houses
from code.classes.output import output
from code.visualisation import random, manhattan

if __name__ == "__main__":

    # prompt user for neighbourhood
    neighbourhood = input("Enter neighbourhood (1, 2 or 3):  ")
    while int(neighbourhood) > 3 or int(neighbourhood) < 1 or neighbourhood is None:
        neighbourhood = input("Enter neighbourhood (1, 2 or 3):  ")

    # load houses and batteries
    houses = houses.Houses(f'data/wijk{neighbourhood}_huizen.csv')
    batteries = batteries.Batteries(f'data/wijk{neighbourhood}_batterijen.csv')

    section = input("With cable overlap, enter 1. Without cable overlap, enter 2: ")
    while int(section) < 1 or int(section) > 2 or section is None:
        section = input("With cable overlap, enter 1. Without cable overlap, enter 2: ")

    if int(section) == 1:
        randomgrid = randomgrid.Randomgrid(houses, batteries)
        batteries, all_houses, price = randomgrid.randomgrid

    elif int(section) == 2:

        algo = input("Choose algorithm. For algomanhattan, enter 1. For find_nearest, enter 2: ")
        while int(algo) < 1 or int(algo) > 2 or int(algo) is None:
            algo = input("Choose algorithm. For algomanhattan, enter 1. For find_nearest, enter 2: ")

        number_iterations = input("Enter number of iterations:  ")
        while int(number_iterations) <= 0:
            number_iterations = input("Enter number of iterations:  ")

        if int(algo) == 1:
            steps_back = input("Enter steps back: ")
            algomanhattan = algomanhattan.Closest_first(houses, batteries, int(number_iterations), int(steps_back))
            batteries, houses_connected, price = algomanhattan.closest_first

        elif int(algo) == 2:
            find = find_nearest.FindNearest(batteries, houses)
            find.run(int(number_iterations))
            houses_connected, batteries, price = find.output()

        else:
            pass
    else:
        print("Invalid input, run again.")


    # plot
    print("Minimum price found price:", price)

    if int(section) == 1:

        vis = random.Visual(all_houses, batteries.batteries)
        a,b,c,d = vis.get_values()
        vis.make_plot(a,b,c,d)

    elif int(section) == 2:
        battery_outputs = output.Output(batteries)
        answer = input("View battery output? y/n: ")
        if answer.capitalize() == 'Y':
            battery_outputs.return_outputs()

        manhattan.Visual(houses_connected, batteries)
