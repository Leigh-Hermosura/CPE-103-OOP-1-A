class RegularPolygon:
    def __init__(self, side):
        self._side = side
class Square(RegularPolygon):
    def area(self):
        return self._side * self._side
class EquilateralTriangle(RegularPolygon):
    def area(self):
        return self._side * self._side * 0.433

# 3 new shapes
class Pentagon(RegularPolygon):
    def area(self):
        return self._side * self._side * 6.8819 * 0.25
class Hexagon(RegularPolygon):
    def area(self):
        return self._side * self._side * 2.598
class Heptagon(RegularPolygon):
    def area(self):
        return self._side * self._side * 1.75 * 2.0765

obj1 = Square(4)
obj2 = EquilateralTriangle(3)

obj3 = Pentagon(5)
obj4 = Hexagon(6)
obj5 = Heptagon(7)

print(obj1.area())
print(obj2.area())

print(obj3.area())
print(obj4.area())
print(obj5.area())
