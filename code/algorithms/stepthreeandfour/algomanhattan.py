"""
algomanhattan.py

Layla Hoogeveen, Leon Brakkee and Ramon Soesan

Algorithms based on the manhattan distance: find the closest connection from a house to a powersource and try to connect.
"""


from code.classes.stepthreeandfour.manhattan import functions
from code.classes.standardobjects import cablepoints
import copy
import random


class Closest_first():
    """algorithm based on making the shortest possible connection untill all houses are divided over the batteries"""

    def __init__(self, houses, batteries, number_iterations, steps_back):

        # initialize the minimal capacity when a battery has to be left out of the list of powersources
        self.min_capacity = functions.minimal_output(houses) - 5

        # initialize a list with powersources
        self.powerlist = functions.add_powersource([batteries])

        # save the initial powerlist
        self.initial_powerlist = functions.copy_list(self.powerlist)

        # run the algorithm
        self.closest_first = self.run(houses, self.powerlist, batteries, self.min_capacity, number_iterations, steps_back)


    def run(self, houses, powersources, batteries, min_capacity, number_iterations, steps_back):
        """function where an algorithms, based on shortest manhattan distance from a powersource to a house"""

        # initialize the run counter
        run = 0

        # set the init price very high (higher than the upper bound), so the price will always be adjusted if a silution is found
        price_init = 10000000000000000000

        # keep track if the gross price to be able to calculate the average price
        gross_price = 0

        # keep the algorithmn running until the right amount of solutions is found
        while run < number_iterations:

            # initialize a list with houses to use as input
            houses_list = functions.copy_list(houses.houses_unconnected)

            count = 0

            # keep looking for a solution while not all houses are connected and it is tried less than 10000 times to find a solution
            while len(houses.houses_unconnected) > 0 and count < 10000:

                # make sure that there are objects in the list of powersources
                if len(self.powerlist) == 0:
                    break

                # find the closest distance between a house and a powersource
                closest_house, current_powersource = functions.get_closest_house(houses_list, self.powerlist)
                # connect the closest house to the powersource
                functions.connect_house_to_powersource(closest_house, current_powersource, houses, self.powerlist)

                # check if the house is connected, i.e. the output is lower than the capacity
                if closest_house.check_connection():

                    # place the cables
                    cable_power = cablepoints.Cablepoints()
                    cable_to_house = cable_power.place_cables(closest_house, current_powersource)

                    # append closest_house and all cables to powerlist
                    functions.append_powersource(self.powerlist, closest_house)
                    functions.append_cables(self.powerlist, cable_to_house)

                    # remove the house from the list of houses
                    functions.remove_house(closest_house, houses_list)

                    # check if current_powersource is still
                    functions.check_constraint(current_powersource, self.powerlist, min_capacity)

                    # take all unconnected houses as houses_list
                    houses_list = functions.copy_list(houses.houses_unconnected)

                    # start counting at 0 again
                    count = 0

                else:
                    # remove the closest house from the list to make sure that you dont look at the same house again
                    functions.remove_house(closest_house, houses_list)

                    # check if there are still houses in the list after previous line, if not, fill with random houses
                    functions.check_feasibility(houses_list, houses, self.powerlist, steps_back)

                    # increase count by one
                    count += 1

            # check if configuration was succesfull, if yes, stop the algorithm
            if len(houses.houses_unconnected) == 0:
                run += 1
                priceman = functions.calc_price(houses.houses_connected, batteries)

                # check if current price is lower than the lowest price
                if priceman.price_total < price_init:
                    price_init = priceman.price_total
                    best_solution = functions.copy_list(houses)

                gross_price = gross_price + priceman.price_total

                # set all data to the starting values before starting the algorithm again
                houses_list = functions.copy_list(houses.houses)
                functions.clear_powersources(self.powerlist)
                self.powerlist = functions.copy_list(self.initial_powerlist)
                houses.empty_connected()
                houses.fill_unconnected()

            # set all data to starting values before starting again
            else:
                houses_list = houses.copy_houses(houses.houses)
                functions.clear_powersources(self.powerlist)
                self.powerlist = copy.deepcopy(self.initial_powerlist)
                houses.empty_connected()
                houses.fill_unconnected()

        return batteries, best_solution, price_init
