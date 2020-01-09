import csv

class Houses():

    def __init__(self, file):
        self.houses = []
        self.house_objects = []
        self.file = file

    def parse_houses(self):
        with open(self.file, "r") as csv_file:
            reader = csv.reader(csv_file)
            self.houses = list(reader)
            self.houses.pop(0)
            for house in self.houses:
                x = house[0]
                y = house[1].strip(' ')
                output = house[2].strip(' ')
                house_object = House(x, y, output)
                self.house_objects.append(house_object)
            
        return (self.house_objects)
            

class House(object):
    def __init__(self, x, y, output):
        self.x_house = int(x)
        self.y_house = int(y)
        self.output = float(output)

    def __repr__(self):
        return f"x-coordinate: {self.x_house}, y-coordinate: {self.y_house}, output: {self.output}"


