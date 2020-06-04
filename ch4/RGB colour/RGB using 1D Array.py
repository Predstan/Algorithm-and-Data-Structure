# Implementation of RGB Grid Colors ADT usind 1-D Array
from Array import Array


class colorImage:
    # Creates and instance of the Image with width and height
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.dims = self.width, self.height
        self.red = Array(height*width)
        self.red.clear(0)
        self.green = Array(height*width)
        self.green.clear(0)
        self.blue = Array(height*width)
        self.blue.clear(0)

        
    # Returns the width of the Image
    def widths(self):
        return self.width

    # Returns the height of the image
    def heights(self):
        return self.height

    # Clears the colour of all pixels
    def clear(self, *color):
        self.red.clear(color[0])
        self.green.clear(color[1])
        self.blue.clear(color[2])

    # Returns the RGB value of a pixel
    def __getitem__(self, ndxTuple):
        assert len(ndxTuple) == len(self.dims), "Invalid number of Array Subscript"
        index = self.computeIndex(ndxTuple)
        assert index is not None, "Array Subscript out of Range"
        return self.red[index], self.green[index], self.blue[index]

    # Sets the RGB value of a pixel
    def __setitem__(self, ndxTuple, value):
        assert len(ndxTuple) == len(self.dims), "Invalid number of Array Subscript"
        index = self.computeIndex(ndxTuple)
        assert index is not None, "Array Subscript out of Range"
        self.red[index] = value[0]
        self.green[index] = value[1]
        self.blue[index] = value[2]   

    # Computes the offset for an element at a particular index
    def computeIndex(self, idx):
        if len(idx) < 0 or len(idx) > len(self.dims)\
            or idx[0] < 0 or idx[0] > self.heights()\
            or idx[1] < 0 or idx[1] > self.heights():
                return None
        else:
            return idx[0] * self.width + idx[1]

