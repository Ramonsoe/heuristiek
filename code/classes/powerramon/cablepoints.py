from .cablepoint import Cablepoint

class Cablepoints():

    def __init__(self, house, battery):

        self.x1 = house.x
        self.y1 = house.y
        self.x2 = battery.x
        self.y2 = battery.y
        self.battery = battery

        self.cable_list = []
        self.cable_x = []
        self.cable_y = []

        self.cable_objects = []
        # self.add_cable()

        # hierdoor hoef je alleen maar Cables aan te roepen als je kabels voor alle huizen wilt
        self.place_cables(house)


    def distance(self):
        """ Returns manhattan distance of two coordinates """

        distance = abs(self.x1 - self.x2) + abs(self.y1 - self.y2)
        return distance

    def add_cable_coords(self, x, y):
        """This functie may be removed"""

        self.cable_x.append(x)
        self.cable_y.append(y)

    def get_all_coordinates(self):
        """ Appends the x and y coordinates in separated lists for visualisation purposes """

        Xi, Yi = self.x1, self.y1
        Xf, Yf = self.x2, self.y2

        for i in range(self.distance() - 1):

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


    def make_cable_list(self):
        """ Puts all the x and y coordinates in one list """

        for i in range(len(self.cable_x)):
            cablepoints = Cablepoint(self.cable_x[i], self.cable_y[i], self.battery)
            # cable_points = [self.cable_x[i], self.cable_y[i], self.battery]
            self.cable_list.append(cablepoints)

        return self.cable_list

    def connected_to_battery(self, battery):
        """ Deze functie moet gaan checken welke huizen al connected zijn """


    def which_battery(self):

        return self.battery

    def place_cables(self, house):

        self.get_all_coordinates()

        house_to_battery_cable = self.make_cable_list()

        house.add_cable(house_to_battery_cable)
