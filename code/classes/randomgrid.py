from code.algorithms import randomgrid


class Randomgrid():
    """class where the random solution is derived"""

    def __init__(self, houses, batteries):
        """initialize the randomgrid"""

        self.randomgrid = self.random_dist(houses, batteries)

    # algorithms
    def random_dist(self, houses, batteries):
        """algorithm for the solution"""

        houses_list = houses.copy_houses(houses.houses)

        # boolean to check if the algorithm has to continue or stop
        go_on = True

        while go_on:
            # fill battery by battery
            for battery in batteries.batteries:

                # initialize count
                count = 0

                # check if list with houses is not empty
                if houses_list is None:
                    exit()

                # keep track of the length of the llist of houses
                # length_houses = len(houses_list)

                # keep looping to fill the battery while there are houses left and it does not take too long
                while count < 100 and len(houses_list) != 0:

                    # random huis
                    house1 = randomgrid.random_house(houses_list)

                    # voeg huis toe
                    randomgrid.connect_house_to_battery(house1, battery, houses, batteries)

                    # remove house from list of unconnected houses and place cables from house to battery
                    if house1.check_connection():
                        randomgrid.place_cables(house1, battery)
                        randomgrid.remove_house(house1, houses_list)
                        count = 0

                    else:
                        count += 1
                    # keep track of the previous length and get the updated length of list of unconnected houses
                    # previous_length = length_houses
                    # length_houses = len(houses_list)

                    # check if the house is connected
                    # if previous_length == length_houses:
                    #     count += 1
                    # else:
                    #     count = 0


            if len(houses_list) == 0:
                print("succes")
                go_on = False
                return houses.houses_connected
            else:
                houses_list = houses.copy_houses(houses.houses)
                randomgrid.clean_batteries(batteries)
                houses.empty_connected()
                print("failure")
