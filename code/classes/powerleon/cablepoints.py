from .cablepoint import Cablepoint

class Cablepoints():
        """Cablepoints in powerleon trekt kabels niet per se naar batterijen maar naar de dichtsbijzijnde battery"""
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

        for i in range(self.distance(house, battery) - 1):

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
        """ Puts all the x and y coordinates in one list """

        for i in range(len(self.cable_x)):
            cablepoint = Cablepoint(self.cable_x[i], self.cable_y[i], battery)
            self.cable_list.append(cablepoint)
        # print(self.cable_list)
        return self.cable_list

    def connected_to_battery(self, battery):
        """ Deze functie moet gaan checken welke huizen al connected zijn """


    def which_battery(self):

        return self.battery

    def place_cables(self, house, battery):

        self.cable_x = []
        self.cable_y = []
        self.get_all_coordinates(house, battery)
        self.make_cable_list(battery)

        house_to_battery_cable = self.make_cable_list(battery)

        house.add_cable(house_to_battery_cable)
