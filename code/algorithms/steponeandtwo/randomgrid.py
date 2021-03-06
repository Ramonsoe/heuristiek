"""
randomgrid.py

Layla Hoogeveen, Leon Brakkee and Ramon Soesan

File in which the random algoritms of step one and two of the assigment is coded. This algorithms iterates over all batteries and
assigns the houses to them at random.
"""


from code.classes.steponeandtwo.random import functions
from code.classes.standardobjects import batteries, houses, price, cables
import csv


class Randomgrid():
    """Class in which the random solution is derived"""

    def __init__(self, houses, batteries):
        """Initialize the randomgrid"""

        self.randomgrid = self.random_dist(houses, batteries)


    def random_dist(self, houses, batteries):
        """Algorithm for the solution"""

        houses_list = houses.copy_houses(houses.houses)

        # boolean to check whether the algorithm has to continue or stop
        go_on = True

        while go_on:
            # fill battery by battery
            for battery in batteries.batteries:

                # initialize count
                count = 0

                # check if list with houses is not empty
                if houses_list is None:
                    exit()

                # keep iterating to fill the battery while there are houses left and it does not take too long
                while count < 100 and len(houses_list) != 0:

                    # random house
                    house1 = functions.random_house(houses_list)

                    # add house to battery
                    functions.connect_house_to_battery(house1, battery, houses, batteries)

                    # remove house from list of unconnected houses and place cables from house to battery
                    if house1.check_connection():

                        # place cables
                        cables.Cables(house1, battery)
                        functions.remove_house(house1, houses_list)
                        count = 0

                    else:
                        count += 1

            # check if succes or failure
            if len(houses_list) == 0:
                go_on = False
                pricerandom = price.Price(houses.houses_connected, batteries)
                return batteries, houses.houses_connected, pricerandom.price_total

            else:
                # make sure the algorithm starts with the correct lists
                houses_list = houses.copy_houses(houses.houses)
                functions.clean_batteries(batteries)
                houses.empty_connected()
