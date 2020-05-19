from point import point

class lineSegment(point) :
    # Creates a Line Object
    def __init__(self, ptA, ptB):
        self.ptA = ptA
        self.ptB = ptB

    # Returns the Starting point of the Line
    def start_point(self):
        return self.ptA

    # Returns the End Point of the Line
    def end_point(self):
        return self.ptB

    # Returns the length of the line 
    def length(self):
        return self.ptA.distance(self.ptB)

    # Returns the String of the point
    def to_string(self):
        return (str(self.ptA.getX()), str(self.ptA.getY())+')'\
             + '#' + "(" + str(self.ptB.getX()), str(self.ptB.getY()))
    
    # Returns True if line is a vertical line
    def is_vertical(self):
        return self.ptA.getX() == self.ptB.getX()

    # Returns True if the line is horizontal
    def is_horizontal(self):
        return self.ptA.getY() == self.ptB.getY()

    # Returns True if the line is Parallel
    def is_parallel(self, OtherLine):
        return self.ptA.distance(OtherLine.ptA) == self.ptB.distance(OtherLine.ptB)

    def is_perpendicular(self, OtherLine):
        return (self.is_vertical() & OtherLine.is_horizontal()) or (self.is_horizontal() & OtherLine.is_vertical())
    
    def slope(self):
        if self.is_vertical() is True:
            return None
        rise = self.ptB.getY() - self.ptA.getY()
        run =  self.ptB.getX() - self.ptA.getX()
        return rise/run


    def shift(self, x = 0, y = 0):
        self.ptA.shift(x, y)
        self.ptB.shift(x, y)
   

    def midpoint(self):
        point_A = (self.ptA.getX() + self.ptB.getX())/2
        point_B = (self.ptA.getY() + self.ptB.getY())/2
        return (point_A, point_B)

 
pointA = point(0, 1)
pointB = point(-2, -2)
lineA = lineSegment(pointA, pointB)
print(lineA.is_horizontal())
print(lineA.to_string())
print(lineA.slope())
print(lineA.midpoint())

print(lineA.midpoint())
print(lineA.midpoint())
print(lineA.slope())
print(lineA.is_vertical())


