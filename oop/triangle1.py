import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)


class Triangle:
    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    def check(self):
        a = self.p1.distance(self.p2)
        b = self.p1.distance(self.p3)
        c = self.p2.distance(self.p3)
        if abs(a - b) < c < a + b:
            return True
        else:
            return False

    def __str__(self):
        if not self.check():
            return "INVALID"
        else:
            a = self.p1.distance(self.p2)
            b = self.p1.distance(self.p3)
            c = self.p2.distance(self.p3)
            cv = a + b + c
            return f"{cv:.3f}"

a = []
t = int(input())
for _ in range(t):
    a += [float(i) for i in input().split()]
i = 0
for x in range(t):
    a1 = Point(a[i], a[i + 1])
    a2 = Point(a[i + 2], a[i + 3])
    a3 = Point(a[i + 4], a[i + 5])
    triangle = Triangle(Point(a[i + 0], a[i + 1]), Point(a[i + 2], a[i + 3]), Point(a[i + 4], a[i + 5]))
    print(triangle)
    i += 6