from code.classes.powerramon import functions, cablepoints, price
import copy
import random

class Closest_first():

    def __init__(self, houses, powersources, batteries):

        self.powerlist = functions.add_powersource(powersources)
        self.initial_powerlist = copy.deepcopy(self.powerlist)
        self.closest_first = self.run(houses, self.powerlist, batteries)

    def run(self, houses, powersources, batteries):

        run = 0
        price_init = 10000000000000000000
        while run < 10:
            # print("gadoor")
            # print(self.powerlist)
            houses_list = copy.deepcopy(houses.houses_unconnected)
            count = 0

            while len(houses.houses_unconnected) > 0 and count < 10000:
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
                    self.powerlist.append(closest_house)
                    for cable in cable_to_house:
                        self.powerlist.append(cable)

                    # remove the house from the list of houses
                    functions.remove_house(closest_house, houses_list)

                    # check if current_powersource is still
                    functions.check_constraint(current_powersource, self.powerlist)

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

            # check if configuration was succesfull, if yes, stop the algorithm
            if len(houses.houses_unconnected) == 0:
                print("succes")
                run += 1

                priceman = price.Price(houses.houses_connected, batteries)
                print(priceman.price_total)
                if priceman.price_total < price_init:
                    price_init = priceman.price_total
                    
                houses_list = houses.copy_houses(houses.houses)
                functions.clear_powersources(self.powerlist)
                self.powerlist = copy.deepcopy(self.initial_powerlist)
                houses.empty_connected()
                houses.fill_unconnected()
                print(run)

            # otherwise, set all data to starting values
            else:
                houses_list = houses.copy_houses(houses.houses)
                functions.clear_powersources(self.powerlist)
                self.powerlist = copy.deepcopy(self.initial_powerlist)
                houses.empty_connected()
                houses.fill_unconnected()
                print("failure")

        return houses.houses_connected, price_init
    def __repr__(self):

        return f"{self.closest_first}"
