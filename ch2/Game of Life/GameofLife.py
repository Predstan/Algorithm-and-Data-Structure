from LifeGrid import LifeGrid

init_cofig = [(1,1), (1, 2), (2, 2), (3, 2)]

grid_width = 5
grid_height = 5

num_gen = 8

def main():
    
    grid = LifeGrid(grid_width, grid_height)
    grid.configure(init_cofig)
    draw(grid)
    for i in range(num_gen):
        evolve(grid)
        print("\n")
        draw(grid)

def evolve(grid):

    live_cells = list()

    for i in range(grid.numRows()):
        for j in range(grid.numCols()):

            neighbours = grid.numLiveNeighbnors(i, j)

            if (neighbours == 2 and grid.isLiveCell(i, j)) or\
                (neighbours == 3):
                live_cells.append((i, j))

    grid.configure(live_cells)

def draw(grid):
    for row in range(grid.numRows()):
            print("  ".join(grid.grid.numRow[row]))

main()