from . import powersource

from . import battery
from .battery import Battery
# from exceptions import ExplicitException

class Powersources():

    def __init__(self, newsources):

        self.powersources = self.add_powersource(newsources)
        self.powersource_objects = []

    def add_powersource(self, newsources):
        """add objects to powersource list"""
        for newsource in newsources:

            try:
                for battery in newsource.batteries:
                    print(battery)
                    newsource = powersource.Powersource(battery)
                    print(newsource.x_power)
                    self.powersource_objects.append(newsource)
            except:
                pass
                print("orieb")

            try:
                for house in newsource.houses:
                    print(house)
                    newsource = powersource.Powersource(newsource[i])
                    self.powersource_objects.append(newsource)
            except:
                print("orieb")
                pass
            try:
                for i in range(len(newsource)):
                    newsource = Powersource(newsource[i])
                    self.powersource_objects.append(newsource)
            except:
                print("orieb")
                pass
        # return self.powersource_objects

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
