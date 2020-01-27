from .cableslayla import Cables

class ConnectToBattery():
    """Creates different lists of cable coordinates from house to battery"""

    def __init__(self, house, houses):

        self.x = house.x
        self.y = house.y
        self.battery = house.battery
        self.house = house
        self.houses = houses
        self.cable = cableslayla.Cables(self.house, self.houses)

        self.run()

    def run(self):
        '''Start the process of placing cables'''
        self.get_sub_connections()
        find_nearest = self.find_nearest_connection()
        nearest = find_nearest[0]
        type = find_nearest[1]
        connection = find_nearest[2]
        self.cable.get_all_coordinates(nearest, type, connection)
        self.cable.add_cables_to_house()
        self.cable.make_cable_list()
        self.cable.make_objects()

    def find_nearest_connection(self):
        '''Find nearest point to connect to if connected to same battery'''

        # to make sure every distance is smaller, choose large distance
        smallest_distance = 1000
    
        for house in self.house.battery.houses:
            if self.house not in house.connected_houses and house not in self.house.connected_houses and house != self.house and house.connected == True:
                distance = self.cable.distance_to_point(house, 'house')
                
                if distance < smallest_distance:
                    smallest_distance = distance
                    nearest = house
                    type = 'house'
                    to_be_connected = house

                    # check cables connected to house as well
                    for cable in house.all_cable_segments:
                        distance = self.cable.distance_to_point(cable, 'cable')
                        if distance < smallest_distance:
                            smallest_distance = distance
                            nearest = cable
                            type = 'cable'
                            to_be_connected = house

        # check for direct connection to battery as well
        distance = self.cable.distance_to_point(self.house.battery, 'battery')
        if distance < smallest_distance:
            smallest_distance = distance
            nearest = self.house.battery

            # when house connects to a battery, the house itself is connected directly
            type = 'battery'
            to_be_connected = self.house.battery

        self.house.connected = True
        for house in self.house.connected_houses:
            house.connected = True

        return nearest, type, to_be_connected
    
    def get_sub_connections(self):

        connected = set()
        for house in self.houses:
            if house.connected == True:
                connected.update(house.connected_houses)
                # connected.append(house)
                # for subhouse in house.connected_houses:
                #     # subhouse.connected_houses.append(house)
                #     subhouse.connected = True
                #     for subsub in subhouse.connected_houses:
                #         subsub.connected = True

        for house in connected:
            house.connected = True
            for subhouse in house.connected_houses:
                subhouse.connected_houses.update(house.connected_houses)
                subhouse.connected = True
                for subsub in subhouse.connected_houses:
                    subsub.connected = True
                    # subsub.connected_houses.update(house.connected_houses)
                    subsub.connected_houses.update(subhouse.connected_houses)
                    for subsubsub in subsub.connected_houses:
                        subsubsub.connected = True
                        # subsubsub.connected_houses.update(house.connected_houses)
                        subsub.connected_houses.update(subsub.connected_houses)

                # connected.append(subhouse)
                # for subsub in subhouse.connected_houses:
                #     subsub.connected = True

        # print (len(connected))

        # connected = []
        # for list in self.house.battery.house_connections:
        #     for house in list:
        #         if house.connected == True:
        #             connected.extend(list)

        # for house in connected:
        #     house.connected = True

                


            