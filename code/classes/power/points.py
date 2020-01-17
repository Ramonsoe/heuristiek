

class Connectpoints():
    """VAN HUIS NAAR POWERSOURCE"""

    def __init__(self, house, powersource):

        self.x1 = house.x_house
        self.y1 = house.y_house

        self.x2 = powersource.x_power
        self.y2 = powersource.y_power

    def distance(self):
        """ Returns manhattan distance of two coordinates """

        distance = abs(self.x1 - self.x2) + abs(self.y1 - self.y2)
        return distance

    def get_cablepoint(self):
        """"Make object for every connection to a powersource"""


        Xi, Xf = self.x1, self.x2
        Yi, Yf = self.y1, self.y2


        for i in range(1, (self.distance() - 1)):

            if Yi < Yf:
                Yi += 1
                continue
            elif Yi > Yf:
                Yi -= 1
                continue

            if Xi < Xf:
                Xi += 1
                continue
            elif Xi > Xf:
                Xi -= 1

            cablepoint = Cablepoint(Xi, Yi)
