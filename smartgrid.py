from batteries import Battery, Batteries
from houses import Houses

class SmartGrid():

    def __init__(self):
        self.smartgrid = []

    # filename als attribuut? ivm meerdere wijken > of in houses / batteries juist
    def houses_to_battery(self): 
        house = Houses()
        house_objects = house.parse_houses()
        batteries = Batteries()
        battery_objects = batteries.read_batteries()
        i = 0 
        for battery in battery_objects:
            battery_houses = []
           
            cap = battery.spare_capacity
            out = house_objects[i].output

            while cap - out > 0:
                cap = cap - out
                battery_houses.append(house_objects[i])
                i += 1
            
            else:
                battery.houses = battery_houses
                i += 1
                

if __name__ == "__main__":
    smart = SmartGrid()
    bat = Batteries()
    bat.read_batteries()
    house = Houses()
    house.parse_houses()
    smart.houses_to_battery()