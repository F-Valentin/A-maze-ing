import sys
import parsing
from maze import Maze


def main() -> None:
    if len(sys.argv) != 2:
        print("We want only one argument (argument: config.txt)")
        sys.exit(-1)
    result = parsing.parsing_config_data(sys.argv[1])
    print(result)
    if not result:
        return
    maze = Maze(result)
    print(maze.get_random_valid_cell(1, 1).has_visited)


if __name__ == "__main__":
    main()
