from Array2D import Array2D

class LifeGrid:
    live = "@"
    dead = "."
    def __init__(self, numRow, numCol):
        self.grid = Array2D(numRow, numCol)
        self.configure(list())


    def numRows(self):
        return self.grid.numRows()


    def numCols(self):
        return self.grid.numCols()


    def configure(self, coordlist):
        for i in range(self.numRows()):
            for j in range(self.numCols()):
                self.clearCell(i, j)


        for cell in coordlist:
            self.setCell(cell[0], cell[1])


    def clearCell(self, row, col):
        assert row >= 0 and row < self.grid.numRows()\
           and col >= 0 and col < self.grid.numCols(),\
                "Invalid Range in Grid"
        self.grid[row, col] = LifeGrid.dead


    def setCell(self, row, col):
        assert row >= 0 and row < self.grid.numRows()\
           and col >= 0 and col < self.grid.numCols(),\
                "Invalid Range in Grid"
        self.grid[row, col] = LifeGrid.live


    def isLiveCell(self, row, col):
        assert row >= 0 and row < self.grid.numRows()\
           and col >= 0 and col < self.grid.numCols(),\
                "Invalid Range in Grid"
        if self.grid[row, col] == LifeGrid.live:
            return True
        else:
            return False


    def numLiveNeighbnors(self, row, col):
        assert row >= 0 and row < self.grid.numRows()\
           and col >= 0 and col < self.grid.numCols(),\
                "Invalid Range in Grid"
        num = 0
        if self.grid[row,col] == LifeGrid.live:
            num -= 1
        for i in range(row-1, row+1):
            for j in range(col-1, col+1):
                try:
                    if self.grid[i,j] == LifeGrid.live:
                        num += 1
                except:
                    continue
        return num
