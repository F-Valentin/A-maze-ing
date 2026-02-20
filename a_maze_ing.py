import sys

import parsing
from maze import Maze
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
    solver = Solver(maze)
    solver.bfs()


if __name__ == "__main__":
    main()
