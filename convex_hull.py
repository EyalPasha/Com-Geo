import math


class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y


def findBottomLeft(points: list):
    return min(points, key=lambda p: (p.y, p.x))


def polarAngle(p0, p):
    return math.atan2(p.y - p0.y, p.x - p0.x)


def sortCCW(points: list):
    p0 = findBottomLeft(points)
    points.sort(key=lambda p: (math.atan2(p.y - p0.y, p.x - p0.x), p.x - p0.x, p.y - p0.y))


def isLeftTurn(p1, p2, p3):
    return (p2.y - p1.y) * (p3.x - p2.x) - (p2.x - p1.x) * (p3.y - p2.y) < 0


def grahamScan(points: list):
    if len(points) < 3:
        return points

    sortCCW(points)
    stack = [points[0], points[1], points[2]]

    for i in range(3, len(points)):
        while len(stack) > 1 and not isLeftTurn(stack[-2], stack[-1], points[i]):
            stack.pop()
        stack.append(points[i])

    return stack
