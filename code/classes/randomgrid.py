from code.algorithms import randomgrid

class Randomgrid():

    def __init__(self, houses, batteries):

        self.randomgrid = self.random_dist(houses, batteries)

    # algorithms
    def random_dist(self, houses, batteries):

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

                length_houses = len(houses_list)

                while count < 100 and len(houses_list) != 0:
                    # random huis
                    house1 = randomgrid.random_house(houses_list)

                    # voeg huis toe
                    randomgrid.connect_house_to_battery(house1, battery)


                    # verwijder huis van lijst
                    if house1.check_connection():
                        randomgrid.place_cables(house1, battery)
                        randomgrid.remove_house(house1, houses_list)

                    previous_length = length_houses
                    length_houses = len(houses_list)

                    # check if the house is connected
                    if previous_length == length_houses:
                        count += 1
                    else:
                        count = 0


            if len(houses_list) == 0:
                print("succes")

                # randomgrid.show_results(batteries)
                go_on = False

            else:
                houses_list = houses.copy_houses(houses.houses)
                randomgrid.clean_batteries(batteries)
                print("failure")
