# Implements Life Grid ADT 


class sparseLifeGrid:

    dead = "."
    life = "@"
    
    # Creates an Instance of Grid with infine sized column and rows
    def __init__(self):
        self.elements = list() 

    # Returns the minimum index of row and col
    def minRange(self):
        row = 0
        col = 0
        for element in self.elements:
            if element.row <= row:
                row = element.row
            if element.col <= col:
                col = element.col
            
        return row, col

    # Returns the minimum index of row and col
    def maxRange(self):
        row = 0
        col = 0
        for element in self.elements:
            if element.row >= row:
                row = element.row
            if element.col >= col:
                col = element.col
            
        return row, col

    # Clears and Reconfigure Cell to Live
    def configure(self, coordList):

        self.elements = list()

        for cell in coordList:
            self.setCell(cell[0], cell[1])

    # Determines if cell is a live cell
    def isLiveCell(self, row, col):
        assert row >= 0 and col >= 0,\
            "Row and Col must be postive"

        for cell in self.elements:
            if row == cell.row and col == cell.col:
                return True
           
    # Clears cell to dead cell
    def clearCell(self, row, col):
        assert row >= 0 and col >= 0,\
            "Row and Col must be postive"
        ndx = self.findPosition(row, col)
        if ndx != None:
            self.elements.pop(ndx)

    # Sets cell to live cell
    def setCell(self, row, col):
        assert row >= 0 and col >= 0,\
            "Row and Col must be postive"
        ndx = self.findPosition(row, col)
        if ndx == None:
            element = LifeGrid(row, col, sparseLifeGrid.life)
            self.elements.append(element)

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


    # Helper Function to find the index of a live cell
    def findPosition(self, row, col):

        for i in range(len(self.elements)):
            if row == self.elements[i].row and \
               col == self.elements[i].col:
               return i
            else:
                return None

# Creates a class to store the element of a life cell
class LifeGrid:

    def __init__(self, row, col, value):
        self.row = row
        self.col = col
        self.value = value