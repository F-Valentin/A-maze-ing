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


def print_maze_from_binary_list(maze, width, height, entry, exit, show_path,
                                wall_color):
    for r in range(height):
        print(f"{wall_color}+", end="")
        for c in range(width):
            if maze[r][c][3] == "1":
                print(f"{wall_color}---+", end="")
            else:
                print(f"   {wall_color}+", end="")
        print()
        for c in range(width):
            if maze[r][c][0] == "1":
                print(f"{wall_color}|", end="")
            else:
                print(" ", end="")
            if r == entry[1] and c == entry[0]:
                print("🟢 ", end="")
            elif r == exit[1] and c == exit[0]:
                print("🔴 ", end="")
            elif show_path and maze[r][c][4] == "1":
                print(" \033[31m. ", end="")
            elif maze[r][c][5] == "1":
                print(f" {wall_color}█ ", end="")
            else:
                print("   ", end="")
        if maze[r][-1][2] == "1":
            print(f"{wall_color}|")
        else:
            print(" ")

    print(f"{wall_color}+", end="")
    for _ in range(width):
        print(f"{wall_color}---+", end="")
    print("\033[0m")
