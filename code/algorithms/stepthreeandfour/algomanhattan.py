import sys
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, '/path/to/code/classes/powerramon')
from code.classes.powerramon import functions, cablepoints, price
# , batteries, houses, randomgrid, price, powersources, house
import copy
import random

class Closest_first():

    def __init__(self, houses, powersources, batteries, number_iterations):

        # initialize the minimal capacity when a battery has to be left out of the list of powersources
        self.min_capacity = functions.minimal_output(houses) - 5

        # initialize a list with powersources
        self.powerlist = functions.add_powersource(powersources)

        # save the initial powerlist
        self.initial_powerlist = copy.deepcopy(self.powerlist)

        # run the algorithm
        self.closest_first = self.run(houses, self.powerlist, batteries, self.min_capacity, number_iterations)

    def run(self, houses, powersources, batteries, min_capacity, number_iterations):
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
            houses_list = copy.deepcopy(houses.houses_unconnected)

            count = 0

            # keep looking for a solution while not all houses are connected and it is tried less than 10000 times to find a solution
            while len(houses.houses_unconnected) > 0 and count < 10000:

                # find the closest distance between a house and a powersource
                try:
                    closest_house, current_powersource = functions.get_closest_house(houses_list, self.powerlist)
                    # connect the closest house to the powersource
                    functions.connect_house_to_powersource(closest_house, current_powersource, houses, self.powerlist)

                    # check if the house is connected, i.e. the output is lower than the capacity
                    if closest_house.check_connection():

                        # place the cables
                        cable_power = cablepoints.Cablepoints()
                        cable_to_house = cable_power.place_cables(closest_house, current_powersource)

                        # append closest_house and all cables to powerlist
                        self.powerlist.append(closest_house)
                        for cable in cable_to_house:
                            self.powerlist.append(cable)

                        # remove the house from the list of houses
                        functions.remove_house(closest_house, houses_list)

                        # check if current_powersource is still
                        functions.check_constraint(current_powersource, self.powerlist, min_capacity)

                        # take all unconnected houses as houses_list
                        houses_list = copy.deepcopy(houses.houses_unconnected)

                        # start counting at 0 again
                        count = 0

                    else:
                        # remove the closest house from the list to make sure that you dont look at the same house again
                        houses_list.remove(closest_house)

                        # check if there are still houses in the list after previous line, if not, fill with random houses
                        functions.check_feasibility(houses_list, houses, self.powerlist)

                        # increase count by one
                        count += 1

                # if exception, reset data and start again
                except:
                    houses_list = houses.copy_houses(houses.houses)
                    functions.clear_powersources(self.powerlist)
                    self.powerlist = copy.deepcopy(self.initial_powerlist)
                    houses.empty_connected()
                    houses.fill_unconnected()




            # check if configuration was succesfull, if yes, stop the algorithm
            if len(houses.houses_unconnected) == 0:
                # print("succes")
                run += 1

                priceman = price.Price(houses.houses_connected, batteries)
                # print(priceman.price_total)
                if priceman.price_total < price_init:
                    price_init = priceman.price_total
                    best_solution = houses.copy_houses(houses)

                gross_price = gross_price + priceman.price_total
                houses_list = houses.copy_houses(houses.houses)
                functions.clear_powersources(self.powerlist)
                self.powerlist = copy.deepcopy(self.initial_powerlist)
                houses.empty_connected()
                houses.fill_unconnected()
                # print(run)


            # otherwise, set all data to starting values
            else:
                houses_list = houses.copy_houses(houses.houses)
                functions.clear_powersources(self.powerlist)
                self.powerlist = copy.deepcopy(self.initial_powerlist)
                houses.empty_connected()
                houses.fill_unconnected()
                print("failure")

        print(number_iterations)
        print(self.min_capacity)
        print(price_init)
        print("average:", gross_price/number_iterations)
        return houses.houses_connected, price_init

if __name__ == "__main__":

    neighbourhood = input("Enter neighbourhood (1, 2 or 3):  ")
    number_iterations = input("Enter number of iterations:  ")
    houses = houses.Houses(f"'data/wijk{neighbourhood}_huizen.csv'")
    batteries = batteries.Batteries(f"'data/wijk{neighbourhood}_batterijen.csv'")
