"""
houses.py

Layla Hoogeveen, Leon Brakkee and Ramon Soesan

File in which house objects are created.
"""


class House(object):


    def __init__(self, x, y, output):
        self.x = int(x)
        self.y = int(y)
        self.output = float(output)
        self.connected = False
        self.cables = []
        self.battery = None
        self.distance_to_battery = None
        self.connected_houses = set()

    def __repr__(self):
        return f"({self.x}, {self.y}), output: {self.output}, connected: {self.connected} to {self.battery}, distance is {self.distance_to_battery}"


    def connect_house(self, house, battery):
        """Connect house to battery"""

        self.connected = True
        self.battery = battery
        x_battery = battery.x
        y_battery = battery.y
        x_house = house.x
        y_house = house.y
        self.distance_to_battery = abs(x_battery - x_house) + abs(y_house - y_battery )


    def check_connection(self):
        """Check whether a house is connected"""

        return self.connected


    def disconnect(self):
        """Disconnect house from current battery"""

        self.connected = False
        self.battery = None
        self.distance_to_battery = None
        self.cables = []


    def add_cable(self, cable):
        """Add a cable to house"""

        self.cables.append(cable)
