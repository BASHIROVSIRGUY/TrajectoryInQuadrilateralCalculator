import sys

from logic.handlers import TrajectoryHandler
from logic.visualizer import Visualizer


def printPoints(geometry_obj):
    i = 0
    for point in geometry_obj.points:
        i += 1
        print(f'point №{i}: (x: {point.x}, y: {point.y})')


def printResult(result_dict: dict) -> None:
    for title, result_list in result_dict.items():
        if len(result_list) == 0:
            continue
        print(f'\n{title}:')
        i = 0
        for quadrangle in result_list:
            i += 1
            print(f'{i}. {quadrangle}')
            printPoints(quadrangle)


def visualize(trajectory_handler_obj: TrajectoryHandler) -> None:
    v = Visualizer()
    for q in trajectory_handler_obj.quadr_list:
        quadr_data = q.getDataForVisualization()
        v.addQuadrilateral(quadr_data)
    line_data = trajectory_handler_obj.trajectory.getDataForVisualization()
    v.addLine(x_points=line_data[0], y_points=line_data[1])
    v.draw()


if __name__ == '__main__':
    json_file_path = 'file.json'
    
    if len(sys.argv) > 1:
        json_file_path = sys.argv[1]
        
    th = TrajectoryHandler(json_file_path)
    results = {
        "Зоны, в которых расположены все точки траектории": th.filterQuadrInsideTrajectory(),
        "Зоны, в которых хотя бы одна из точек траектории": th.filterQuadrIntersectionTrajectory(),
        "Зона с максимальным количеством точек траектории": [th.getQuadrWithMaxPoints()]
    }
    printPoints(th.trajectory)
    printResult(results)
    visualize(th)
