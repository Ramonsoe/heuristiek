from code.algorithms import randomgrid, areadivider
from code.classes import batteries, houses, randomgrid
from code.visualisation import vis

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

    randomgrid = randomgrid.Randomgrid(house, bat)

    all_houses = randomgrid.randomgrid

    vis = vis.Visual(all_houses, bat.batteries)

    a,b,c,d = vis.get_values()

    vis.make_plot(a,b,c,d)
