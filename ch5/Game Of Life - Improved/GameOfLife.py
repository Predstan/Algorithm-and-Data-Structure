from sparseLifeGrid import sparseLifeGrid


def main(init_config, num_gen):
    # Constructs the Main Grid and Configures it
    grid = sparseLifeGrid()
    grid.configure(init_config)
    print("\n")
    
    # Play Game
    print("Start Point")
    draw(grid)
    for i in range(num_gen):
        evolve(grid)
        print("\n")
        print("Generation", i+1)
        if grid.numOfLiveCells() != 0:
            draw(grid)
        else:
            print ("Dead Cell")
            break

# Function for regenerating live and dead organisms according to the Rules 
def evolve(grid):
    # Creates a list for live cells after each generation
    live_cells = list()

    # Iterates over the grid for regeneration of cells according to the rule
    for i in range(0, grid.maxRange()[0]+2):
        for j in range(0, grid.maxRange()[1]+2):

            # Determine Number of live Neigbors
            neighbours = grid.numLiveNeighbors(i, j)
           
            

            # Regeneration from live and dead cells
            if (neighbours == 2 and grid.isLiveCell(i, j)) or\
                (neighbours == 3):
                live_cells.append((i, j))

    # Reconfigure live cells
    grid.configure(live_cells)

# Draw Grid
def draw(grid):
    
    num = 0

    # Creates a list for each rows
    row = []
    rowend, colend = grid.maxRange()
    
    # iterates over Grid
    for i in range(0, rowend+2):
        for j in range(0, colend+2):

            # Determines if cell is a live cell
            if grid.isLiveCell(i, j):
                row.append("@") # append @ for Livecell
            else:
                row.append(".") # append . for dead cell
            num += 1

            # print out each row
            if num == colend+2:
                print("  ".join(row))
                num = 0
                row = []

# Execute Main Function
INIT_CONFIG =[ (3, 3), (0, 0), (5, 5) ]

num_gen = 8
main(INIT_CONFIG, num_gen)
