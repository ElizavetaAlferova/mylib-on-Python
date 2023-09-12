import unittest
from shapes import Circle, Triangle, Rectangle, Square


class TestShapes(unittest.TestCase):
    def test_circle_area(self):
        circle = Circle(5)
        self.assertAlmostEqual(circle.area(), 78.5398, places=4)

    def test_triangle_area(self):
        triangle = Triangle(3, 4, 5)
        self.assertAlmostEqual(triangle.area(), 6.0, places=4)

    def test_triangle_is_rightangled(self):
        triangle = Triangle(3, 4, 5)
        self.assertTrue(triangle.is_rightangled())

    def test_rectangle_area(self):
        rectangle = Rectangle(6, 8)
        self.assertEqual(rectangle.area(), 48)

    def test_square_area(self):
        square = Square(4)
        self.assertEqual(square.area(), 16)


if __name__ == '__main__':
    unittest.main()