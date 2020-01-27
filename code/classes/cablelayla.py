
class Cable(object):

    def __init__(self, x1, y1, x2, y2, battery):

        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.battery = battery

    def __hash__(self):
         return hash(self.battery)

    def __eq__(self, other):
        return (
            ((self.x1 == other.x1 and self.x2 == other.x2) or 
             (self.x1 == other.x2 and self.x2 == other.x1)) and 
            ((self.y1 == other.y1 and self.y2 == other.y2) or 
             (self.y1 == other.y2 and self.y2 == other.x1))
        )

    def __repr__(self):

        return f"({self.x1},{self.y1}) to ({self.x2},{self.y2}) connected to {self.battery}"