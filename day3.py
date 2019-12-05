import sys


def main():
    with open('input_day_3.txt') as f:
        points1 = build_set_of_points(f.readline().strip().split(','))
        points2 = build_set_of_points(f.readline().strip().split(','))

        minDist = find_intersections(points1, points2)

        print(minDist)




def build_set_of_points(input):
    points = {}
    point = [0,0]
    steps = 0

    for i in input:
        direc = i[0]
        dist = int(i[1:])
        for j in range(dist):
            steps += 1
            if direc == 'R':
                point[0] += 1
            elif direc == 'L':
                point[0] -= 1
            elif direc == 'U':
                point[1] += 1
            else:
                point[1] -= 1
            if (point[0], point[1]) not in points:
                points[(point[0], point[1])] = steps
    return points


def find_intersections(input1, input2):
    intersect = set(list(input1)).intersection(set(list(input2)))

    minDist = sys.maxsize

    for pt in intersect:
        if (input1[pt] + input2[pt]) < minDist:
            minDist = input1[pt] + input2[pt]

    return minDist


if __name__ == '__main__':
    main()
