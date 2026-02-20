
def print_maze_line(f, data: dict):
    width = data["width"]
    print("+", end="")
    for _ in range(width):
        print("---+", end="")
    print()
    while (True):
        (c := f.read(3))
        if c == "\n":
            print()
        elif c:
            print("|", end="")
            for _ in range(width):

        else:
            break


def write_binary_maze(f, out_file):
    while (c := f.read(1)):
        if c == "\n":
            out_file.write("\n")
        else:
            out_file.write(format(int(c, 16), "04b"))
