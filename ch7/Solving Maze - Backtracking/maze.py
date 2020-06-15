from Array2D import Array2D
from stack import Stack

class Maze:
    maze_wall = "*"
    Path_token ="x"
    Tried_Token = " "


    def __init__(self, numRow, numCol):
        self.Grid = Array2D(numRow, numCol)
        self.startCell = None
        self.ExitCell = None

    def numRows(self):
        return self.Grid.numRows()

    def numCols(self):
        return self.Grid.numCols()

    def setWall(self, row, col):
        assert row >=0 and row < self.numRows() \
           and col >=0 and col < self.numCols(),\
               "Out of Range row or col"
        self.Grid[row, col] = Maze.maze_wall

    def setStart(self, row, col):
        assert row >=0 and row < self.numRows() \
           and col >=0 and col < self.numCols(),\
               "Out of Range row or col"
        self.startCell = cellPosition(row, col)

    def setExit(self, row, col):
        assert row >=0 and row < self.numRows() \
           and col >=0 and col < self.numCols(),\
           "Out of Range row or col"
        self.ExitCell = cellPosition(row, col)

    def findPath(self):
        row = self.startCell.row
        col = self.startCell.col
        stack = Stack()

        self.markPath(row, col)

        while self.ExitFound(row, col) is not True:
            paths = self.possiblePath(row, col)
            if len(paths) != 0:
                row, col = paths[0]
                self.markPath(row, col)
                stack.push(cellPosition(row, col))
            else:
                if stack.isEmpty():
                    return False
                else:
                    self.markTried(row, col)
                    cell = stack.pop()
                    row = cell.row
                    col = cell.col


        if self.ExitFound(row, col):
            return True

    def possiblePath(self, row, col):
        paths = []
        for i in range(row - 1, row + 2):
            for j in range(col - 1, col + 2):
                if (i <= self.numRows()-1) and (j <= self.numCols()-1):
                    if i == row or j == col:
                        if self.isValidMove(i, j):
                            paths.append((i, j))
        return paths



    def reset(self):
        for i in range(self.numRows()):
            for j in range(self.numCols):
                if self.Grid[i, j] == Maze.Path_token \
                    or self.Grid[i, j] == Maze.Tried_Token:
                    self.Grid[i, j] = None


    def isValidMove(self, row, col):
        assert row >=0 and row < self.numRows() \
           and col >=0 and col < self.numCols(),\
           "Out of Range row or col"
        return self.Grid[row, col] is None

    def ExitFound(self, row, col):
        return row == self.ExitCell.row and \
               col == self.ExitCell.col

    def markTried(self, row, col):
        self.Grid[row, col] = Maze.Tried_Token

    def markPath(self, row, col):
        self.Grid[row, col] = Maze.Path_token

    def draw(self):
        row = []
        for i in range(self.numRows()):
            for j in range(self.numCols()):
                if self.Grid[i, j] == None:
                    self.Grid[i, j] = " "
                row.append(self.Grid[i, j])
                if len(row) == self.numCols():
                    col = " ".join(row)
                    print(col)
                    row = []



class cellPosition:
    def __init__(self, row, col):
        self.row = row
        self.col = col
