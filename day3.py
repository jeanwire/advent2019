import sys


def main():
    with open('input_day_3.txt') as f:
        points1 = build_set_of_points(f.readline().strip().split(','))
        points2 = build_set_of_points(f.readline().strip().split(','))

        minDist = find_intersections(points1, points2)

        print(minDist)



def build_set_of_points(input):
    points = set()
    point = [0,0]

    for i in input:
        direc = i[0]
        dist = int(i[1:])
        for j in range(dist):
            if direc == 'R':
                point[0] += 1
            elif direc == 'L':
                point[0] -= 1
            elif direc == 'U':
                point[1] += 1
            else:
                point[1] -= 1
            points.add((point[0], point[1]))
    return points


def find_intersections(input1, input2):
    intersect = input1.intersection(input2)

    minDist = sys.maxsize
    minPt = (0,0)

    for pt in intersect:
        if (abs(pt[0]) + abs(pt[1])) < minDist:
            minDist =abs(pt[0]) + abs(pt[1])
            minPt = pt

    return minDist


if __name__ == '__main__':
    main()
