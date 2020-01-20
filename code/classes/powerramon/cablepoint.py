class Cablepoint():


    def __init__(self, x, y, battery):

        self.x = x
        self.y = y

        self.battery = battery


    def __repr__(self):

        return f"|{self.x, self.y}, {self.battery}|"
