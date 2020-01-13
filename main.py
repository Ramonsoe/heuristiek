from code.algorithms import randomgrid
from code.classes import batteries, houses, randomgrid
# from code.visualisation import *

if __name__ == "__main__":

    bat = batteries.Batteries('data/wijk1_batterijen.csv')
    house = houses.Houses('data/wijk1_huizen.csv')

    randomgrid = randomgrid.Randomgrid(house, bat)
    
