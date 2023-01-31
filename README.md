# TrajectoryInQuadrilateralCalculator

Дано: \
Траектория: множество точек вида: \
[{x: XXX, y:YYY}, {x: XXX, y:YYY},...{x: XXX, y:YYY}] \
Множество четырёхугольников вида: \
[{x1: X1, y1: Y1, x2: X2, y2:Y2, x3:X3, y3:Y3, x4:Y4, y4:Y4}…] \
Примечание: \
Четырёхугольники выпуклые. \
Написать функции: \
1 Выводит подмножество четырёхугольников в которых лежит хотя бы одна из точек 
траектории \
2 Выводит подмножество четырёхугольников в которых лежат все точки траектории \
3 Выводит четырёхугольник в котором лежит максимальное количество точек траектории \
* Входные данные: \
Json файл вида \
{ \
  "trajectory": [ \
    {"x": 10.0, "y": 2.0}. \
    {"x": 11.0, "y": 4.0} \
  ], \
  "quadrangles": [ \
    {"x1": 0, "y1": 0, "x2": 1, "y2": 10, "x3": 20, "y3": 2, "x4": 100, "y4": 100} \
  ] \
}
* Выходные данные: \
Вывести в консоль указанные объекты четырёхугольников.

Start: \
`python main.py [file_path.json]`
