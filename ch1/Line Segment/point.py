# Implements the Point class for representing points in the
# 2-D Cartisian
import math

class point:
    # Creates a point object
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Returns X coordinate of the point.
    def getX(self):
        return self.x

    # Returns the Y coordinate of the point
    def getY(self):
        return self.y

    # Shifts the point by X value and Y value
    def shift(self, x_value = 0, y_value = 0):
        self.x += x_value
        self.y += y_value

    # Computes the distance between the points
    def distance(self, otherPoint):
        xDiff = self.x - otherPoint.x
        yDiff = self.y - otherPoint.y
        return math.sqrt(xDiff **2 + yDiff**2)


