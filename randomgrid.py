from batteries import Battery, Batteries
from houses import Houses
import random


class SmartGrid():

    def __init__(self):
        self.smartgrid = []

    # filename als attribuut? ivm meerdere wijken > of in houses / batteries juist
    def houses_to_battery(self):
        house = Houses()
        house_objects = house.parse_houses()
        batteries = Batteries()
        battery = batteries.read_batteries()
        # battery_objects = batteries.read_batteries()
        appended_houses = []
        print(battery)
        for house in house_objects:
            current_battery = random.choice(battery_objects)
            current_capacity = current_battery.capacity
            current_spare_capacity = current_capacity - sum(item['output'] for item in current_battery.houses)
            current_house = random.choice(house_objects)

            if current_house in appended_houses:
                break
            else:
                current_battery.houses.append(current_house)
                appended_houses.append(current_house)

if __name__ == "__main__":
    smart = SmartGrid()
    bat = Batteries()
    bat.read_batteries()
    house = Houses()
    house.parse_houses()
    # smart.houses_to_battery()
