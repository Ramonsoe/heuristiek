"""
powersource.py

Layla Hoogeveen, Leon Brakkee and Ramon Soesan

File in which a list of power sources (batteries, connected houses and cables) are created.
"""


class Powersources():

    def __init__(self):

        self.powersources_objects = []


    def add_powersource(self, newsources):
        """Add objects to power source list"""

        for newsource in newsources:

            # use try except because newsource can be a house, cable or battery; they have different attributes
            try:
                for battery in newsource.batteries:
                    self.powersources_objects.append(battery)
            except:
                pass

            try:
                newsource.distance_to_battery
                self.powersources_objects.append(house)
            except:
                pass

            try:
                for cable in newsource.cable_list:

                    self.powersources_objects.append(cable)
            except:
                pass

        return self.powersources_objects
