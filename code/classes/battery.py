from houses import Connected

class Battery():
    def _init_(self, x, y, capacity):
        self.x_battery = int(x)
        self.y_battery = int(y)
        self.capacity = float(capacity)
        self.spare_capacity = float(capacity)
        self.houses = []
        self.cables = []

    def _repr_(self):
        return f"({self.x_battery},{self.y_battery})"


    def add_house(self, house):
        self.houses.append(house)

    def check_spare_capacity(self):
        return self.spare_capacity

    def new_spare_capacity(self, output):

        spare_capacity = self.check_spare_capacity()
        self.spare_capacity = spare_capacity - output.output