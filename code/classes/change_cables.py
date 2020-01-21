class FormatCables():

    def __init__(self, houses):
        self.houses = houses
        self.cables = []
        self.x = []
        self.y = []
        
        self.run()

    def run(self):
        self.remove_doubles()
        self.change_house_cables()
        # self.format()

    def remove_doubles(self):

        cable_objects = {}
        for house in self.houses:
            for cable in house.all_cable_segments:

                key = repr(cable)
                cable_objects[key] = cable

        self.cables = list(cable_objects.values()) 

    # def format(self):

    #     for cable in self.cables:

    #         x = [cable.x1, cable.x2]
    #         y = [cable.y1, cable.y2]

            
    #         self.x.append(x)
    #         self.y.append(y)

    #         # self.x.append[cable.x1, cable.xt]
    #         # self.x.append(cable.x2)
    #         # self.y.append(cable.y1)
    #         # self.y.append(cable.y2)

    def change_house_cables(self):

        for cable in self.cables:
            for house in self.houses:
                for house_cable in house.all_cable_segments:
                    if house_cable.x1 == cable.x1 and house_cable.x2 == cable.x2 and house_cable.y1 == cable.y1 and house_cable.y2 == cable.y2 and house_cable.battery == cable.battery:
                        house_cable = cable

    
