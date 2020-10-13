from math import sqrt

class Point:

    x = 0.0
    y = 0.0

    def __init__(self, x, y):
        self.x = x
        self.y = y


    def dist_to(self, p):
        return sqrt((self.x - p.x)**2 + (self.y - p.y)**2)

    
    def abs(self):
        return sqrt(self.x**2 + self.y**2)

class Rectangle:
  def __init__(self,point1,point2):
    self.p1 = point1
    self.p2 = point2

  def length(self):
    return abs(self.p2.x - self.p1.x)

  def height(self):
    return abs(self.p2.y - self.p1.y)

  def area(self):
    return self.height() * self.length()
  
  def perimeter(self):
    return (self.height() * 2) + (self.length() * 2)

class Circle:
  def __init__(self,point1,radius):
    self.p1 = point1
    self.rad = radius

  def area(self):
    return (self.rad * 3.14) * (self.rad * 3.14)

  def perimeter(self):
    return self.rad * 3.14 * 2.0

  def inside(self,point2):
    return self.p1.dist_to(point2) < self.rad


def main():
    p1 = Point(3, 4)
    print("The point ({}, {}) is at a distance of {} from the origin.".format(p1.x, p1.y, p1.abs()))

    p2 = Point(-1, 6.5)
    print("It is a distance {:.5} away from the point ({}, {}).".format(p1.dist_to(p2), p2.x, p2.y))

    p3 = Point(1,1)
    p4 = Point(4,5)

    rect = Rectangle(p3,p4)


    print("The area of the rectangle with corners ({},{}) and ({},{}) is {}".format(p3.x, p3.y, p4.x, p4.y, rect.area()))

    print("The perimeter of the rectangle with corners ({},{}) and ({},{}) is {}".format(p3.x, p3.y, p4.x, p4.y, rect.perimeter()))

    p5 = Point(-2,3)
    p6 = Point(0,1)

    
    circ = Circle(p5, 2)
    if circ.inside(p6):
      print("The point ({}, {}) is inside the circle".format(p6.x, p6.y))
    else:
      print("The point ({}, {}) is not inside the circle".format(p6.x, p6.y))


if __name__ == "__main__":
    main()

#skibitybibbityhippityhoppity
#beep boop i do the code properly cause i am smart and understand