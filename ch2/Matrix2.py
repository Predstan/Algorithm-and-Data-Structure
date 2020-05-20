# Implements the Matrix ADT using the 2-D Array

from Array2D import Array2D


class Matrix:
    # Creates the Matrix sizes by number of Rows and Columns
    def __init__(self, numRows = 0, numCols = 0):
        self.mat = Array2D(numRows, numCols)
        self.mat.clear(0)

    # Returns the Number of Columns of the Matrix
    def numCols(self):
        return self.mat.numCols()

    # Returns the Number of Rows of the Matrix
    def numRows(self):
        return self.mat.numRows()

    # Returns the value in the index
    def __getitem__(self, ndx):
        return self.mat[ndx[0], ndx[1]]

    # Set the value to the index of the matrix
    def __setitem__(self, ndx, value):
        self.mat[ndx[0], ndx[1]] = value


    # Scales the Matrix by a given Scalar
    def scaleBy(self, scalar):
        for i in range(self.numRows()):
            for j in range(self.numCols()):
                self[i,j] *= scalar

    # Creates and Returns the Transpose of the Matrix
    def transpose(self):
        new = Matrix(self.numCols(), self.numRows())
        for i in range(self.numRows()):
            for j in range(self.numCols()):
                new[j,i] = self[i,j]
        return new

        

    # Creates and Returns the addition of both Matrices
    def __add__(self, otherMatrix):
        assert self.numRows() == otherMatrix.numRows()\
           and self.numCols() == otherMatrix.numCols(),\
               "Size of both Matricees must be the same"
        new = Matrix(self.numRows, self.numCols)
        for i in range(self.numRows()):
            for j in range(self.numCols()):
                new[i, j] = self[i, j] + otherMatrix[i,j]
        return new

    # Creates and Returns the subraction of both Matrices
    def __sub__(self, otherMatrix):
        assert self.numRows() == otherMatrix.numRows()\
           and self.numCols() == otherMatrix.numCols(),\
               "Size of both Matricees must be the same"
        new = Matrix(self.numRows, self.numCols)
        for i in range(self.numRows()):
            for j in range(self.numCols()):
                new[i, j] = self[i, j] - otherMatrix[i,j]
        return new
    
    # Creates and Returns the multiplication of both Matrices
    def __mul__(self, otherMatrix):
        assert self.numCols() == otherMatrix.numRows(),\
            "Columns of Matrix A must be equal to the Rows of matrix B"
        new = Matrix(self.numRows(), otherMatrix.numCols())
        for i in range(self.numRows()):
            for j in range(otherMatrix.numCols()):
                for k in range(otherMatrix.numRows()):
                    new[i,j] = self[i,k] * otherMatrix[k, j]
                    
        return new


a = Matrix(3, 2)
a[0,0] = 0
a[1, 0] = 2
a[2,0] = 4
a[0, 1] =1
a[1, 1] = 3
a[2, 1] = 5
b = Matrix(2, 3)
b[0, 0] = 6
b[1, 0] = 9
b[0, 1] = 7
b[0, 2] = 8
b[1, 1] = 1
b[1, 2] = 0
print(b[0,0])
for i in range(a.numRows()):
    for j in range(a.numCols()):
        print(a[i,j])

d = a.transpose()
for i in range(d.numRows()):
    for j in range(d.numCols()):
        print(d[i,j])

a*b
