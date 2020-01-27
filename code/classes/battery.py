from .houses import Houses

class Battery(object):
    def __init__(self, x, y, capacity):
        self.x = int(x)
        self.y = int(y)
        self.x_battery = self.x
        self.y_battery = self.y
        self.capacity = float(capacity)
        self.spare_capacity = float(capacity)

        self.houses = []
        self.cables = []

    def __repr__(self):
        return f"({self.x},{self.y}, {self.spare_capacity})"

    def add_house(self, house):
        self.houses.append(house)

    def remove_house(self, house):
        self.houses.remove(house)

    def calc_spare_capacity(self):

        capacity_used = sum(house.output for house in self.houses)
        self.spare_capacity = self.capacity - capacity_used
        return self.spare_capacity

    def check_availability(self, house):

        if self.calc_spare_capacity() - house.output >= 0:
            return True
        return False