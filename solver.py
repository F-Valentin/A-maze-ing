class Solver:
    def __init__(self, maze_file: str) -> None:
        self.maze_file = maze_file

    def bfs(self) -> None:
        north = 0b0000_0001
        south = 0b0000_0100
        east = 0b0000_0010
        west = 0b0000_1000

        try:
            with open(self.maze_file, "w") as f:
                pass
        except FileNotFoundError:
            print(
                f"Error: The file '{self.maze_file}' "
                "was not found in the current directory."
            )
            return None
        except PermissionError:
            print(
                f"Error: You do not have permission to read '{
                    self.maze_file}'.")
            return None
