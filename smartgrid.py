from batteries import Battery
from houses import Houses

class SmartGrid():

    def __init__(self):
        self.idk = []

    # filename als attribuut? ivm meerdere wijken
    def houses_to_battery(self): 
        house = Houses()
        bat = Battery()
        
        bats = bat.read_batteries()
        houses_left = house.parse_houses()
        
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
    smart = SmartGrid()
    smart.houses_to_battery()