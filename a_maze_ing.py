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


if __name__ == "__main__":
    main()
