from code.algorithms import randomgrid, areadivider, areadivider2
from code.classes import batteries, houses, randomgrid
# from code.visualisation import *

if __name__ == "__main__":

    bats1 = batteries.Batteries('data/wijk1_batterijen.csv')
    houses1 = houses.Houses('data/wijk1_huizen.csv')

    bats2 = batteries.Batteries('data/wijk2_batterijen.csv')
    houses2 = houses.Houses('data/wijk2_huizen.csv')

    bats3 = batteries.Batteries('data/wijk3_batterijen.csv')
    houses3 = houses.Houses('data/wijk3_huizen.csv')

    bat = batteries.Batteries('data/wijk1_batterijen.csv')
    house = houses.Houses('data/wijk1_huizen.csv')

    # areadivider = areadivider.AreaDivider(bats1, houses1)
    areadivider = areadivider2.AreaDivider(bats1, houses1)

    # randomgrid = randomgrid.Randomgrid(house, bat)
    
