from .battery import Battery
from .batteries import Battery
from .cable import Cable


class Cables():
    """list van cables"""

    def __init__(self):

        self.battery = battery
        self.cable_list = []

    def add_cable(self, x1, y1, x2, y2):

        self.cable_list.append(Cable(x1, x2, y1, y2))

    def which_battery(self):

        return self.battery

    def connected_to_battery(self, battery):

        # get the last cable
        last_cable = self.cable_list[-1]

        # check whether last cable connects to battery
        if battery.battery_x == last_cable.x2 and battery.battery_y == last_cable.y2:
            return True
        return False
