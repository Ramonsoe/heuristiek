from code.classes.powerramon import functions, cablepoints

class Closest_first():

    def __init__(self, houses, powersources):

        self.closest_first = self.run(houses, powersources)

    def run(self, houses, powersources):

        houses_list = houses.copy_houses(houses.houses)

        count = 0

        while houses_list is not None and count < 10000000:

            closest_house, current_powersource = functions.get_closest_house(houses_list, powersources)
            print(">>>>>>>>", closest_house)
            functions.connect_house_to_powersource(closest_house, current_powersource, houses, powersources)

            if closest_house.check_connection():
                cable_power = cablepoints.Cablepoints()
                cable_to_house = cable_power.place_cables(closest_house, current_powersource)
                newpowersources = [closest_house, cable_to_house]
                functions.add_powersource(newpowersources)
                functions.remove_house(closest_house, houses_list)
                count = 0

            else:
                count += 1

        if houses_list is None:
            print("succes")
        else:
            houses_list = houses.copy_houses(houses.houses)
            functions.clear_powersources(powersources)
            houses.empty_connected()
            print("failure")
