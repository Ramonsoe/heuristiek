from code.algorithms.stepthreeandfour import algomanhattan
from code.classes.standardobjects import batteries, houses
from code.visualisation import manhattan

if __name__ == "__main__":

    neighbourhood = input("Enter neighbourhood (1, 2 or 3):  ")
    number_iterations = input("Enter number of iterations:  ")
    steps_back = input("Enter steps back: ")
    houses = houses.Houses(f'data/wijk{neighbourhood}_huizen.csv')
    batteries = batteries.Batteries(f'data/wijk{neighbourhood}_batterijen.csv')


    # running the algorithm
    algomanhattan = algomanhattan.Closest_first(houses, batteries, int(number_iterations), int(steps_back))
    houses_connected, price, batteries = algomanhattan.closest_first
    manhattan.Visual(houses_connected, batteries)
