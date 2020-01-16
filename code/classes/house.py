from . import cables

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
        return f"({self.x_house}, {self.y_house}), output: {self.output}, connected: {self.connected} to {self.battery}"

    def connect_house(self, house, battery):
        self.connected = True
        self.battery = battery
        cable = cables.Cables(house, battery)
        self.distance_to_battery = cable.distance()

    def check_connection(self):
        return self.connected

    def add_cable(self, cable):

        self.cables.append(cable)
