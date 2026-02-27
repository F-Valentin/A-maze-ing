import sys
import os

from mazegen import MazeGenerator, parsing_config_data
from mazegen import print_maze_from_binary_list

COLORS = [
    "\033[37m",  # white
    "\033[32m",  # green
    "\033[34m",  # blue
    "\033[33m",  # yellow
    "\033[35m",  # magenta
    "\033[36m",  # cyan
]


def main() -> None:
    if len(sys.argv) != 2:
        print("We want only one argument (argument: config.txt)")
        sys.exit(-1)

    config = parsing_config_data(sys.argv[1])
    if not config:
        return

    maze_gen = MazeGenerator(width=config["width"], height=config["height"])
    if config["42"]:
        maze_gen.feel_forty_two(entry=config["entry"],
                                exit=config["exit"])
    maze_gen.generate(entry=config["entry"])
    if not maze_gen.is_valid_maze():
        print("Error: The generated maze is invalid (contains isolated cells)")
        sys.exit(-1)
    maze_gen.save_to_hex_file(config["output_file"])

    solution = maze_gen.solve(entry=config["entry"],
                              exit_coords=config["exit"])
    print(f"Shortest path length: {len(solution)}")
    print(f"Path: {solution}")

    def clear_screen():
        os.system("cls" if os.name == "nt" else "clear")

    show_path = True
    color_index = 0
    wall_color = COLORS[color_index]
    while True:
        clear_screen()

        binary_format = maze_gen.get_binary_maze()
        print_maze_from_binary_list(
            binary_format,
            config["width"],
            config["height"],
            config["entry"],
            config["exit"],
            show_path,
            wall_color
        )

        print("\n[S] Toggle path  |  [R] Regenerate  | [C] Color  |  [Q] Quit")
        choice = input("Choice: ").lower()

        if choice == "s":
            show_path = not show_path

        elif choice == "r":
            maze_gen = MazeGenerator(
                width=config["width"],
                height=config["height"]
            )
            if config["42"]:
                maze_gen.feel_forty_two(entry=config["entry"],
                                        exit=config["exit"])
            maze_gen.generate(entry=config["entry"])
            maze_gen.solve(entry=config["entry"], exit_coords=config["exit"])
            show_path = True
        elif choice == "c":
            color_index = (color_index + 1) % len(COLORS)
            wall_color = COLORS[color_index]

        elif choice == "q":
            break


if __name__ == "__main__":
    main()
