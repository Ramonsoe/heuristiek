import csv
from Huizen_Batterijen import *

class Read():

    def __init__(self):
        self.houses_results = []
        self.spare_houses = []
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
                dict['houses'] = []

                self.smartgrid.append(dict)
             

    def append_houses(self):
        houses = self.read_houses()
        index_battery = 0
        list = []
        self.smartgrid[index_battery]['houses'] = list
        for house in houses:
            output = house[2]
            current_battery = self.smartgrid[index_battery]
           
            spare_capacity = float(current_battery['spare_capacity']) - float(output)
            if (spare_capacity > 0):
                
                current_battery['spare_capacity'] = spare_capacity
                addhouse = {}
                x_coordinate = house[0]
                y_coordinate = house[1]
                addhouse['location'] = f"{x_coordinate, y_coordinate}"
                addhouse['output'] = output
                
                list.append(addhouse)
                self.smartgrid[index_battery]['houses'] = list
                
            else:
                # self.spare_houses.append(house)
                index_battery += 1
                list = []

                addhouse = {}
                x_coordinate = house[0]
                y_coordinate = house[1]
                addhouse['location'] = f"{x_coordinate, y_coordinate}"
                addhouse['output'] = output
                self.smartgrid[index_battery]['houses']
                list.append(addhouse)
                # return self.smartgrid

        print (self.smartgrid)
    
    def read_houses(self):
        with open("Huizen_Batterijen/wijk1_huizen.csv", "r") as csv_file:
            reader = csv.reader(csv_file)
            houses_results = list(reader)
            houses_results.pop(0)
        return houses_results

    def divide_spares(self):
        # for battery in self.smartgrid:
        
        current_battery = self.smartgrid[4]
        if current_battery['spare_capacity'] > 0:
            for house in self.spare_houses:
                poep = float(current_battery['spare_capacity'])
                plas = float(house[2])
                if poep - plas > 0:
                    current_battery['spare_capacity'] = poep - plas
                    # print (current_battery)
                    # current_battery['houses'] = house
                    house.clear()

        print (self.spare_houses)
        print (self.smartgrid[4])

if __name__ == "__main__":
    read = Read()
    read.read_batteries()
    read.read_houses()
    read.append_houses()
    read.divide_spares()