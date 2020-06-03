
class sparseLifeGrid:

    dead = "."
    life = "@"

    def __init__(self):
        self.elements = list() 

    def minRange(self):
        row = []
        col = []
        for element in self.elements:
            row.append(element.row)
            col.append(element.col)
        return min(row), min(col)

    def maxRange(self):
        row = 0
        col = 0
        for element in self.elements:
            if element.row >= row:
                row = element.row
            if element.col >= col:
                col = element.col
            
        return row, col

    def configure(self, coordList):

        self.elements = list()

        for cell in coordList:
            self.setCell(cell[0], cell[1])

    def isLiveCell(self, row, col):
        assert row >= 0 and col >= 0,\
            "Row and Col must be postive"

        for cell in self.elements:
            if row == cell.row and col == cell.col:
                return True
           

    def clearCell(self, row, col):
        assert row >= 0 and col >= 0,\
            "Row and Col must be postive"
        ndx = self.findPosition(row, col)
        if ndx != None:
            self.elements.pop(ndx)


    def setCell(self, row, col):
        assert row >= 0 and col >= 0,\
            "Row and Col must be postive"
        ndx = self.findPosition(row, col)
        if ndx == None:
            element = LifeGrid(row, col, sparseLifeGrid.life)
            self.elements.append(element)

    
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



    def findPosition(self, row, col):

        for i in range(len(self.elements)):
            if row == self.elements[i].row and \
               col == self.elements[i].col:
               return i
            else:
                return None


class LifeGrid:

    def __init__(self, row, col, value):
        self.row = row
        self.col = col
        self.value = value