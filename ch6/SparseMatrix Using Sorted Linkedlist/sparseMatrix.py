# Implementation of the Sparse Matrix Using Sorted LinkedList
# Implementation Uses an Array to Store Each Row
# Each Rows Occupies a Single Array
from Array import Array


class sparseMatrix:
    # Creates a Matrix with no Non Zero Element
    def __init__(self, nRols, nCols):
        self.numCol = nCols
        self.ArrayOfRows = Array(nRols)

    # Returns the Number of Rows
    def numRows(self):
        return len(self.ArrayOfRows)

    # Returns the number of Columns
    def numCols(self):
        return self.numCol

    # Returns the item in a row and col using x[i, j]
    def __getitem__(self, ndxTuple):
        row, col = ndxTuple
        assert row < self.numRows() and col < self.numCols(),\
            "Out of Range"
        # Set a reference Node to the head of the given Row
        curNode = self.ArrayOfRows[row]
        # Iterate Over the Node when the column is not yet determined
        while curNode is not None and curNode.col < col:
            curNode = curNode.next

        # Return as Zero Element when the column number is higher than our target
        if curNode is None or curNode.col > col:
            return 0
        # Sets the Value when Column is Found
        else:
            return curNode.value

    # Sets of a row and column using x[i, j] = value
    def __setitem__(self, ndxTuple, value):
        row, col = ndxTuple
        # Sets a previous Node to Node
        preNode = None
        # Sets the Current Node to the head in the given Array  
        curNode = self.ArrayOfRows[row]
        
        # Iterates Over the Node when the column is not determined
        while curNode is not None and curNode.col < col:
            preNode = curNode
            curNode = curNode.next

        # Set value When Column is Determined
        if curNode is not None and curNode.col == col:
            if value == 0:
                # Determine if col is the head and unlink the node
                # When value is 0
                if curNode == self.ArrayOfRows[row]:
                    self.ArrayOfRows[row] = curNode.next
                else:
                    preNode.next = curNode.next  
            # Set Value when value is not 0 
            else:
                curNode.value = value
        
        # When column is not Found and Value is not 0
        elif value != 0:
            # Creates the Node element
            newNode = MatrixElements(col, value)
            newNode.next = curNode
            # Determine if Node is head
            if curNode == self.ArrayOfRows[row]:
                self.ArrayOfRows[row] = newNode                
            else:
                preNode.next = newNode
    # Scale the Matrix Element by a Value
    def ScaleBy(self, scalar):
        for row in range(self.numRows()):
            curNode = self.ArrayOfRows[row]
            while curNode is not None:
                curNode.value *= scalar
                curNode = curNode.next

    # Returns the Addition of two Matrices
    def __add__(self, OtherMatrix):
        assert self.numRows() == OtherMatrix.numRols()\
           and self.numCols() == OtherMatrix.numCols(), \
                   "Matrix not Compatible for Addition"
        # Creates a New Matrix for the storage
        MatrixC = sparseMatrix(self.numRows(), self.numCols())

        # Iterate over Matrix A and check each Non Zero element
        for row in range(self.numRows()):
            curNode = self.ArrayOfRows[row]
            while curNode is not None:
                MatrixC[row, curNode.col] = curNode.value
                curNode = curNode.next

            
        for row in range(self.numRows()):
            curNode = OtherMatrix.ArrayOfRows[row]
            while curNode is not None:
                MatrixC[row, curNode.col] += curNode.value
                curNode = curNode.next

        return MatrixC

    # Returns the Subtraction of 2 Matrices    
    def __sub__(self, OtherMatrix):
        assert self.numRows() == OtherMatrix.numRows()\
           and self.numCols() == OtherMatrix.numCols(),\
                " Matrix not Compatible for Addition"

        MatrixC = sparseMatrix(self.numRows(), self.numCols())

        for row in range(self.numRows()):
            curNode = self.ArrayOfRows[row]
            while curNode is not None:
                MatrixC[row, curNode.col] = curNode.value
                curNode = curNode.next

            
        for i in range(self.numRows()):
            curNode = OtherMatrix.ArrayOfRows[i]
            while curNode is not None:
                MatrixC[row, curNode.col] -= curNode.value
                curNode = curNode.next

        return MatrixC

    # Return the transpose of a Matrix
    def transpose(self):

        newMat = sparseMatrix(self.numCols(), self.numRows())

        for row in range(self.numRows()):
            curNode = self.ArrayOfRows[row]
            while curNode is not None:
                newMat[curNode.col, row] = curNode.value
                curNode = curNode.next
        return newMat

    # Returns the Multiplication of  2 Matrices
    def __mul__(self, MatB):

        assert self.numCols() == MatB.numRows(),\
            "Cannot be Multiplied"

        newMat = sparseMatrix(self.numRows(), MatB.numRows())
        
        for i in range(self.numRows()):
            curNodeA = self.ArrayOfRows[i]
            while curNodeA is not None:
                curNodeB = MatB.ArrayOfRows[curNodeA.col]

                while curNodeB is not None:
                    newMat[i, curNodeB.col] += curNodeA.value * curNodeB.value
                    curNodeB = curNodeB.next

                curNodeA = curNodeA.next
                
        return newMat
            
class MatrixElements(object):
    def __init__(self, col, value):
        self.col = col
        self.value = value
        self.next = None            

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


print("\n")
print(MatA[1, 2])
print(MatA[1, 3])
print(MatA[2, 1])
print(MatA[2, 3])
print("\n")

print(MatC[1, 1])
print(MatC[1, 2])

print(MatC[2, 1])
print(MatC[2, 2])











           


            







