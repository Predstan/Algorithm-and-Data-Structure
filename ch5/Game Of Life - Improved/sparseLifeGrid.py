# Implentation of Life Grid with Binary Search and Sorted List
class sparseLifeGrid:
    # Creates and Infinite-Sized Grid
    def __init__(self):
        self.elements = list()

    # Returns the Maximum row and col of Grid
    def maxRange(self):
        row = 0
        col = 0
        for element in self.elements:
            if element.row >= row:
                row = element.row
            if element.col >= col:
                col = element.col
            
        return row, col

    # Returns the minimum row and col of Grid
    def minRange(self):
        row = 0
        col = 0
        for element in self.elements:
            if element.row <= row:
                row = element.row
            if element.col <= col:
                col = element.col
            
        return row, col

    # Congure Cells as live cell
    def configure(self, coordList):
        self.elements = list()

        for cell in coordList:
            self.setCell(cell[0], cell[1])

    # Set Live cell
    def setCell(self, row, col):
        # Find the Position of the Cell
        ndx = self.findPostion(row, col)
        element = LifeGrid(row, col)
        self.elements.insert(ndx[0], element)

    # Clear Cell and Set to dead Cell
    def clearCell(self, row, col):
        assert row >= 0 and col >= 0,\
            "Row and Col must be postive"
        # Find the Position of the Cell
        ndx = self.findPostion(row, col)
        if ndx[1] != None:
            self.elements.pop(ndx[0])
        
    def numOfLiveCells(self):
        return len(self.elements)

    # Determines if cell is a Live Cell
    def isLiveCell(self, row, col ):
        assert row >= 0 and col >= 0,\
            "Row and Col must be postive"
        ndx = self.findPostion(row, col)
        return ndx[1] is not None

    # Returns the number of live Neighbors
    def numLiveNeighbors(self, row, col):
        assert row >= 0 and col >= 0,\
            "Row and Col must be postive"

        num = 0
        if self.isLiveCell(row, col):
            num -= 1

        for newnum in range(row-1, row+2):
            for newcol in range(col-1, col+2):
                if newnum >= 0 and newcol >= 0:
                    if self.isLiveCell(newnum, newcol):
                        num += 1
       
        return num
    
    # Find the position of a cell in the Sorted List
    def findPostion(self, row, col):
        low = 0
        high = len(self.elements) - 1

        # Divides the List until Cell is found
        while low <= high:
            mid = (high + low) // 2
            rows = self.elements[mid].row
            cols = self.elements[mid].col

            # Returns Cell Position and True if Found
            if rows == row and cols == col:
                return mid, True

            # is the row number less than the row?
            elif rows > row:
                high = mid - 1

            # Or if row is the same
            # Is column number less than the row
            elif rows == row and cols > col:
                high = mid - 1

            # is the Cell number larger than the cell
            else:
                low = mid + 1
        # Return where cell is suppose to be and None as Tuple
        return low, None

class LifeGrid:
    def __init__(self, row, col):
        self.row = row
        self.col = col
