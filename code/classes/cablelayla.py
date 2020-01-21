
class Cable(object):

    def __init__(self, x1, y1, x2, y2, battery):

        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.battery = battery

    def __repr__(self):

        return f"({self.x1},{self.y1}) to ({self.x2},{self.y2}) connected to {self.battery}"