from swampy.TurtleWorld import *
from random import randint, choice
from draw_shapes import Shape, draw_tool

import matplotlib.pyplot as plt
import plotly.plotly as py
import plotly
plotly.tools.set_credentials_file(username='nizan1212', api_key='yL4axfj0HAgFi08GXP0X')

NUMBER_OF_REPEATS = 5           # number of polygons
NUMBER_OF_EDGES = [3, 4, 5, 7]      # optional edges for polygons

''' Builds hostograms '''
def histogram(values, title):
    plt.hist(values)
    plt.title(title)
    plt.xlabel("Value")
    plt.ylabel("Frequency")
    fig = plt.gcf()
    plot_url = py.plot_mpl(fig, filename=title + '-histogram')


if __name__ == "__main__":
    failure = 0  # number of unsuccessful shapes
    areas_hist = []
    angles_hist = []
    for shape in range(1, NUMBER_OF_REPEATS+1):
        s = Shape(choice(NUMBER_OF_EDGES))
        try:
            s.draw_polygon(s, draw_tool)
            print ("Shape {} painted".format(shape))
            angles_hist.append(s.edges)
            s.find_equal_angles(s.angle_list)
            area = s.get_inscribe_rectangle_area()
            areas_hist.append(area)
            print ("Area of the inscribe rectangle is {}\n".format(area))
        except RuntimeError:
            failure += 1

        """moving to the next shape"""
        pu(draw_tool)  # pen up
        fd(draw_tool, 60)  # move pen
        lt(draw_tool, 180)
        pd(draw_tool)  # pen down

    if failure > 1:
        print (str(failure) + "shapes did not draw successfully")
    else:
        print ("All shapes successfully painted")

    # histogram(angles_hist, "Angles Distribution")
    # histogram(areas_hist, "Areas Distribution")
