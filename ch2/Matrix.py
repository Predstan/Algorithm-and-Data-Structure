 # Implements the Matrix ADT using the 1-D Array
from Array import Array

class Matrix:
    # Creates the Matrix sizes by number of Rows and Columns
    def __init__(self, numRow = 0, numCol = 0):
        self.numRow = Array(numRow)

        for i in range(numRow):
            self.numRow[i] = Array(numCol)

    # Returns the Number of Rows of the Matrix
    def numRows(self):
        return len(self.numRow)

    # Returns the Number of Columns of the Matrix
    def numCols(self):
        return len(self.numRow[0])

    # Returns the value in the index
    def __getitem__(self, ndx):
        assert ndx[0] >= 0 and ndx[0] < self.numRows()\
           and ndx[1] >= 0 and ndx[1] < self.numCols(),\
               "Out of Range"
        therow = self.numRow[ndx[0]]
        return therow[ndx[1]]

    # Set the value to the index of the matrix
    def __setitem__(self, ndx, value):
        assert ndx[0] >= 0 and ndx[0] < self.numRows()\
           and ndx[1] >= 0 and ndx[1] < self.numCols(),\
               "Out of Range"
        therow = self.numRow[ndx[0]]
        therow[ndx[1]] = value

    # Scales the Matrix by a given Scalar
    def scaleBy(self, scalar):
        for i in range(self.numRows()):
            therow = self.numRow[i]
            for i in range(self.numCols()):
                therow[i] =therow[i] * scalar

    # Creates and Returns the Transpose of the Matrix
    def transpose(self):
        new = Matrix(self.numCols, self.numRows)
        for i in range(self.numRows()):
            for j in range(self.numCols):
                new[j, i] = self[i, j]
        return new

    # Creates and Returns the addition of both Matrices
    def __add__(self, otherMatrix):
        assert self.numRows() == otherMatrix.numRows()\
           and self.numCols() == otherMatrix.numCols(),\
               "Size of both Matricees must be the same"
        new = Matrix(self.numRows(), self.numCols())
        for i in range(self.numRows()):
            for j in range(self.numCols()):
                new[i,j] =  self[i,j] + otherMatrix[i,j]
        return new
    
    # Creates and Returns the subraction of both Matrices
    def __sub__(self, otherMatrix):
        assert self.numRows() == otherMatrix.numRows()\
           and self.numCols() == otherMatrix.numCols(),\
               "Size of both Matricees must be the same"
        new = Matrix(self.numRows(), self.numCols())
        for i in range(self.numRows()):
            for j in range(self.numCols()):
                new[i, j] = self[i,j] - otherMatrix[i,j]
        return new

    # Creates and Returns the multiplication of both Matrices
    def __mul__(self, otherMatrix):
        assert self.numCols() == otherMatrix.numRows(),\
            "Columns of Matrix A must be equal to the Rows of matrix B"
        new = Matrix(self.numRows(), otherMatrix.numCols())
        for i in range(self.numRows()):
            for j in range(otherMatrix.numCols()):
                for k in range(otherMatrix.numRows()):
                    new[i,j] += self[i,k] * otherMatrix[k, j]
        return new

