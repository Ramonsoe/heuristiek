class Price():

    def __init__(self, houses, batteries):

        self.price_cables = self.price_cables(houses)
        self.price_batteries = self.price_bats(batteries)
        self.price_total = self.price_cables + self.price_batteries
        print(self.price_total)

    def price_bats(self, batteries):
        price_bats = 0
        for battery in batteries.batteries:
            price_bats += 5000

        return price_bats

    def price_cables(self, houses):

        price_cables = 0

        for house in houses:

            price_cables += 9 * (len(house.cables[0]) - 2)

        return price_cables
