# Implementation of 2-D ADT using 1-D Array
from Array import Array

class Array2D:
    # Creates the Size of the Array by number of Column and Rows
    def __init__(self, numRow, numCol):
        
        self.numRow = Array(numRow)

        for i in range(numRow):
            self.numRow[i] = Array(numCol)
    # Returns the number of Rows in the Array
    def numRows(self):
        return len(self.numRow)

    # Returns the number of Column in the Array
    def numCols(self):
        return len(self.numRow[0])

    # Clears and sets the value to a given value
    def clear(self, value):
        for row in range(self.numRows()):
            self.numRow[row].clear(value)
 
    # Returns the item in the given index
    def __getitem__(self, ndx):
        assert len(ndx) == 2, "Invalid number of array"
        row = ndx[0]
        col = ndx[1]
        assert row >= 0 and row < self.numRows()\
           and col >= 0 and col < self.numCols(),\
               "Array out of range"
        therow = self.numRow[row]
        return therow[col]

    # Sets the item in the given index to the value
    def __setitem__(self, ndx, value):
        assert len(ndx) == 2, "Invalid number of array"
        row = ndx[0]
        col = ndx[1]
        assert row >= 0 and row < self.numRows()\
           and col >= 0 and col < self.numCols(),\
               "Array out of range"
        therow = self.numRow[row]
        therow[col] = value