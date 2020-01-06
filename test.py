import csv
from Huizen_Batterijen import *


class Read():

    def __init__(self):
        self.houses_results = []
        self.batteries_results = []
        self.smartgrid = []

    def read_batteries(self):
        with open("Huizen_Batterijen/wijk1_batterijen.csv", "r") as csv_file:
            reader = csv.reader(csv_file)
            batteries_results = list(reader)
            batteries_results.pop(0)
            
            for i in range(len(batteries_results)):
                dict = {}
                dict['location'] = batteries_results[i][0]
                dict['capacity'] = batteries_results[i][1].strip(' ')
                dict['spare_capacity'] = dict['capacity']
                


                self.smartgrid.append(dict)
             

    def append_houses(self):
        houses = self.read_houses()
        index_battery = 0
        # current_capacity = current_battery['capacity']
        list = []
        self.smartgrid[index_battery]['HH'] = list
        print(self.smartgrid[index_battery]['HH'])
        for house in houses:
            output = house[2]
            current_battery = self.smartgrid[index_battery]

            
            if (float(current_battery['spare_capacity']) - float(output) > 0):
                current_battery['spare_capacity'] = float(current_battery['spare_capacity']) - float(output)
                addhouse = {}
                x_coordinate = house[0]
                y_coordinate = house[1]
                addhouse['location'] = f"{x_coordinate, y_coordinate}"
                addhouse['output'] = output
                
                list.append(addhouse)
                self.smartgrid[index_battery]['HH'] = list
                print (len(list))
            else:
                index_battery += 1
                list = []
                # current_capacity = current_battery['capacity']


    
        # print(self.smartgrid)


    def read_houses(self):
        with open("Huizen_Batterijen/wijk1_huizen.csv", "r") as csv_file:
            reader = csv.reader(csv_file)
            houses_results = list(reader)
            houses_results.pop(0)
            # print (houses_results)
        return houses_results

if __name__ == "__main__":
    read = Read()
    read.read_batteries()
    read.read_houses()
    read.append_houses()