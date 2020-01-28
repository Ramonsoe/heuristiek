from code.algorithms.stepthreeandfour import find_nearest
from code.classes.standardobjects import batteries, houses
from code.visualisation import manhattan

if __name__ == "__main__":

    neighbourhood = input("Enter neighbourhood (1, 2 or 3):  ")
    # number_iterations = input("Enter number of iterations:  ")
    # steps_back = input("Enter steps back: ")
    houses = houses.Houses(f'data/wijk{neighbourhood}_huizen.csv')
    batteries = batteries.Batteries(f'data/wijk{neighbourhood}_batterijen.csv')


    # running the algorithm
    n = 100 # number of runs

    find = find_nearest.FindNearest(batteries, houses)
    find.run(n)
    best_houses, best_batteries, best_price = find.output()
    print (best_price)


    # algomanhattan = randomgrid.Closest_first(houses, batteries, int(number_iterations), int(steps_back))
    # houses_connected, price, batteries = algomanhattan.closest_first

    manhattan.Visual(best_houses, best_batteries)
