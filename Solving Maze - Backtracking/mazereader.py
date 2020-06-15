from maze import Maze

def main():
    maze = buidMaze("maze.txt")
    if maze.findPath():
        print("Path Found")
        maze.draw()
    else:
        print("No Path Found")

def buidMaze(file):
    infile = open(file, "r")
    nrols, ncols = valuePairs(infile)
    maze = Maze(nrols, ncols)

    startCell = valuePairs(infile)
    row, col = startCell
    maze.setStart(row, col)

    ExitCell = valuePairs(infile)
    row, col = ExitCell
    maze.setExit(row, col)

    for i in range(nrols):
        line = infile.readline()
        for j in range(len(line)):
            if line[j] == "*":
                maze.setWall(i, j)

    infile.close()
    return maze


def valuePairs(infile):
    line = infile.readline()
    valA, valB = line.split()
    return int(valA), int(valB)

if __name__ == "__main__":
    main()
