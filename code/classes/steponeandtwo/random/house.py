"""
houses.py

Layla Hoogeveen, Leon Brakkee and Ramon Soesan

File where house objects are created.
"""


class House(object):
    def __init__(self, x, y, output):
        self.x_house = int(x)
        self.y_house = int(y)
        self.output = float(output)
        self.connected = False
        self.cables = []
        self.battery = None
        self.distance_to_battery = None


    def __repr__(self):
        return f"({self.x_house}, {self.y_house}), output: {self.output}, connected: {self.connected} to {self.battery}, distance is {self.distance_to_battery}"


    def connect_house(self, house, battery):
        self.connected = True
        self.battery = battery
        x_battery = battery.x_battery
        y_battery = battery.y_battery
        x_house = house.x_house
        y_house = house.y_house
        self.distance_to_battery = abs(x_battery - x_house) + abs(y_house - y_battery )


    def check_connection(self):
        return self.connected


    def add_cable(self, cable):

        self.cables.append(cable)
