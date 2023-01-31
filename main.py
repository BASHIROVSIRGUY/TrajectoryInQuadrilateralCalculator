import sys

from logic.handlers import TrajectoryHandler
from logic.visualizer import Visualizer


if __name__ == '__main__':
    json_file_path = 'file.json'
    
    if len(sys.argv) > 1:
        json_file_path = sys.argv[1]
        
    th = TrajectoryHandler(json_file_path)
    results = [th.filterQuadrInsideTrajectory(),
               th.filterQuadrIntersectionTrajectory(),
               [th.getQuadrWithMaxPoints()]]
    i = 0
    for result in results:
        if len(result) == 0:
            continue
        print()
        i += 1
        j = 0
        for quadrangle in result:
            print(quadrangle)
            j += 1
            k = 0
            for point in quadrangle.points:
                k += 1
                print(f'result №{i}, quadrangle №{j}, point №{k}: (x: {point.x}, y: {point.y})')

    line_data = th.trajectory.getDataForVisualization()
    quadr_data = th.quadr_list[0].getDataForVisualization()
    v = Visualizer()
    v.addLine(x_points=line_data[0], y_points=line_data[1])
    v.addQuadrilateral(quadr_data)
    v.draw()
