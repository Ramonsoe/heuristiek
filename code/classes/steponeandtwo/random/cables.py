"""
cables.py

Layla Hoogeveen, Leon Brakkee and Ramon Soesan

File where cable objects are created and a list of cables is filled.
"""


from .battery import Battery
from .batteries import Battery
from .cable import Cable


class Cables():
    """Creates different lists of cable coordinates from house to battery"""

    def __init__(self, house, battery):

        self.x1 = house.x_house
        self.y1 = house.y_house
        self.x2 = battery.x_battery
        self.y2 = battery.y_battery

        self.cable_list = []
        self.cable_x = []
        self.cable_y = []

        # hierdoor hoef je alleen maar Cables aan te roepen als je kabels voor alle huizen wilt
        self.place_cables(house)


    def distance(self):
        """ Returns manhattan distance of two coordinates """

        distance = abs(self.x1 - self.x2) + abs(self.y1 - self.y2)
        return distance


    def add_cable_coords(self, X, Y):
        """This functie may be removed"""

        self.cable_x.append(X)
        self.cable_y.append(Y)


    def get_all_coordinates(self):
        """ Appends the x and y coordinates in separated lists for visualisation purposes """

        Xi, Yi = self.x1, self.y1
        Xf, Yf = self.x2, self.y2

        self.add_cable_coords(Xi, Yi)

        for i in range(self.distance()):

            if Xi < Xf:
                Xi += 1
                self.add_cable_coords(Xi, Yi)
                continue
            elif Xi > Xf:
                Xi -= 1
                self.add_cable_coords(Xi, Yi)
                continue

            if Yi < Yf:
                Yi += 1
                self.add_cable_coords(Xi, Yi)
                continue
            elif Yi > Yf:
                Yi -= 1
                self.add_cable_coords(Xi, Yi)

        return self.cable_x, self.cable_y


    def make_cable_list(self, list_x, list_y):
        """ Puts all the x and y coordinates in one list """

        for i in range(len(self.cable_x)):

            cable_points = [self.cable_x[i], self.cable_y[i]]
            self.cable_list.append(cable_points)
        return self.cable_list


    def connected_to_battery(self, battery):
        """ Deze functie moet gaan checken welke huizen al connected zijn """


    def which_battery(self):

        return self.battery


    def place_cables(self, house):

        X_segments, Y_segments = self.get_all_coordinates()

        house_to_battery_cable = self.make_cable_list(X_segments, Y_segments)

        house.add_cable(house_to_battery_cable)
