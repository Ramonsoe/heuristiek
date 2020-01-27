class House(object):
    def __init__(self, x, y, output):
        self.x = int(x)
        self.y = int(y)
        self.x_house = self.x
        self.y_house = self.y
        
        self.output = float(output)
        self.connected = False
        self.cables = []
        self.all_cable_segments = []
        self.connected_houses = set()
        self.battery = None

    def __repr__(self):
        return f"({self.x}, {self.y}), output: {self.output}, connected: {self.connected} to {self.battery}"

    def check_connection(self):
        return self.connected

    def add_cable(self, cable):
        self.cables.append(cable)
