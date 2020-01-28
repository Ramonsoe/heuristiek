"""
cablepoints.py

Layla Hoogeveen, Leon Brakkee and Ramon Soesan

File where cablepoint are created and a list of all cablepoint is created.
"""


from .cablepoint import Cablepoint

class Cablepoints():

    def __init__(self):

        self.cable_list = []
        self.cable_x = []
        self.cable_y = []

        self.cable_objects = []

    def distance(self, house, battery):
        """ Returns manhattan distance of two coordinates """

        distance = abs(house.x - battery.x) + abs(house.y - battery.y)
        return distance

    def add_cable_coords(self, x, y):
        """This functie may be removed"""

        self.cable_x.append(x)
        self.cable_y.append(y)

    def get_all_coordinates(self, house, battery):
        """ Appends the x and y coordinates in separated lists for visualisation purposes """

        Xi, Yi = house.x, house.y
        Xf, Yf = battery.x, battery.y

        self.add_cable_coords(Xi, Yi)

        # places the cables step by step from origin to destination
        for i in range(self.distance(house, battery)):

            if Yi < Yf:
                Yi += 1
                self.add_cable_coords(Xi, Yi)
                continue
            elif Yi > Yf:
                Yi -= 1
                self.add_cable_coords(Xi, Yi)
                continue


            if Xi < Xf:
                Xi += 1
                self.add_cable_coords(Xi, Yi)
                continue
            elif Xi > Xf:
                Xi -= 1
                self.add_cable_coords(Xi, Yi)


    def make_cable_list(self, battery):
        """ Puts all the x and y coordinates in one list and create object of every cablepoint"""

        for i in range(len(self.cable_x)):
            cablepoint = Cablepoint(self.cable_x[i], self.cable_y[i], battery)
            self.cable_list.append(cablepoint)

        return self.cable_list


    def place_cables(self, house, battery):

        self.cable_x = []
        self.cable_y = []
        self.get_all_coordinates(house, battery)

        # try except because not all powerosurces are batteries, they can also be houses or cables
        try:
            battery.spare_capacity
            battery = battery
        except:
            pass

        try:
            battery = battery.battery
        except:
            pass

        house_to_battery_cable = self.make_cable_list(battery)
        house.add_cable(house_to_battery_cable)

        return self.cable_list
