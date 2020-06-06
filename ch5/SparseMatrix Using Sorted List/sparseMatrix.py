class sparseMatrix:

    def __init__(self, numRow, numCol):
        self.numRow = numRow
        self.numCol = numCol
        self.elements = list()

    def numRows(self):
        return self.numRow

    def __len__(self):
        return len(self.elements)

    def numCols(self):
        return self.numCol

    def __getitem__(self, ndxTuple):
        row = ndxTuple[0]
        col = ndxTuple[1]
        assert row < self.numRow and col < self.numCol,\
               "index Must be Within Matrix"
        ndx, truth = self.findPosition(row, col)
        if truth != None:
            return self.elements[ndx].value
        else:
            return 0.0

    def __setitem__(self, ndxTuple, value):
        row = ndxTuple[0]
        col = ndxTuple[1]
        assert row < self.numRows() and col < self.numCols(),\
            "Index out of Range"
        ndx, truth = self.findPosition(row, col)

        if truth != None:
            self.elements[ndx].value = value

        else:
            entry = MatrixElements(row, col, value)
            self.elements.insert(ndx, entry)

    def scaleBy(self, scalar):
        for element in self.elements:
            element.value *= scalar

   # Returns the transpose of the Matrix
    def transpose(self):

        # Creates a transpose Matrix
        mat_transpose = sparseMatrix(self.numRow, self.numCol)

        # Iterates over the Matrix elements and change row and column
        for element in self.elements:
            elements = MatrixElements(element.col, element.row, element.value)
            ndx, truth = mat_transpose.findPosition(elements.row, elements.col)
            mat_transpose.elements.insert(ndx, elements)

        return mat_transpose

    # Returns the Subtraction two Matrix using A - B
    def __sub__(self, matB):
        assert self.numRows() == matB.numRows() and \
            self.numCols() == matB.numCols(),\
            "Row and Columns for both Matrix must be equal"

        # Creates a Matrix for the result of Subtraction
        MatC = sparseMatrix(self.numRows(), self.numCols())

        # Duplicates the values of Matrix A into the result Matrix
        for element in self.elements:
            dup = MatrixElements(element.row, element.col, element.value)
            MatC.elements.append(dup)

        # Itrates over Matrix B values
        for element in matB.elements:
            value = MatC[element.row, element.col]
            value -= matB[element.row, element.value]

            # Sets the value of the row and column into the result matrix
            MatC[element.row, element.col] = value

        return MatC

    def __add__(self, MatB):
        assert self.numRows() == MatB.numRows() and \
               self.numCols() == MatB.numCols(),\
                   " Row and Columns for both Matrix must be equal"
        # Creates a Matrix for the result of Addition
        MatC = sparseMatrix(self.numRows(), self.numCols())

        # Duplicates the values of Matrix A into the result Matrix
        for element in self.elements:
            dup = MatrixElements(element.row, element.col, element.value)
            MatC.elements.append(dup)

        # Itrates over Matrix B values
        for element in MatB.elements:
            value = MatC[element.row, element.col]
            value += MatB[element.row, element.col]

            # Sets the value of the row and column into the result matrix
            MatC[element.row, element.col] = value

        return MatC
    # Returns the Multiplication of Two Matrices using A*B
    def __mul__(self, matB):

        # Creates a Matrix for the result of the Multiplication
        matC = sparseMatrix(self.numRows(), self.numCols())

        # Gets the Transpose of Matrix B
        matB_transpose = matB.transpose()

        # Iterates over the value of Matrix A and transpose of B
        for element_A in self.elements:
            for element_B in matB_transpose.elements:

                # Determines if col of value in A and transpose of B are equal and multiplies their value
                if element_A.col == element_B.col:
                    value = element_A.value * element_B.value

                    # Iterates over the value of Matrix A and transpose of B the second time
                    for otherA in self.elements:
                        for otherB in matB_transpose.elements:

                            # Determines values that has the same column value
                            # And if the row is equal to the row of value from Matrix A
                            # And if the column is equal to the row of value from transpose of Matrix B
                            if otherA.col == otherB.col \
                                and otherA.row == element_A.row \
                                and otherB.row == element_B.row:

                                # Multiply both values from Matrix A and transpose of B
                                this = otherA.value * otherB.value

                                     # Determines that this result is not equal to the first value
                                if value != this:

                                    # Adds this result to the value
                                    value += this


                    elements = MatrixElements(element_A.row, element_B.row, value)
                    ndx, truth = matC.findPosition(element_A.row, element_B.row)
                    matC.elements.insert(ndx, elements)

        return matC


    def findPosition(self, row, col):
        low = 0
        high = len(self.elements) - 1

        while low <= high:
            mid = (high+low) // 2

            rows = self.elements[mid].row
            cols = self.elements[mid].col


            if rows == row and cols == col:
                return mid, True

            elif rows > row:
                high = mid - 1

            elif (rows == row) and cols > col:
                high = mid - 1


            else:
                low = mid + 1




        return low, None

class MatrixElements:
    def __init__(self, row, col, value):
        self.row = row
        self.col = col
        self.value = value



#TEST
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


MatC = MatA * MatB

print(MatC[0, 0])
print(MatC[0, 1])
print(MatC[0, 2])
print(MatC[0, 3])
print(MatC[1, 0])
print(MatC[1, 1])
print(MatC[1, 2])
print(MatC[1, 3])
print(MatC[2, 0])
print(MatC[2, 1])
print(MatC[2, 2])
print(MatC[2, 3])
print(MatC[3, 0])
print(MatC[3, 1])
print(MatC[3, 2])
print(MatC[3, 3])


print("\n")
print(transpose[1,1])
print(transpose[1,3])
print(transpose[2,1])
print(transpose[2,2])
print("\n")
print(transpose.findPosition(2, 2))
print(len(MatC))
print(len(MatA))
print(len(transpose))
print(len(MatC))
