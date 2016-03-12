from .Vector import Vector
from .Point import Point


class HilbertCurve3D:

    def __init__(self, n):
        self.n = n
        self.last_point = Point(-(2**(n-1)) + 1/2, -(2**(n-1)) + 1/2, -(2**(n-1)) + 1/2)

        self.generator = self.generate_points_list(self.n, Vector(0, 1, 0), Vector(0, 0, 1), Vector(1, 0, 0))

    def __iter__(self):
        return self.generator

    def generate_points_list(self, n, v1, v2, v3):

        if n <= 0:
            yield self.last_point
        else:
            yield from self.generate_points_list(n - 1, v2, v3, v1)

            self.last_point += v1

            yield from self.generate_points_list(n - 1, v3, v1, v2)

            self.last_point += v2

            yield from self.generate_points_list(n - 1, v3, v1, v2)

            self.last_point -= v1

            yield from self.generate_points_list(n-1, -v1, -v2, v3)

            self.last_point += v3

            yield from self.generate_points_list(n - 1, -v1, -v2, v3)

            self.last_point += v1

            yield from self.generate_points_list(n - 1, -v3, v1, -v2)

            self.last_point -= v2

            yield from self.generate_points_list(n - 1, -v3, v1, -v2)

            self.last_point -= v1

            yield from self.generate_points_list(n - 1, v2, -v3, -v1)


if __name__ == '__main__':
    pass
