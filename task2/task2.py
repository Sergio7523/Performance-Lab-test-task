import sys


def read_circle_data(filename):
    with open(filename, mode='r', encoding='utf-8') as f:
        center_x, center_y = map(float, f.readline().strip().split())
        radius = float(f.readline().strip())
    return center_x, center_y, radius


def read_points(filename):
    with open(filename, mode='r', encoding='utf-8') as f:
        points = [tuple(map(float, line.strip().split())) for line in f]
    return points


def point_position(circle, point):
    center_x, center_y, radius = circle
    point_x, point_y = point
    distance_squared = (point_x - center_x) ** 2 + (point_y - center_y) ** 2
    
    if distance_squared < radius ** 2:
        return 1
    elif distance_squared == radius ** 2:
        return 0
    else:
        return 2


def main():
    if len(sys.argv) != 3:
        print(
            ('Используйте: python path/to/task2.py '
            'path/to/circle_file path/to/dotfile')
        )
        sys.exit(1)

    circle_file = sys.argv[1]
    points_file = sys.argv[2]
    center_x, center_y, radius = read_circle_data(circle_file)
    points = read_points(points_file)
    circle = (center_x, center_y, radius)

    for point in points:
        position = point_position(circle, point)
        print(position)


if __name__ == '__main__':
    main()
