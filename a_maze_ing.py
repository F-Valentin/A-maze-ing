import sys

from mazegen import MazeGenerator, parsing_config_data, print_maze_from_binary_list


def main() -> None:
    if len(sys.argv) != 2:
        print("We want only one argument (argument: config.txt)")
        sys.exit(-1)

    config = parsing_config_data(sys.argv[1])
    if not config:
        return

    maze_gen = MazeGenerator(width=config["width"], height=config["height"])

    maze_gen.generate(entry=config["entry"])
    if not maze_gen.is_valid_maze():
        print("Error: The generated maze is invalid (contains isolated cells).")
        sys.exit(-1)
    maze_gen.save_to_hex_file(config["output_file"])

    solution = maze_gen.solve(entry=config["entry"], exit_coords=config["exit"])
    print(f"Shortest path length: {len(solution)}")
    print(f"Path: {solution}")

    binary_format = maze_gen.get_binary_maze()
    print_maze_from_binary_list(
        binary_format,
        config["width"],
        config["height"],
        config["entry"],
        config["exit"],
    )


if __name__ == "__main__":
    main()
