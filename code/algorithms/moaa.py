import random
from . import formulas
from code.classes.powerleon import points, powersources, powersource
# from code.classes import batteries, houses
# from . import functions

class Smartcable():

    def __init__(self, houses, batteries):

        self.unconnected_houses = houses.houses

        self.batteries = batteries.batteries
        # self.smartcable = self.run(houses)
    def run(self, houses):

        # begin bij random battery
        battery = formulas.random_battery(self.batteries)
        print("HOIHOI", self.batteries)

        # vind het dichtsbijzijnde huis en bijbehorende kabelpunt om connectie te maken
        calculate = points.Points()
        house, cablepoint = calculate.calculate_near(self.unconnected_houses, self.batteries[battery])
        # if house.output < battery.spare_capacity:
        # of via een functie checken?
        formulas.connect_house_to_battery(battery, house, houses)   # verbind huis

        if house.check_connection():                                # check of huis verbonden is
            # maak kabels aan
            connecting = points.Connect(house, cablepoint)

            # Update de coordinaten lijst
            print(batteries.batteries[battery])

        else: # BATTERY IS FULL OR THERE IS NO NEW HOUSE
            pass
            # clear alle kabels en diens batterij
                # Mocht batterij vol zitten, verwijder alles uit PS lijst
