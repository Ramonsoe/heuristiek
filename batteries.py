import csv
from Huizen_Batterijen import *
from houses import Houses

class Batteries():

    def __init__(self):
        self.batteries = []

    def read_batteries(self):
        with open("Huizen_Batterijen/wijk1_batterijen.csv", "r") as csv_file:
            reader = csv.reader(csv_file)
            self.batteries = list(reader)
            self.batteries.pop(0)
            
            for b in self.batteries:
                xy = b[0]
                xy = xy.strip('[]')
                xy = xy.split(", ")
                capacity = b[1].strip(' ')
                battery = Battery(xy[0], xy[1], capacity)
                # print (battery)

class Battery(object):

    def __init__(self, x, y, capacity):
        self.x_battery = x
        self.y_battery = y
        self.capacity = capacity
        self.houses = [] 

    def __str__(self):
        return f"x-coordinate: {self.x_battery}, y-coordinate: {self.y_battery}, capacity: {self.capacity}"

if __name__ == "__main__":
    bat = Batteries()
    bat.read_batteries()
    