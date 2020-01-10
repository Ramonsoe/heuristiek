from .houses import Houses, Connected

class Battery(object):
    def __init__(self, x, y, capacity):
        self.x_battery = int(x)
        self.y_battery = int(y)
        self.capacity = float(capacity)
        self.spare_capacity = float(capacity)
        self.houses = []
        self.cables = []

    def __repr__(self):
        return f"({self.x_battery},{self.y_battery})"

    def add_house(self, house):

        self.houses.append(house)
        Houses.
        Connected.connected_house(house)
        

    def check_spare_capacity(self):

        return self.spare_capacity

    def new_spare_capacity(self, output):

        spare_capacity = self.check_spare_capacity()
        self.spare_capacity = spare_capacity - output.output
