# Implements the Game of Life Program
from LifeGrid import LifeGrid

# Configuration for the Live Organisms
def init_config():
    live = int(input("Enter Number of Live Cells :"))
    init_config = [] * live
    for i in range(live):
        print("For Cell", i+1)
        r = int(input("Enter row number :"))
        c = int(input("Enter column number :"))
        cell = (r, c)
        init_config.append(cell)
    return init_config




# Number of Columns and Rows on Grid
grid_width = int(input("Enter Grid's Width :"))
grid_height = int(input("Enter Grid's height :"))

# Number of generation
num_gen = int(input("Enter Number of Generation :"))


def main():
    # Constructs the Main Grid and Configures it
    grid = LifeGrid(grid_width, grid_height)
    grid.configure(init_config())
    print("\n")
    
    # Play Game
    print("Start Point")
    draw(grid)
    for i in range(num_gen):
        evolve(grid)
        print("\n")
        print("Generation", i+1)
        draw(grid)

# Function for regenerating live and dead organisms according to the Rules 
def evolve(grid):
    # Creates a list for live cells after each generation
    live_cells = list()

    # Iterates over the grid for regeneration of cells according to the rule
    for i in range(grid.numRows()):
        for j in range(grid.numCols()):

            # Determine Number of live Neigbors
            neighbours = grid.numLiveNeighbnors(i, j)
            

            # Regeneration from live and dead cells
            if (neighbours == 2 and grid.isLiveCell(i, j)) or\
                (neighbours == 3):
                live_cells.append((i, j))

    # Reconfigure live cells
    grid.configure(live_cells)

# Draw Grid
def draw(grid):
    rows= []
    num = 0
    for i in range(grid.numRows()):
            row = grid.grid.numRow[i]
            for value in row:
                rows.append(value)
                num +=1
            if num == grid.numCols():
                print("  ".join(rows))
                num = 0
                rows = list()
# Execute Main Function
main()