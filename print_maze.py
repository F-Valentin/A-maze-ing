def read_maze_from_hex_file(filename):
    maze = []
    with open(filename, "r") as f:
        lines = [line.strip() for line in f.readlines()]

    for line in lines:
        row = []
        for i in range(0, len(line)):
            row.append(format(int(line[i], 16), "04b"))
        maze.append(row)
    return maze


def print_maze_from_binary_list(maze, width, height, entry, exit):
    for r in range(height):
        print("+", end="")
        for c in range(width):
            if maze[r][c][3] == "1":
                print("---+", end="")
            else:
                print("   +", end="")
        print()
        for c in range(width):
            if maze[r][c][0] == "1":
                print("|", end="")
            else:
                print(" ", end="")
            if r == entry[1] and c == entry[0]:
                print("🟢 ", end="")
            elif r == exit[1] and c == exit[0]:
                print("🔴 ", end="")
            else:
                print("   ", end="")
        if maze[r][-1][2] == "1":
            print("|")
        else:
            print(" ")

    print("+", end="")
    for _ in range(width):
        print("---+", end="")
    print()
