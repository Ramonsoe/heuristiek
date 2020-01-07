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

            print (self.batteries)
             

    # def append_houses(self):
    #     houses = self.read_houses()
    #     index_battery = 0
    #     list = []
    #     self.smartgrid[index_battery]['houses'] = list
    #     for house in houses:
    #         output = house[2]
    #         current_battery = self.smartgrid[index_battery]
           
    #         spare_capacity = float(current_battery['spare_capacity']) - float(output)
    #         if (spare_capacity > 0):
                
    #             current_battery['spare_capacity'] = spare_capacity
    #             addhouse = {}
    #             x_coordinate = house[0]
    #             y_coordinate = house[1]
    #             addhouse['location'] = f"{x_coordinate, y_coordinate}"
    #             addhouse['output'] = output
                
    #             list.append(addhouse)
    #             self.smartgrid[index_battery]['houses'] = list
                
    #         else:
    #             # self.spare_houses.append(house)
    #             index_battery += 1
    #             list = []

    #             addhouse = {}
    #             x_coordinate = house[0]
    #             y_coordinate = house[1]
    #             addhouse['location'] = f"{x_coordinate, y_coordinate}"
    #             addhouse['output'] = output
    #             self.smartgrid[index_battery]['houses']
    #             list.append(addhouse)
    #             # return self.smartgrid

    #     print (self.smartgrid)


    # def divide_spares(self):
    #     # for battery in self.smartgrid:
        
    #     current_battery = self.smartgrid[4]
    #     if current_battery['spare_capacity'] > 0:
    #         for house in self.spare_houses:
    #             poep = float(current_battery['spare_capacity'])
    #             plas = float(house[2])
    #             if poep - plas > 0:
    #                 current_battery['spare_capacity'] = poep - plas
    #                 # print (current_battery)
    #                 # current_battery['houses'] = house
    #                 house.clear()

    #     print (self.spare_houses)
    #     print (self.smartgrid[4])



# class Battery(object):

#     def __init__(self):
#         self.battery = []
#         # self.battery['location'] = 'test'
#         # self.battery['capacity'] = 'test'
#         # self.battery['houses'] = []

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
    