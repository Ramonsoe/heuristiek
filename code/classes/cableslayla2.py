from .battery import Battery
from .batteries import Battery
from .cablelayla import Cable
from .house import House
import copy

class Cables():
    """Creates different lists of cable coordinates from house to battery"""

    def __init__(self, house, connection):

        self.x = house.x
        self.y = house.y
        self.battery = house.battery
        self.house = house
        self.connection = connection

        self.cable_list = []
        self.cable_x = []
        self.cable_y = []
        self.cable_objects = []


        self.run()

    def run(self):
        '''Start the process of placing cables'''

        self.get_all_coordinates()
        self.add_cables_to_house()
        self.make_cable_list()
        self.make_objects()

    def distance(self, nearest_x, nearest_y):
        """Return Manhattan distance of two coordinates"""

        distance = abs(self.x - nearest_x) + abs(self.y - nearest_y)
        return distance


    def add_cable_coords(self, X, Y):
        """This functie may be removed"""

        self.cable_x.append(X)
        self.cable_y.append(Y)

    def get_all_coordinates(self):
        """Append x and y coordinates in separated lists for visualisation purposes"""

        Xi, Yi = self.x, self.y
        nearest = self.connection

        if hasattr(self.connection, 'x1'):

            # find nearest point of cable segment
            if (abs(self.x - nearest.x1) - abs(self.y - nearest.y1)) < (abs(self.x - nearest.x2) - abs(self.y - nearest.y2)):
                Xf = nearest.x1
                Yf = nearest.y1
            else:
                Xf = nearest.x2 
                Yf = nearest.y2

            # if nearest.x1 == nearest.x2:
            #     Xf = nearest.x1
            #     if (abs(self.y - nearest.y1) < abs(self.y - nearest.y1)):
            #         Yf = nearest.y1
            #     else:
            #         Yf = nearest.y2
            # elif nearest.y1 == nearest.y2:
            #     Yf = nearest.y1
            #     if (abs(self.x - nearest.x1) < abs(self.x - nearest.x1)):
            #         Xf = nearest.x1
            #     else:
            #         Xf = nearest.x2

        else:
            Xf, Yf = nearest.x, nearest.y
            
        self.add_cable_coords(Xi, Yi)

        for i in range(self.distance(Xf, Yf)):
            if Yi < Yf:
                Yi += 1
                self.add_cable_coords(Xi, Yi)
            elif Yi > Yf:
                Yi -= 1
                self.add_cable_coords(Xi, Yi)

            if Xi < Xf:
                Xi += 1
                self.add_cable_coords(Xi, Yi)
            elif Xi > Xf:
                Xi -= 1
                self.add_cable_coords(Xi, Yi)


    def make_cable_list(self):
        '''Put all x and y coordinates into one list'''

        for i in range(len(self.cable_x)):
            cable_points = [self.cable_x[i], self.cable_y[i]]
            self.cable_list.append(cable_points)
        
        self.house.cables = self.cable_list

        return self.cable_list

    def make_objects(self):
        '''Make objects out of all cable segments'''

        for start, end in zip(self.cable_list[0::2], self.cable_list[1::2]):
            if start[0] < start[1]:
                x1 = start[0]
                x2 = start[1]
            else:
                x1 = start[1]
                x2 = start[0]
            
            if end[0] < end[1]:
                y1 = end[0]
                y2 = end[1]
            else:
                y1 = end[1]
                y2 = end[0]
            cable = Cable(x1, x2, y1, y2, self.battery)

            self.cable_objects.append(cable)

    def add_cables_to_house(self):
        '''Add cable objects to house'''
        
        self.house.all_cable_segments = self.cable_objects