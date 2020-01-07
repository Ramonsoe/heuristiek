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

class Battery(object):

    def __init__(self, x, y, capacity):
        self.x_battery = x
        self.y_battery = y
        self.capacity = capacity
        self.houses = [] 

    def __str__(self):
        return f"{self.x_battery}"

#     def read_batteries(self):
#         with open("Huizen_Batterijen/wijk1_batterijen.csv", "r") as csv_file:
#             reader = csv.reader(csv_file)
#             batteries = list(reader)
#             batteries.pop(0)
            
#             for battery in batteries:
#                 dict = {}
#                 dict['location'] = batteries_results[i][0]
#                 dict['capacity'] = batteries_results[i][1].strip(' ')
#                 dict['spare_capacity'] = dict['capacity']
#                 dict['houses'] = []

#                 self.battery.append(dict)

if __name__ == "__main__":
    bat = Batteries()
    bat.read_batteries()
    