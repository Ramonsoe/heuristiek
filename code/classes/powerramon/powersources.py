from . import powersource



class Powersources():

    def __init__(self):

        self.powersources = []

    def add_house_power(self, connected_houses):

        for house in connected_houses:
            powersource = Powersource(house)
            self.powersources.append(powersource)

    def add_bat_power(self, batteries):

        for battery in batteries.batteries:
            powersource = Powersource(battery)
            self.powersources.append(powersource)

    def add_cablepower(self, cablepoint):

        powersource = Powersource(cablepoint)
        self.powersources.append(powersource)

    def remove_powersources(self):
        """verwijder powersources van een volle batterij"""
        pass
        if battery == full:

            remove every house connected to this battery
            remove every cable connected to every house
            remove own battery coordinates
