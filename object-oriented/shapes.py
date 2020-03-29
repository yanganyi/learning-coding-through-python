import math

class Square:
    def __init__(self,side):
        self.side = side

    def area(self):
        return pow(self.side, 2)

    def perimeter(self):
        return 4 * self.side

    def __str__(self):
        return 'Hey I am a square of side '+str(self.side)+'!'


class Rectangle:
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)

    def __str__(self):
        return 'Hey I am a rectangle of length '+str(self.length)+' and breadth '+str(self.breadth)+'!'

class Circle:
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return math.pi * pow(self.radius, 2)

    def perimeter(self):
        return 2 * math.pi * self.radius

    def __str__(self):
        return 'Hey I am a circle of radius '+str(self.radius)+'!'


sq_1 = Square(3)
print(sq_1)
print(sq_1.area())
print(sq_1.perimeter())

sq_1.side = 5
print(sq_1)
print(sq_1.area())
print(sq_1.perimeter())

rec_1 = Rectangle(3,5)
print(rec_1)
print(rec_1.area())
print(rec_1.perimeter())

cir_1 = Circle(5)
print(cir_1)
print(cir_1.area())
print(cir_1.perimeter())