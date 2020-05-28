# Implementing Triangle Array ADT using 1-D Array

from Array import Array

class TriangleArray:
    # Creates an instance of the Array using row-major order
    def __init__(self, numRows):

        self.numRows = numRows

        # Creates a 1 Dimensional Array
        self.rows = Array(numRows)

        # Creates an Array of columns in the Rows
        # Where number of array element is equal to the number of the row
        for i in range(numRows):
            self.rows[i] = Array(i+1)

    # Returns the length of elements in the array
    def length(self):
        length = 0
        for i in range(self.numRows):
            for j in range(len(self.rows[i])):
                length += 1
        return length

    # Returns the item in the index of the array
    def __getitem__(self, ndx):
        assert len(ndx) == 2, "Must be 2 index"
        row = ndx[0]
        col = ndx[1]
        assert row >= 0 and row < len(self.rows)\
           and col >= 0 and col < len(self.rows[row]),\
               "Out of Range"
        therow = self.rows[row]
        return therow[col]

    # Sets the item in the index of the array
    def __setitem__(self, ndx, value):
        assert len(ndx) == 2, "Must be 2 index"
        row = ndx[0]
        col = ndx[1]
        assert row >= 0 and row < len(self.rows)\
           and col >= 0 and col < len(self.rows[row]),\
               "Out of Range"
        therow = self.rows[row]
        therow[col] = value

    # Clear and set the value of the array
    def clear(self, value):
        for i in range(len(self.rows)):
            for j in range(len(self.rows[i])):
                self[i, j] = value


