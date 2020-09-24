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

class rectangle:
  
  point1 = Point(1,1)
  point2 = Point(4,5)

def main():
    p1 = Point(3.0, 4.0)
    print("The point ({}, {}) is at a distance of {} from the origin.".format(p1.x, p1.y, p1.abs()))

    p2 = Point(-1.0, 6.5)
    print("It is a distance {:.5} away from the point ({}, {}).".format(p1.dist_to(p2), p2.x, p2.y))


if __name__ == "__main__":
    main()
