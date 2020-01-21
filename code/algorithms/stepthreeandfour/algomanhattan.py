from code.classes.powerramon import functions, cablepoints

class Closest_first():

    def __init__(self, houses, powersources):


        self.powerlist = functions.add_powersource(powersources)
        self.closest_first = self.run(houses, self.powerlist)

    def run(self, houses, powersources):

        houses_list = houses.copy_houses(houses.houses)
        count = 0

        while houses_list is not None and count < 100:
            # print(len(self.powerlist))
            closest_house, current_powersource = functions.get_closest_house(houses_list, self.powerlist)
            # print(current_powersource)
            functions.connect_house_to_powersource(closest_house, current_powersource, houses, self.powerlist)

            if closest_house.check_connection():
                cable_power = cablepoints.Cablepoints()
                cable_to_house = cable_power.place_cables(closest_house, current_powersource)
                # newhouse = [closest_house, cable_to_house]
                # newsources = functions.add_powersource(newpowersources)
                self.powerlist.append(closest_house)
                for cable in cable_to_house:
                    self.powerlist.append(cable)
                functions.remove_house(closest_house, houses_list)
                functions.check_constraint(current_powersource, self.powerlist)
                count = 0
            else:
                count += 1

        if houses_list is None:
            print("succes")
        else:
            houses_list = houses.copy_houses(houses.houses)
            print(len(houses.houses_connected))
            # print(self.powerlist)
            functions.clear_powersources(self.powerlist)
            houses.empty_connected()
            print("failure")
