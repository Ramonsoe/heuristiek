import csv
from Huizen_Batterijen import *
from houses import Houses

class Battery():

    def __init__(self):
        self.batteries = []

    def read_batteries(self):
        with open("Huizen_Batterijen/wijk1_batterijen.csv", "r") as csv_file:
            reader = csv.reader(csv_file)
            batteries = list(reader)
            batteries.pop(0)
            
            for b in batteries:
                dict = {}
                dict['location'] = b[0]
                dict['capacity'] = b[1].strip(' ')
                dict['spare_capacity'] = dict['capacity']
                dict['houses'] = []

                self.batteries.append(dict)

            # print (self.batteries)
            return self.batteries

# class BatteryObject(object):

#     def __init__(location, capacity, houses):
#         self.battery = {}
#         self.location = 'yo'
#         self.capacity = 1507
#         self.houses = [] 
#         self.battery['location'] = 'test'
#         self.battery['capacity'] = 'test'
#         self.battery['houses'] = []

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
    bat = Battery()
    bat.read_batteries()
    