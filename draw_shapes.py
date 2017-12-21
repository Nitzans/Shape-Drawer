from swampy.TurtleWorld import *
import random

board = TurtleWorld()       # The painting environment
draw_tool = Turtle()        # The draw tool


class Shape:
    def __init__(self, edges):
        self.edges = edges
        self.coordinates_list = []
        self.angle_list = []

    @staticmethod
    def draw_polygon(self, drawer):
        plots = [(round(drawer.get_x(), 2), round(drawer.get_y(), 2))]  # init first plot
        sum_angles = 180 * (self.edges - 2)  # This should be the total sum of polygon's angle
        average_angle = 180 - (sum_angles / self.edges)  # I chose to avoid sharp angles (less than 90)

        for i in range(self.edges-1):
            angle = int(random.uniform(average_angle - average_angle/3, average_angle + average_angle/3)) # the  divergence I allow is no more than quarter the angle
            length = random.uniform(20, 50)
            lt(drawer, angle)   # Turns left by the given angle
            fd(drawer, length)  # Moves the cursor forward by the given distance
            x = round(Turtle.get_x(drawer), 2)
            y = round(Turtle.get_y(drawer), 2)
            plots.append((x, y))  # adding plot to the list
            self.angle_list.append(angle)   # adding angle to the list

        # draw the last edge which will "close" the shape
        drawer.world.canvas.line([plots[len(plots)-1], plots[0]], fill=drawer.pen_color)
        drawer.redraw()

        self.coordinates_list.extend(plots)  # update the shape's coordinates

    ''' This function calculate the area of the rectangle surrounds the polygon'''
    def get_inscribe_rectangle_area(self):
        x_coords = []
        y_coords = []
        for x, y in self.coordinates_list:
            x_coords.append(x)
            y_coords.append(y)
        width = max(x_coords) - min(x_coords)
        height = max(y_coords) - min(y_coords)
        return width * height

    ''' This function finds angles which repeat themselves in shape'''
    def find_equal_angles(self, angles_list):
        frequency = dict((x, angles_list.count(x)) for x in angles_list)
        for angle, occurrences in frequency.items():
            if occurrences > 1:
                print ("Angle {} appears {} times".format(angle, occurrences))

