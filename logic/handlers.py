import json
from typing import List

from logic.geometry import Point, Trajectory, Quadrangle


class TrajectoryHandler:
    _quadr_keys = [
        ('x1', 'y1'),
        ('x2', 'y2'),
        ('x3', 'y3'),
        ('x4', 'y4'),
    ]

    def __init__(self, json_file_path: str):
        data = self._getJsonData(json_file_path)
        self.trajectory: Trajectory = self._getTrajectory(data['trajectory'])
        self.quadr_list: List[Quadrangle] = self._getQuadrList(data['quadrangles'])

    """
    Выводит подмножество четырёхугольников в которых лежит хотя бы одна из точек траектории
    """
    def filterQuadrIntersectionTrajectory(self) -> List[Quadrangle]:
        filterQuadr = []
        for quadr in self.quadr_list:
            status = False
            for point in self.trajectory.points:
                status |= quadr.checkInclude(point)
            if status:
                filterQuadr.append(quadr)
        return filterQuadr

    """
    Выводит подмножество четырёхугольников в которых лежат все точки траектории
    """
    def filterQuadrInsideTrajectory(self) -> List[Quadrangle]:
        filterQuadr = []
        for quadr in self.quadr_list:
            status = True
            for point in self.trajectory.points:
                status &= quadr.checkInclude(point)
            if status:
                filterQuadr.append(quadr)
        return filterQuadr

    """
    Выводит четырёхугольник в котором лежит максимальное количество точек траектории
    """
    def getQuadrWithMaxPoints(self) -> Quadrangle:
        target_quadr = {
            'obj': None,
            'count': 0
        }
        for quadr in self.quadr_list:
            point_count = 0
            for point in self.trajectory.points:
                if quadr.checkInclude(point):
                    point_count += 1
            if point_count > target_quadr['count']:
                target_quadr['obj'] = quadr
                target_quadr['count'] = point_count
        return target_quadr['obj']
    
    def _getJsonData(file_path):
        res_obj = None
        with open(file_path) as file:
            res_obj = json.load(file)
        return res_obj
    
    def _getTrajectory(self, data: List[dict]) -> Trajectory:
        point_list: List[Point] = []
        for item in data:
            point = Point(item['x'], item['y'])
            point_list.append(point)
        return Trajectory(point_list)

    def _getQuadrList(self, data: List[dict]) -> List[Quadrangle]:
        quadr_list = []
        for item in data:
            point_list = []
            for point_keys in self._quadr_keys:
                point = Point(item[point_keys[0]], item[point_keys[1]])
                point_list.append(point)
            quadrangle = Quadrangle(point_list)
            quadr_list.append(quadrangle)
        return quadr_list
