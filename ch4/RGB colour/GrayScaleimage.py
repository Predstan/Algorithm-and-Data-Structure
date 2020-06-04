# Implementation of the RGB ADT using 2-D Array

from Array2D import Array2D

class colorImage:
    # Creates an instance of the image
    def __init__(self, nrols, ncols):

        self.colorImage = Array2D(nrols, ncols)
        self.clear(0,0,0)

    # Returns the width of the image
    def width(self):
        return self.colorImage.numCols()

    # Returns the height of the image
    def height(self):
        return self.colorImage.numRows()

    # Clears the color of every pixel in the image
    def clear(self, *color):
        color = RGBcolor(color[0], color[1], color[2])
        self.colorImage.clear(color)

    # Returns the RGB value at a particular index
    def __getitem__(self, ndxTuple):
        row = ndxTuple[0]
        col = ndxTuple[1]
        assert row >= 0 and row < self.height()\
           and col >= 0 and col <self.width(),\
                    "row or column out of range"
        return self.colorImage[row, col]

    # Sets the RGB value of a pixel
    def __setitem__(self, ndxTuple, *color):
        row = ndxTuple[0]
        col = ndxTuple[1]
        assert row >= 0 and row < self.height()\
           and col >= 0 and col <self.width(),\
                    "row or column out of range"
        color = RGBcolor(color[0], color[1], color[2])
        self.colorImage[row, col] = color

    # Returns the Gray scale conversion of the RGB value
    def colorToGrayscale(self, row, col):
        assert row >= 0 and row < self.height()\
           and col >= 0 and col <self.width(),\
                    "row or column out of range"
        color = self[row, col]
        red = color.red
        green = color.green
        blue = color.blue
        gray = round(0.299 *  red + 0.587 * green + 0.114 * blue)
        return gray

# Storage for the RGB of a pixel
class RGBcolor:

    def __init__(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue
    



