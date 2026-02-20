import sys

import parsing
from print_maze import write_binary_maze, print_maze_line

from maze import Maze


def main() -> None:
    if len(sys.argv) != 2:
        print("We want only one argument (argument: config.txt)")
        sys.exit(-1)
    result = parsing.parsing_config_data(sys.argv[1])
    if not result:
        return
    maze = Maze(result)
    maze.perfect_maze()
    maze.print_hexa_walls()
    with open("maze.txt", "r") as f, open("binary_maze.txt", "w") as out_file:
        write_binary_maze(f, out_file)
    with open("binary_maze.txt", "r") as out_file:
        print_maze_line(out_file, result)


if __name__ == "__main__":
    main()
