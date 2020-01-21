
class Price():

    def __init__(self, houses, batteries):

        self.price_cables = self.price_cables(houses)
        self.price_batteries = self.price_bats(batteries)
        self.price_total = self.price_cables + self.price_batteries
        self.cable_objects = []

    def price_bats(self, batteries):
        price_bats = 0

        for battery in batteries:
            price_bats += 5000

        return price_bats

    def price_cables(self, houses):
        '''Returns price of all cables and removes double prices'''

        price_cables = 0
        cable_objects = {}

        for house in houses:

            for cable in house.all_cable_segments:

                key = repr(cable)
                cable_objects[key] = cable

        price_cables = 9 * (len(cable_objects))
        self.cable_objects = list(cable_objects.values()) 

        # print (price_cables)

        return price_cables

    def total_price(self):

        total_price = self.price_batteries + self.price_cables
        return total_price

    def cables(self):
        
        return self.cable_objects
