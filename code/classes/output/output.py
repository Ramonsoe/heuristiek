"""
Return all information of batteries, including connected houses, (spare) capacity and location
"""


import pprint


class Output:

    def __init__(self, batteries):

        self.batteries = batteries.batteries
        self.outputs = []

        self.convert()

    def convert(self):
        '''Convert information of all batteries to dictionary'''

        for battery in self.batteries:
            info = {}
            info['location'] = battery.x, battery.y
            info['capacity'] = battery.capacity
            houses = []

            for house in battery.houses:
                house_info = {}
                house_info['location'] = house.x, house.y
                house_info['output'] = house.output
                cables = []
                for cable in house.cables[0]:
                    cable_coords = cable.x, cable.y
                    cables.append(cable_coords)

                house_info['cables'] = cables
                houses.append(house_info)

            info['houses'] = houses
            self.outputs.append(info)

    def return_outputs(self):
        """Return output of all batteries"""

        pprint.pprint(self.outputs)
