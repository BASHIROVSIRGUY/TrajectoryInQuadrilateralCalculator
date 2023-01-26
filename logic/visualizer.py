from typing import List

import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.patches import Polygon


class Visualizer:
    def __init__(self):
        self.fig, self.axes = plt.subplots()

    def addQuadrilateral(self, data: List[tuple]) -> None:
        polygon = Polygon(data, fill=False)
        self.axes.add_patch(polygon)

    def addLine(self, x_points: list, y_points: list) -> None:
        line = Line2D(x_points, y_points, color="r")
        self.axes.add_line(line)

    def draw(self):
        self.axes.autoscale_view()
        plt.show()
