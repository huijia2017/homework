# Please use the Shape structures (https://github.com/prubach/Python_OO/blob/master/Shapes.py) and extend it by:
# 1. adding a Triangle and EquilateralTriangle - they may inherit from each other
# 2. adding perimeter calculation to every structure
# 3. adding a Square that inherits from Rectangle and uses its calc_surface implementation
# 4. providing some code that tests the new functionality and structures


class Shapes:
    def __init__(self, a, b):
        self.length = a
        self.breadth = b


class Rectangle(Shapes):

    def calc_surface(self):
        return "the area of the " + str(self.__class__.__name__) + " is " + str(self.length * self.breadth) + " cm2"


import math


class Circle(Shapes):
    def __init__(self, a):
        self.radius = a

    def calc_surface(self):
        return "the area of the circle is " + str(math.pi * self.radius ** 2) + " cm2"


class Triangle:
    def __init__(self, a, b, c):
        self.length = a
        self.breadth = b
        self.height = c

    def calc_perimeter(self):
        return "The perimeter of the " + str(self.__class__.__name__) + " is " + str(self.length + self.breadth + self.height) + " cm2"


class EquilateralTriangle(Triangle):

    def __init__(self, a):
        self.length = a
        self.breadth = a
        self.height = a


class Square(Rectangle):
    def __init__(self, a):
        self.length = a
        self.breadth = a


c = Circle(10)
eq = EquilateralTriangle(8)
t = Triangle(2, 6, 10)
r = Rectangle(4, 8)
s = Square(6)

print(c.calc_surface())
print(eq.calc_perimeter())
print(r.calc_surface())
print(s.calc_surface())
print(t.calc_perimeter())
