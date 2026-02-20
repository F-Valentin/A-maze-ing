import sys

import parsing
from print_maze import read_maze_from_hex_file, print_maze_from_binary_list


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
    binary_maze = read_maze_from_hex_file("maze.txt")
    print_maze_from_binary_list(binary_maze, result["width"], result["height"])


if __name__ == "__main__":
    main()
