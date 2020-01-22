from code.algorithms.stepthreeandfour import randomgrid, find_nearest, algomanhattan
from code.classes.powerramon import batteries, houses, randomgrid, price, powersources, cablepoints, house, allpowersources
# from code.visualisation import vis1

if __name__ == "__main__":

    # data load
    bats1 = batteries.Batteries('data/wijk1_batterijen.csv')
    houses1 = houses.Houses('data/wijk1_huizen.csv')

    bats2 = batteries.Batteries('data/wijk2_batterijen.csv')
    houses2 = houses.Houses('data/wijk2_huizen.csv')

    bats3 = batteries.Batteries('data/wijk3_batterijen.csv')
    houses3 = houses.Houses('data/wijk3_huizen.csv')

    batteries = batteries.Batteries('data/wijk1_batterijen.csv')
    houses = houses.Houses('data/wijk1_huizen.csv')

    # tests

    # areadivider = areadivider.AreaDivider(bats1, houses1)


    # print(len(cable.cable_list))
    newpowersources = [batteries]
    algomanhattan = algomanhattan.Closest_first(houses, newpowersources, batteries)
    pricemanhattan = price.Price(algomanhattan.closest_first, batteries)
    # powersourc = powersources.Powersources()
    # powersourc.add_powersource(newpowersources)
    # print(powersourc.powersources_objects[1].battery)



    # randomgrid = randomgrid.Randomgrid(houses, batteries)
    # pricerandom = price.Price(randomgrid.randomgrid, batteries)
    # print(randomgrid.randomgrid[0])
    # print(batteries.batteries[0].houses)
    # pricearea = price.Price(find_nearest.connected_houses, batteries)

    # all_houses = areadivider.connected_houses
    #
    # vis = vis.Visual(all_houses, bat.batteries)
    #
    # a,b,c,d = vis.get_values()
    #
    # vis.make_plot(a,b,c,d)
