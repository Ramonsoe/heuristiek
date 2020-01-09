import csv
from .battery import Battery

class Batteries():

    def __init__(self, battery_file):
        self.batteries = self.load_batteries(battery_file)

    def load_batteries(self, battery_file):
        battery_objects = []
        with open(battery_file, "r") as csv_file:
            reader = csv.reader(csv_file)
            batteries = list(reader)
            batteries.pop(0)

            for b in batteries:
                xy = b[0]
                xy = xy.strip('[]')
                xy = xy.split(", ")
                capacity = b[1].strip(' ')
                battery = Battery(xy[0], xy[1], capacity)
                battery_objects.append(battery)

        print (battery_objects)
        return battery_objects

