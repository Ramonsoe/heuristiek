from .battery import Battery
from .batteries import Battery
from .cable import Cable


class Cables():
    """list van cables"""

    def __init__(self):

        self.battery = battery
        self.cable_list = []
        self.cable_x = []
        self.cable_y = []

    def add_cable(self, cable):

        cable = Cable(x1, y1, x2, y2)
        self.cable_list.append(cable)

    # def distance(self):
    #
    #     mdist = abs(self.x1 - self.x2) + abs(self.y1 - self.y2)
    #     return mdist

    def add_cable_coords(self, X, Y):

        self.cable_x.append(X)
        self.cable_y.append(Y)

        self.cable_list.append(X,Y)

    def get_all_coordinates(self, mdist):

        Xi, Yi = self.x1, self.y1
        Xf, Yf = self.x2, self.y2

        self.add_cable_coords(Xi, Yi)

        for i in range(mdist):

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


    def connected_to_battery(self, battery):

        # get the last cable
        last_cable = self.cable_list[-1]

        # check whether last cable connects to battery
        if battery.battery_x == last_cable.x2 and battery.battery_y == last_cable.y2:
            return True
        return False

    def which_battery(self):

        return self.battery
