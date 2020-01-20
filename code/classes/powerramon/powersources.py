from . import powersource

from . import battery
from .battery import Battery
# from exceptions import ExplicitException

class Powersources():

    def __init__(self, newsources):

        self.powersources = self.add_powersource(newsources)
        # self.powersource_objects = []


    def add_powersource(self, newsources):
        """add objects to powersource list"""
        powersource_objects = []
        i = 0
        j = 0

        for newsource in newsources:
            i += 1
            print(i)

            try:
                for battery in newsource.batteries:
                    powersource_objects.append(battery)
            except:
                pass

            try:
                for house in newsource.houses_connected:
                    powersource_objects.append(house)
            except:
                pass

            try:
                for cable in newsource.cable_list:
                    powersource_objects.append(cable)
            except:
                pass
        return powersource_objects

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
