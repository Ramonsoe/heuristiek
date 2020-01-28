"""
powersource.py

Layla Hoogeveen, Leon Brakkee and Ramon Soesan

File where a list of powersources (batteries, connected houses and cables) are created.
"""


class Powersources():

    def __init__(self):

        self.powersources_objects = []


    def add_powersource(self, newsources):
        """add objects to powersource list"""

        for newsource in newsources:

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
