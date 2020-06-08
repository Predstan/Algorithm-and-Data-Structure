# Implementation of Sparse Matrix ADT using python List

class sparseMatrix:

    # Creating an Instance of the Matrix value
    def __init__(self, numRows, numCols):
        self.numRows = numRows
        self.numCols = numCols
        self.elements = list()

    # Returns the number of Rows
    def numRow(self):
        return self.numRows

    # Returns the number of col
    def numCol(self):
        return self.numCols

    # Returns the value of the row and col using x[i, j]
    def __getitem__(self, ndxTuple):
        ndx = self.findPosition(ndxTuple[0], ndxTuple[1])
        if ndx is not None:
            return self.elements[ndx].value
        else:
            return 0

    # Sets the value of the row and col using x[i, j] = value
    def __setitem__(self, ndxTuple, value):
        ndx = self.findPosition(ndxTuple[0], ndxTuple[1])
        if ndx is not None:
            if value != 0.0 :
                self.elements[ndx].value = value
            else:
                self.elements.pop(ndx)
        else:
            if value != 0.0:
                element = MatrixElement(ndxTuple[0], ndxTuple[1], value)
                self.elements.append(element)

    # Scale the Matrix by a value
    def scaleBy(self, scalar):
        for element in self.elements:
            element.value *= scalar

    # Returns the Addition two Matrix using A + B
    def __add__(self, MatB):
        assert self.numRows == MatB.numRows and \
               self.numCols == MatB.numCols,\
                   " Row and Columns for both Matrix must be equal"
        # Creates a Matrix for the result of Addition
        MatC = sparseMatrix(self.numRows, self.numCols)

        # Duplicates the values of Matrix A into the result Matrix
        for element in self.elements:
            dup = MatrixElement(element.row, element.col, element.value)
            MatC.elements.append(dup)

        # Itrates over Matrix B values
        for element in MatB.elements:
            value = MatC[element.row, element.col]
            value += element.value

            # Sets the value of the row and column into the result matrix
            MatC[element.row, element.col] = value

        return MatC

    # Returns the Subtraction two Matrix using A - B
    def __sub__(self, matB):
        assert self.numRows == MatB.numRows and \
            self.numCols == MatB.numCols,\
            " Row and Columns for both Matrix must be equal"

        # Creates a Matrix for the result of Subtraction
        MatC = sparseMatrix(self.numRows, self.numCols)

        # Duplicates the values of Matrix A into the result Matrix
        for element in self.elements:
            dup = MatrixElement(element.row, element.col, element.value)
            MatC.elements.append(dup)

        # Itrates over Matrix B values
        for element in MatB.elements:
            value = MatC[element.row, element.col]
            value -= element.value

            # Sets the value of the row and column into the result matrix
            MatC[element.row, element.col] = value

        return MatC

    # Returns the Multiplication of Two Matrices using A*B
    def __mul__(self, matB):

        # Creates a Matrix for the result of the Multiplication
        matC = sparseMatrix(self.numRow(), matB.numCol())
        
        # Iterates Over Non Zero Elments in Matrix A
        for element_A in self.elements:
            # Obtain the Value
            value = element_A.value
            # Iterates Over B
            for element_B in matB.elements:
                # Determine if the value on the row as same column of Mat A element
                if element_A.col == element_B.row:
                    # Multiplies this value by value in Mat A
                    value_now = value * element_B.value
                    # Puts this Value into New Matrix with Row of A as ite row
                    # And Column of B as its Column
                    matC[element_A.row, element_B.col] += value_now

        return matC


    # Returns the transpose of the Matrix
    def transpose(self):

        # Creates a Trasnpose Matrix
        mat_transpose = sparseMatrix(self.numRows, self.numCols)

        # Iterates over the Matrix elements and change row and column
        for i in range(len(self.elements)):
            element = MatrixElement(self.elements[i].col, self.elements[i].row, self.elements[i].value)
            mat_transpose.elements.append(element)


        return mat_transpose


    # Returns the position of an element in the list of element of the Matrix
    def findPosition(self, row, col):

        for i in range(len(self.elements)):
            if row == self.elements[i].row and \
               col == self.elements[i].col:
               return i
        return None

# Create a Class Storage for storing the row, col and value
class MatrixElement:

    def __init__(self, row, col, value):
        self.row = row
        self.col = col
        self.value = value


#TEST

MatA = sparseMatrix(4, 4)
MatB = sparseMatrix(4, 4)
MatA[1, 2] = 10
MatA[1, 3] = 12
MatA[2, 1] = 1
MatA[2, 3] = 2

MatB[1, 1] = 2
MatB[1, 2] = 5
MatB[2, 2] = 1
MatB[3, 1] = 8
transpose = MatB.transpose()


MatC = MatA*MatB

print(MatC[1, 1])
print(MatC[1, 2])
print(MatC[2, 1])
print(MatC[2, 2])
