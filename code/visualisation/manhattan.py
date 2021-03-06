"""
manhattan.py

Layla Hoogeveen, Leon Brakkee and Ramon Soesan

File with the code to make a visualisation of the algomanhattan.
"""


from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource, Plot, LinearAxis, Grid
from bokeh.models.glyphs import MultiLine
from bokeh.io import curdoc, show
from code.classes.standardobjects import batteries, houses
import copy


class Visual():

    def __init__(self, houses, batteries):

        self.batteries = batteries.batteries
        self.connected_houses = houses

        self.coordinates_house_x = []
        self.coordinates_house_y = []
        self.coordinates_battery_x = []
        self.coordinates_battery_y = []

        self.coord_cable_x = []
        self.coord_cable_y = []
        self.coords_all_x = []
        self.coords_all_y = []

        self.color_plot()


    def remove_coords(self):
        """Clear the temporary lists"""

        self.coord_cable_x.clear()
        self.coord_cable_y.clear()


    def color_plot(self):
        """Plot houses, batteries and cables using different colors for each battery"""

        color = ['blue','red','black','orange','green']
        i = -1
        color_list = []
        for battery in self.batteries:

            self.coordinates_battery_x.append(battery.x)
            self.coordinates_battery_y.append(battery.y)

            i += 1
            for house in battery.houses:

                self.coordinates_house_x.append(house.x)
                self.coordinates_house_y.append(house.y)

                color_list.append(color[i])
                cablez = house.cables[0]

                for cable in cablez:

                    self.coord_cable_x.append(cable.x)
                    self.coord_cable_y.append(cable.y)

                self.coords_all_x.append(copy.deepcopy(self.coord_cable_x))
                self.coords_all_y.append(copy.deepcopy(self.coord_cable_y))
                self.remove_coords()

        # empty grid
        grid = figure(plot_width = 1500 , plot_height = 600,
                        title='Smart Grid')
        # add houses
        grid.square(self.coordinates_house_x, self.coordinates_house_y, size=5)

        # add batteries
        grid.circle(self.coordinates_battery_x, self.coordinates_battery_y, size=10, color='red')

        # add cables to grid
        grid.multi_line(self.coords_all_x, self.coords_all_y, color=color_list)

        show(grid)
