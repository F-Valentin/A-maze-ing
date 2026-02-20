import sys

import parsing
from maze import Maze
from print_maze import print_maze_from_binary_list, read_maze_from_hex_file
from solver import Solver


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
    print_maze_from_binary_list(
        binary_maze,
        result["width"],
        result["height"],
        result["entry"],
        result["exit"])
    solver = Solver(maze)
    solver.bfs()


if __name__ == "__main__":
    main()
