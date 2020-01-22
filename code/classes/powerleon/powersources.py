from . import powersource




class Powersources():

    def __init__(self):

        self.powersources = []

    def add_house_power(self, connected_houses):

        for house in connected_houses:
            ps = powersource.Powersource(house)
            self.powersources.append(ps)

    def add_bat_power(self, batteries):

        for battery in batteries.batteries:
            print(battery.x)
            ps = powersource.Powersource(battery)
            self.powersources.append(ps)

    def add_cablepower(self, cablepoint):

        ps = powersource.Powersource(cablepoint)
        self.powersources.append(ps)

    def remove_powersources(self):
        """verwijder powersources van een volle batterij"""
        pass
        # if battery == full:
        #
        #     remove every house connected to this battery
        #     remove every cable connected to every house
        #     remove own battery coordinates
