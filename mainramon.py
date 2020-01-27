from code.algorithms.stepthreeandfour import randomgrid, find_nearest, algomanhattan
from code.classes.powerramon import batteries, houses, randomgrid, price, powersources, cablepoints, house, allpowersources
# from code.visualisation import vis1

if __name__ == "__main__":

    neighbourhood = input("Enter neighbourhood (1, 2 or 3):  ")
    number_iterations = input("Enter number of iterations:  ")
    steps_back = input("Enter steps back: ")
    houses = houses.Houses(f'data/wijk{neighbourhood}_huizen.csv')
    batteries = batteries.Batteries(f'data/wijk{neighbourhood}_batterijen.csv')

    
    # batteries = batteries.Batteries('data/wijk1_batterijen.csv')
    # houses = houses.Houses('data/wijk1_huizen.csv')

    # tests
    newpowersources = [batteries]
    algomanhattan = algomanhattan.Closest_first(houses, newpowersources, batteries, number_iterations, int(steps_back))
    # algomanhattan = algomanhattan.Closest_first(houses, newpowersources, batteries, 1, 20)
    # pricemanhattan = price.Price(algomanhattan.closest_first, batteries)
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
