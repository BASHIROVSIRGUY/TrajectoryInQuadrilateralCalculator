from logic.handlers import TrajectoryHandler
from logic.visualizer import Visualizer


if __name__ == '__main__':
    json_str = """
    {
        "trajectory": [
            {"x": 10.0, "y": 2.0},
            {"x": 11.0, "y": 4.0}
        ],
        "quadrangles": [
            {"x1": 0, "y1": 0, "x2": 1, "y2": 10, "x3": 20, "y3": 2, "x4": 100, "y4": 100}
        ]
    }
    """
    th = TrajectoryHandler(json_str)
    results = [th.filterQuadrInsideTrajectory(),
               th.filterQuadrIntersectionTrajectory(),
               [th.getQuadrWithMaxPoints()]]
    i = 0
    for result in results:
        if len(result) == 0:
            continue
        print("\n")
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
