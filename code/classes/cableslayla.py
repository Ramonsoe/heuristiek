from .battery import Battery
from .batteries import Battery
from .cablelayla import Cable
from .house import House
import copy

class Cables():
    """Creates different lists of cable coordinates from house to battery"""

    def __init__(self, house, houses):

        self.x = house.x
        self.y = house.y
        self.battery = house.battery
        self.house = house

        self.cable_list = []
        self.cable_x = []
        self.cable_y = []
        self.cable_objects = []
        self.nearest = None
        self.nearest_type = None

        self.houses = houses

        self.run()

    def run(self):
        '''Start the process of placing cables'''

        # self.get_sub_connections()
        find_nearest = self.find_nearest_point()
        nearest = find_nearest[0]
        type = find_nearest[1]
        connection = find_nearest[2]
        self.get_all_coordinates(nearest, type, connection)
        self.add_cables_to_house()
        self.make_cable_list()
        self.make_objects()
        # print (self.house)

    def distance(self, nearest_x, nearest_y):
        """Return Manhattan distance of two coordinates"""

        distance = abs(self.x - nearest_x) + abs(self.y - nearest_y)
        return distance

    def add_cable_coords(self, X, Y):
        """This functie may be removed"""

        self.cable_x.append(X)
        self.cable_y.append(Y)

    def get_all_coordinates(self, nearest, type, to_be_connected):
        """Append x and y coordinates in separated lists for visualisation purposes"""

        Xi, Yi = self.x, self.y

        self.nearest_type = type
        self.nearest = to_be_connected

        if type == 'cable':

            # find nearest point of cable segment
            if (abs(self.x - nearest.x1) - abs(self.y - nearest.y1)) < (abs(self.x - nearest.x2) - abs(self.y - nearest.y2)):
                Xf = nearest.x1
                Yf = nearest.y1
            else:
                Xf = nearest.x2 
                Yf = nearest.y2

        else:
            Xf, Yf = nearest.x, nearest.y

        # add the connected house to list of connected houses
        if type == 'house' or type == 'cable':
            self.house.connected_houses.add(to_be_connected)
            to_be_connected.connected_houses.add(self.house)
            to_be_connected.connected_houses.update(self.house.connected_houses)
            for house in to_be_connected.connected_houses:
                house.connected_houses.add(self.house)
                house.connected_houses.update(to_be_connected.connected_houses)
            for house in house.connected_houses:
                house.connected_houses.add(self.house)
                house.connected_houses.update(to_be_connected.connected_houses)
            
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
            cable = Cable(start[0], start[1], end[0], end[1], self.battery)

            self.cable_objects.append(cable)


    def find_nearest_point(self):
        '''Find nearest point to connect to if connected to same battery'''

        # to make sure every distance is smaller, choose large distance
        smallest_distance = 1000
    
        for house in self.house.battery.houses:

            # if self.house not in house.connected_houses:
                
            distance = self.distance_to_point(house, 'house')
            
            if distance < smallest_distance and house != self.house and self.house not in house.connected_houses and house.connected == True:
                smallest_distance = distance
                nearest = house
                type = 'house'
                to_be_connected = house

                # check cables connected to house as well
                for cable in house.all_cable_segments:
                    distance = self.distance_to_point(cable, 'cable')
                    if distance < smallest_distance:
                        smallest_distance = distance
                        nearest = cable
                        type = 'cable'
                        to_be_connected = house

        # check for direct connection to battery as well
        distance = self.distance_to_point(self.house.battery, 'battery')
        if distance < smallest_distance:
            smallest_distance = distance
            nearest = self.house.battery

            # when house connects to a battery, the house itself is connected directly
            self.house.connected = True
            type = 'battery'
            to_be_connected = self.house.battery

        # types needed for comparison with x and y, but cable object had other attributes
        if type == 'cable' or type == 'house':
            if to_be_connected.connected == True:
                self.house.connected = True

        # house must be connected directly to battery 
        else:
            self.house.connected = True

        return nearest, type, to_be_connected


    def distance_to_point(self, point, type):
        '''Return Manhattan distance of two coordinates'''

        if type == 'battery' or type == 'house':
            distance = abs(self.x - point.x) + abs(self.y - point.y)
            return distance

        if type == 'cable':
            distance = abs(self.x - (point.x1 + point.x2) / 2) + abs(self.y - (point.y1 + point.y2) / 2)
            return distance


    def add_cables_to_house(self):
        '''Add cable objects to house'''
        
        self.house.all_cable_segments = self.cable_objects        
            
    def get_sub_connections(self):

        connected = set()
        for house in self.houses:
            if house.connected == True:
                connected.update(house.connected_houses)

        for house in connected:
            house.connected = True
            for subhouse in house.connected_houses:
                subhouse.connected_houses.update(house.connected_houses)
                subhouse.connected = True
                for subsub in subhouse.connected_houses:
                    subsub.connected = True
                    subsub.connected_houses.update(subhouse.connected_houses)
                    # for subsubsub in subsub.connected_houses:
                    #     subsubsub.connected = True
                        # subsubsub.connected_houses.update(house.connected_houses)
                        # subsub.connected_houses.update(subsub.connected_houses)

    def return_nearest(self):

        return self.nearest