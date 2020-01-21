
class Price():

    def __init__(self, houses, batteries):

        self.houses = houses
        self.batteries = batteries
        self.total_price = 0
        
        self.run()

    def run(self):
        
        price_batteries = self.price_batteries()
        price_cables = self.price_cables()
        self.calc_total_price(price_batteries, price_cables)

    def price_batteries(self):
        price_bats = 0

        for battery in self.batteries:
            price_bats += 5000

        return price_bats

    def price_cables(self):
        '''Returns price of all cables and removes double prices'''

        unique_cables = set()

        for house in self.houses:
            for cable in house.all_cable_segments:
                unique_cables.add(cable)

        price = len(unique_cables) * 9
        return price

    def calc_total_price(self, batteries, cables):

        self.total_price = total_price = batteries + cables