# Implements the Game of Life Program
from LifeGrid import LifeGrid

# Configuration for the Live Organisms
init_cofig = [(1,1), (1, 2), (2, 2), (3, 2)]

# Number of Columns and Rows on Grid
grid_width = 5
grid_height = 5

# Number of generation
num_gen = 8


def main():
    # Constructs the Main Grid and Configures it
    grid = LifeGrid(grid_width, grid_height)
    grid.configure(init_cofig)
    
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

            # Regenetion from live and dead cells
            if (neighbours == 2 and grid.isLiveCell(i, j)) or\
                (neighbours == 3):
                live_cells.append((i, j))

    # Reconfigure live cells
    grid.configure(live_cells)

# Draw Grid
def draw(grid):
    for row in range(grid.numRows()):
            print("  ".join(grid.grid.numRow[row]))

# Execute Main Function
main()