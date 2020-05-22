from Array2D import Array2D


class GrayscaleImage:
    # Creates a New instance for the height and width of the image
    def __init__(self, nrows, ncols):
        self.image = Array2D(nrows, ncols)

        # Initializes the intensity of each pixels to Black
        self.clear(0)

    # Returns the width of the image
    def width(self):
        return self.image.numCols()

    # Returns the column of the Image
    def height(self):
        return self.image.numRows()

    # Sets the intensity of every pixel to a colour
    def clear(self, value):
        if value <= 0:
            return self.image.clear(0)
        if value >= 255:
            return self.image.clear(255)
        return self.image.clear(value)
        

    # Returns the pixel in the index
    def __getitem__(self, ndx):
        row = ndx[0]
        col = ndx[1]
        return self.image[row, col]

    # Sets a pixel to a value
    def __setitem__(self, ndx, value):
        row = ndx[0]
        col = ndx[1]
        if value <= 0:
            value = 0
        if value >= 255:
            value = 255
        self.image[row, col] = value

        




    

