from code.algorithms import randomgrid

class Randomgrid():

    def __init__(self, houses, batteries):

        self.randomgrid = self.random_dist(houses, batteries)

    # algorithms
    def random_dist(self, houses, batteries):

        go_on = True
        i = 0
        while i < 5:
            # print(len(houses.houses_copy))
            # fill battery by battery
            for battery in batteries.batteries:
                # print(battery)
                # print(f"eerste{len(houses.houses_copy)}")
                # print(len(houses.houses))
                count = 0

                if houses.houses_copy is None:
                    exit()

                length_houses = len(houses.houses_copy)

                while count < 100 and len(houses.houses_copy) != 0:
                    # random huis
                    house1 = randomgrid.random_house(houses.houses_copy)
                    # print(house1.output)
                    # voeg huis toe
                    randomgrid.connect_house_to_battery(house1, battery)

                    
                    # verwijder huis van lijst
                    if house1.check_connection():
                        houses.pop_house(house1)

                    previous_length = length_houses
                    length_houses = len(houses.houses_copy)
                    if previous_length == length_houses:
                        count += 1
                    else:
                        count = 0

                # print(len(battery.houses))
                # print(go_on)

            if len(houses.houses_copy) == 0:
                print("succes")
                houses.houses_copy = houses.houses
                go_on = False
                i += 1

            else:
                houses.houses_copy = houses.houses
                # print(len(houses.houses))
                # print("nieuwe", len(houses.houses_copy))
                i += 1
                # print(">>>>>>failure")
