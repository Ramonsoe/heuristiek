class House(object):
    def __init__(self, x, y, output):
        self.x_house = int(x)
        self.y_house = int(y)
        self.output = float(output)
        self.connected = False


    def __repr__(self):
        return f"({self.x_house}, {self.y_house}), output: {self.output}, connected: {self.connected}"

    def connect_house(self):
        self.connected = True
        
    def check_connection(self):
        return self.connected

    # def total_connected_houses(self):
    #
    #     if self.connect_house() = True:
