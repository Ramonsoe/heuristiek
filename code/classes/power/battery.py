
class Battery(object):
    def __init__(self, x, y, capacity):
        self.x = int(x)
        self.y = int(y)
        self.capacity = float(capacity)
        self.spare_capacity = float(capacity)
        self.houses = []
        self.cables = []

    def __repr__(self):
        return f"({self.x_battery},{self.y_battery}, {self.spare_capacity})"

    def add_house(self, house):
        self.houses.append(house)

    def remove_house(self, house):
        self.houses.remove(house)

    def calc_spare_capacity(self):

        capacity_used = sum(house.output for house in self.houses)
        spare_capacity = self.capacity - capacity_used

        return spare_capacity

    def check_spare_capacity(self):

        return self.spare_capacity

    def new_spare_capacity(self, output):

        spare_capacity = self.check_spare_capacity()
        self.spare_capacity = spare_capacity - output.output
