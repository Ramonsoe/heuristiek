from batteries import Battery, Batteries
from houses import Houses

house = Houses()
house_objects = house.parse_houses()

class SmartGrid():

    def __init__(self):
        self.smartgrid = []

    # bubble sort
    def sort_houses(self):
        swap = True
        while swap:
            swap = False
            for i in range(len(house_objects) - 1):
                if house_objects[i].output > house_objects[i + 1].output:
                    house_objects[i], house_objects[i + 1] = house_objects[i + 1], house_objects[i]
                    swap = True

    # filename als attribuut? ivm meerdere wijken > of in houses / batteries juist
    def houses_to_battery(self): 
        batteries = Batteries()
        battery_objects = batteries.read_batteries()
        i = 0 
        for battery in battery_objects:
            battery_houses = []
        
            cap = battery.spare_capacity
            out = house_objects[i].output
            if house_objects[i] not in battery_houses:
                battery_houses.append(house_objects[i])

            while cap - out > 0:
                cap = cap - out
                if house_objects[i] not in battery_houses:
                    battery_houses.append(house_objects[i])
                if i < (len(house_objects) - 1):
                    i += 1

            battery.houses = battery_houses

# if __name__ == "__main__":
#     smart = SmartGrid()
#     bat = Batteries()
#     bat.read_batteries()
#     house = Houses()
#     house.parse_houses()
#     smart.sort_houses()
#     smart.houses_to_battery()