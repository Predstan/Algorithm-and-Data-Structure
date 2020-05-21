# Implementing the LIFE GRID ADT for Game of Life

from Array2D import Array2D

class LifeGrid:
    # Defines the Constant to reperesent the Live and Dead Cells
    live = "@"
    dead = "."

    # Creating Game Grids
    def __init__(self, numRow, numCol):
        self.grid = Array2D(numRow, numCol)
        self.configure(list())

    # Returns the Number of Rows of the Grid
    def numRows(self):
        return self.grid.numRows()

    # Returns the Number of Columns of the Grid
    def numCols(self):
        return self.grid.numCols()

    # Clears and Configures the Live cell
    def configure(self, coordlist):
        for i in range(self.numRows()):
            for j in range(self.numCols()):
                self.clearCell(i, j)


        for cell in coordlist:
            self.setCell(cell[0], cell[1])

    # Set Cell to dead Cell
    def clearCell(self, row, col):
        assert row >= 0 and row < self.grid.numRows()\
           and col >= 0 and col < self.grid.numCols(),\
                "Invalid Range in Grid"
        self.grid[row, col] = LifeGrid.dead

    # Set cell to live cell
    def setCell(self, row, col):
        assert row >= 0 and row < self.grid.numRows()\
           and col >= 0 and col < self.grid.numCols(),\
                "Invalid Range in Grid"
        self.grid[row, col] = LifeGrid.live

    # Returns True if Cell is Live
    def isLiveCell(self, row, col):
        assert row >= 0 and row < self.grid.numRows()\
           and col >= 0 and col < self.grid.numCols(),\
                "Invalid Range in Grid"
        if self.grid[row, col] == LifeGrid.live:
            return True

    # Retuen number of neighbor's Cells
    def numLiveNeighbnors(self, row, col):
        assert row >= 0 and row < self.grid.numRows()\
           and col >= 0 and col < self.grid.numCols(),\
                "Invalid Range in Grid"
        num = 0
        if self.grid[row,col] == LifeGrid.live:
            num -= 1
        for i in range(abs(row-1), row+2):
            for j in range(abs(col-1), col+2):
                try:
                    if self.grid[i,j] == LifeGrid.live:
                        num += 1
                except:
                    continue
        return num
