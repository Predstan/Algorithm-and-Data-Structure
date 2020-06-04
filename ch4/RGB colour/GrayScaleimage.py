from Array2D import Array2D

class colorImage:

    def __init__(self, nrols, ncols):

        self.colorImage = Array2D(nrols, ncols)
        self.clear(0,0,0)

    def width(self):
        return self.colorImage.numCols()

    def height(self):
        return self.colorImage.numRows()

    def clear(self, *color):
        color = RGBcolor(color[0], color[1], color[2])
        self.colorImage.clear(color)

    def __getitem__(self, ndxTuple):
        row = ndxTuple[0]
        col = ndxTuple[1]
        assert row >= 0 and row < self.height()\
           and col >= 0 and col <self.width(),\
                    "row or column out of range"
        return self.colorImage[row, col]

    def __setitem__(self, ndxTuple, *color):
        row = ndxTuple[0]
        col = ndxTuple[1]
        assert row >= 0 and row < self.height()\
           and col >= 0 and col <self.width(),\
                    "row or column out of range"
        color = RGBcolor(color[0], color[1], color[2])
        self.colorImage[row, col] = color

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

class RGBcolor:

    def __init__(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue
    



