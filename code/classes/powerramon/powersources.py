from . import powersource, allpowersources
from.allpowersources import All_powersources
from . import battery
from .battery import Battery
# from exceptions import ExplicitException

class Powersources():

    def __init__(self):

        # self.powersources = self.add_powersource(newsources)
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
        # self.powersources_objects.append(powersource_objects)

        # print(aps.allpowersources)


    # def add_house_power(self, connected_houses):
    #
    #     for house in connected_houses:
    #         powersource = Powersource(house)
    #         self.powersources.append(powersource)
    #
    # def add_bat_power(self, batteries):
    #
    #     for battery in batteries.batteries:
    #         powersource = Powersource(battery)
    #         self.powersources.append(powersource)
    #
    # def add_cablepower(self, cablepoint):
    #
    #     powersource = Powersource(cablepoint)
    #     self.powersources.append(powersource)
    #
    # def remove_powersources(self):
    #     """verwijder powersources van een volle batterij"""
    #     pass
    #     if battery == full:
    #
    #         remove every house connected to this battery
    #         remove every cable connected to every house
    #         remove own battery coordinates
