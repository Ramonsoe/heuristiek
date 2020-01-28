"""
battery.py

Layla Hoogeveen, Leon Brakkee and Ramon Soesan

File in which battery objects are created.
"""


class Battery(object):
    """battery object with attributes"""

    def __init__(self, x, y, capacity):
        self.x = int(x)
        self.y = int(y)
        self.capacity = float(capacity)
        self.spare_capacity = float(capacity)
        self.houses = []
        self.cables = []


    def __repr__(self):
        return f"({self.x},{self.y}, {self.spare_capacity})"


    def add_house(self, house):
        """Add house to list of connected houses"""

        self.houses.append(house)


    def remove_house(self, house):
        """Remove house from list of connected houses"""

        self.houses.remove(house)


    def restore_capacity(self, house):
        """Regain capacity when house is removed"""

        self.spare_capacity += house.output


    def calc_spare_capacity(self):
        """Calculate how much capacity is left"""

        capacity_used = sum(house.output for house in self.houses)
        spare_capacity = self.capacity - capacity_used

        return spare_capacity


    def check_availability(self, house):
        """Check whether a combination of house and battery is available"""

        if self.calc_spare_capacity() - house.output >= 0:
            return True
        return False


    def check_spare_capacity(self):
        """Return spare capacity"""

        return self.spare_capacity


    def new_spare_capacity(self, output):
        """Change spare capacity"""

        spare_capacity = self.check_spare_capacity()
        self.spare_capacity = spare_capacity - output.output
