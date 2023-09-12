import math


class Shape:
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2


class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        p = (self.a + self.b + self.c) / 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

    def is_rightangled(self):
        sides = [self.a, self.b, self.c]
        sides.sort()
        return abs(sides[0] ** 2 + sides[1] ** 2 - sides[2] ** 2) < 1e-6


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)


if __name__ == '__main__':
    # Примеры использования
    circle = Circle(5)
    print('Площадь круга:', circle.area())

    triangle = Triangle(3, 4, 5)
    print('Площадь треугольника:', triangle.area())
    print('Прямоугольный ли треугольник:', triangle.is_rightangled())

    rectangle = Rectangle(6, 8)
    print('Площадь прямоугольника:', rectangle.area())

    square = Square(4)
    print('Площадь квадрата:', square.area())