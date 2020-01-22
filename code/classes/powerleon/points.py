
class Points():
    """returns the nearest house for given coordinates corresponding to the battery"""

    def __init__(self):


        # self.calculate_near(unconnected_houses, battery_cbpoints)
        self.house_distances = {}

    def calculate_near(self, unconnected_houses, battery_cablepoints):
        """check per unc. huis alle kabelpunten in de batterij, returns huis met minste dist"""
        """ Deze functie nog omschrijven voor een hele volle batterij (met veel values)"""

        man_dist = {}
        # print(battery_cablepoints)
        # print(battery_cablepoints[0], battery_cablepoints[1])
        # for cablepoint in battery_cablepoints:

        for house in unconnected_houses:

            distance = abs(house.x - battery_cablepoints[0]) + abs(house.y - battery_cablepoints[1])

            # put every house in a dict with it's distance
            man_dist[(house)] = distance

        # get the nearest house
        nearby_house = min(man_dist, key=man_dist.get)

        # print(man_dist[nearby_house])
        # print(nearby_house)
        # print(battery_cablepoints)

        # return the house and it's nearest cablepoint
        return nearby_house, battery_cablepoints


class Connect():
    """Draws cables from a house to a certain point"""

    def __init__(self, house, battery_cablepoint):

        self.connect_line = []

        self.get_cablepoint(house, battery_cablepoint)

    def distance(self, house, battery_cablepoint):
        """ Returns manhattan distance of two coordinates """

        distance = abs(house.x - battery_cablepoint[0]) + abs(self.y1 - battery_cablepoint[1])
        return distance

    def get_cablepoint(self, house, battery_cablepoint):
        """"Make object for every connection to a powersource"""


        Xi, Xf = house.x, battery_cablepoint[0]
        Yi, Yf = house.y, battery_cablepoint[1]

        for i in range(1, (self.distance(house, battery_cablepoint) - 1)):

            if Yi < Yf:
                Yi += 1

            elif Yi > Yf:
                Yi -= 1

            elif Xi < Xf:
                Xi += 1

            elif Xi > Xf:
                Xi -= 1

            cablepoint = Cablepoint(Xi, Yi)
            self.connect_line.append(cablepoint)
        print(self.connect_line)
