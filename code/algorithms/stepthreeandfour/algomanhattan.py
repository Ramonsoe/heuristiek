from code.classes.powerramon import functions, cablepoints
import copy

class Closest_first():

    def __init__(self, houses, powersources, batteries):


        self.powerlist = functions.add_powersource(powersources)
        self.closest_first = self.run(houses, self.powerlist, batteries)

    def run(self, houses, powersources, batteries):

        go_on = True
        # while go_on:
        # print(len(powersources))
        houses_list = copy.deepcopy(houses.houses_unconnected)
        count = 0

        while len(houses_list) > 0 and count < 1000:
            # print(batteries.batteries)
            closest_house, current_powersource = functions.get_closest_house(houses_list, self.powerlist)
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
                houses_list = copy.deepcopy(houses.houses_unconnected)
                count = 0
                # print("unconnected", len(houses.houses_unconnected))
                print(len(houses.houses_connected))
                # print("jhouselist", len(houses_list))
            else:
                houses_list.remove(closest_house)
                # print(">>",len(houses_list))
                count += 1

        if houses_list is None:
            print("succes")
            go_on = False
        else:
            houses_list = houses.copy_houses(houses.houses)
            functions.clear_powersources(self.powerlist)
            functions.add_powersource(batteries.batteries)
            # houses.empty_connected()
            # print(batteries.batteries)
            # print(len(houses.houses_unconnected))
            # print(len(self.powerlist))
            # print("failure")
            
            return houses.houses_connected
