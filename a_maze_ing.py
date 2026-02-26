import sys

from mazegen import MazeGenerator, parsing_config_data


def main() -> None:
    if len(sys.argv) != 2:
        print("We want only one argument (argument: config.txt)")
        sys.exit(-1)

    config = parsing_config_data(sys.argv[1])
    if not config:
        return

    maze_gen = MazeGenerator(
        width=config["width"],
        height=config["height"],
        seed=1234)

    maze_gen.generate(entry=config["entry"])
    # maze_gen.print_maze(config)

    while (1):
        print("r to re-generate the maze.")
        print("s to show or hide the path to the exit (hide by default).")
        print("c to change the maze's color.")
        print("q to quit the program.")
        opt = input()
        print(opt)
        if (opt == "r"):
            maze_gen.re_generate(entry=config["entry"])
            # maze_gen.print_maze(config)

        elif (opt == "s"):
            maze_gen.show_path(entry=config["entry"])
        elif (opt == "c"):
            pass
        elif (opt == "q"):
            break
        else:
            print("You have passed a wrong option.")


if __name__ == "__main__":
    main()
