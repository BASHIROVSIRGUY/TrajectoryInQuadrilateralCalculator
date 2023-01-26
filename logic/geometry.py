from typing import List
from abc import ABC, abstractmethod


class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y


class Geometry(ABC):
    points: List[Point] = []

    def __init__(self, point_list: List[Point]):
        self.points = point_list

    @abstractmethod
    def getDataForVisualization(self):
        pass


class Trajectory(Geometry):
    def getDataForVisualization(self):
        vis_data_x = []
        vis_data_y = []
        for point in self.points:
            vis_data_x.append(point.x)
            vis_data_y.append(point.y)
        return vis_data_x, vis_data_y


class Quadrangle(Geometry):
    def __init__(self, point_list: List[Point]):
        super().__init__(point_list)
        self._sortPoints()

    def checkInclude(self, out_point: Point):
        return self._calcSquareWithPoint(out_point) == self._calcSquareWithPoint(self.points[0])

    def getDataForVisualization(self):
        vis_data = []
        for point in self.points:
            vis_data.append((point.x, point.y))
        return vis_data

    def _calcSquareWithPoint(self, out_point: Point):
        square = 0
        for i in range(len(self.points)):
            square += self._calcSquareTriangle(i, out_point)
        return square

    def _calcSquareTriangle(self, current_num: int, out_point: Point) -> float:
        point_i = self.points[current_num]
        next_point = self.points[(current_num + 1) % 4]
        return abs((point_i.x - out_point.x)*(next_point.y - out_point.y) -
                   (next_point.x - out_point.x)*(point_i.y - out_point.y))/2

    def _sortPoints(self) -> None:
        def findPoint(sort_key, reverse):
            self.points = sorted(self.points, key=lambda item: item.__dict__[sort_key])
            target_point = self.points[0] if not reverse else self.points[-1]
            self.points.remove(target_point)
            return target_point

        self.points = [
            findPoint('y', False),
            findPoint('x', False),
            findPoint('y', True),
            findPoint('x', True)
        ]
