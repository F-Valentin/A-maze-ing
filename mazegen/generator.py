import random
from typing import Any, Optional

# from print_maze import print_maze_from_binary_list
from .cellule import Cellule


class MazeGenerator:
    def __init__(self, width: int, height: int,
                 seed: Optional[Any] = None) -> None:
        self.width = width
        self.height = height
        if seed is not None:
            random.seed(seed)

        self.maze: list[list[Cellule]] = []
        self.shortest_path: dict[Cellule, Cellule] = {}
        self.is_path_visible: bool = False
        self._init_maze()

    def _init_maze(self) -> None:
        """Initializes the grid of cells."""
        for y in range(self.height):
            self.maze.append([])
            for x in range(self.width):
                self.maze[y].append(Cellule(x, y, 0x0F, False))

    def generate(self, entry: tuple[int, int]) -> None:
        """Generates a perfect maze using a randomized depth-first search."""
        x, y = entry
        curr_cell = self.maze[y][x]
        curr_cell.has_visited = True
        maze_path = [curr_cell]

        while len(maze_path) > 0:
            next_cell = self._get_random_unvisited_neighbor(
                curr_cell.x, curr_cell.y)
            if next_cell is None:
                curr_cell = maze_path.pop()
            else:
                maze_path.append(next_cell)
                curr_cell = next_cell

    def re_generate(self, entry: tuple[int, int]):
        """Re-generates a perfect maze using a randomized depth-first search."""
        self._reset_visited()
        self._reset_cell_walls()
        random.seed(a=None)
        self.generate(entry)

    def solve(self, entry: tuple[int, int],
              exit_coords: tuple[int, int]) -> str:
        """Solves the maze using BFS and returns the shortest path string."""
        self._reset_visited()
        queue: list[Cellule] = []

        entry_cell = self.maze[entry[1]][entry[0]]
        entry_cell.has_visited = True
        queue.append(entry_cell)

        while queue:
            curr_cell = queue.pop(0)
            if (curr_cell.x, curr_cell.y) == exit_coords:
                break

            neighbors = self._get_valid_path_neighbors(
                curr_cell.x, curr_cell.y)
            if neighbors is None:
                continue

            for neighbor in neighbors:
                if not neighbor.has_visited:
                    neighbor.has_visited = True
                    self.shortest_path[neighbor] = curr_cell
                    queue.append(neighbor)

        return self._build_path_string(entry, exit_coords)

    def save_to_hex_file(self, filename: str) -> None:
        """Saves the maze to a file in hexadecimal format."""
        with open(filename, "w") as f:
            for row in range(self.height):
                for col in range(self.width):
                    cell = self.maze[row][col]
                    f.write(str(hex(cell.walls)).lstrip("0x").upper())
                f.write("\n")

    def get_binary_maze(self) -> list[list[str]]:
        """Adapter: Converts the cell grid to the binary string format needed by print_maze."""
        binary_maze = []
        for y in range(self.height):
            row = []
            for x in range(self.width):
                row.append(format(self.maze[y][x].walls, "04b"))
            binary_maze.append(row)
        return binary_maze

    # --- Internal Helpers ---

    def _get_random_unvisited_neighbor(
            self, x: int, y: int) -> Optional[Cellule]:
        cell = self.maze[y][x]
        valid_neighbors = list(
            filter(
                lambda coords: (
                    0 <= coords[0] < self.width
                    and 0 <= coords[1] < self.height
                    and not self.maze[coords[1]][coords[0]].has_visited
                ),
                cell.neighbors,
            )
        )
        if not valid_neighbors:
            return None

        n_x, n_y = random.choice(valid_neighbors)
        next_cell = self.maze[n_y][n_x]
        self._open_walls(cell, next_cell)
        next_cell.has_visited = True
        return next_cell

    def _open_walls(self, cell1: Cellule, cell2: Cellule) -> None:
        north, south, east, west = 0b0001, 0b0100, 0b0010, 0b1000
        if cell1.x + 1 == cell2.x:
            cell1.walls &= ~east
            cell2.walls &= ~west
        elif cell1.x - 1 == cell2.x:
            cell1.walls &= ~west
            cell2.walls &= ~east
        elif cell1.y - 1 == cell2.y:
            cell1.walls &= ~north
            cell2.walls &= ~south
        elif cell1.y + 1 == cell2.y:
            cell1.walls &= ~south
            cell2.walls &= ~north

    def _reset_visited(self) -> None:
        for row in range(self.height):
            for col in range(self.width):
                self.maze[row][col].has_visited = False

    def _reset_cell_walls(self) -> None:
        for row in range(self.height):
            for col in range(self.width):
                self.maze[row][col].walls = 0x0F

    def is_valid_maze(self) -> bool:
        """
        Checks if the maze is fully connected (no isolated cells).
        Must be called AFTER generate() and BEFORE solve() or _reset_visited().
        """
        for row in range(self.height):
            for col in range(self.width):
                if not self.maze[row][col].has_visited:
                    return False
        return True

    def _get_valid_path_neighbors(
            self, x: int, y: int) -> Optional[list[Cellule]]:
        north, south, east, west = 0b0001, 0b0100, 0b0010, 0b1000
        cell = self.maze[y][x]

        def is_open(n_x: int, n_y: int) -> bool:
            if not (0 <= n_x < self.width and 0 <= n_y < self.height):
                return False
            n_cell = self.maze[n_y][n_x]
            if n_cell.has_visited:
                return False
            if y + 1 == n_y and not n_cell.walls & north:
                return True
            if y - 1 == n_y and not n_cell.walls & south:
                return True
            if x + 1 == n_x and not n_cell.walls & west:
                return True
            if x - 1 == n_x and not n_cell.walls & east:
                return True
            return False

        valid_coords = filter(lambda c: is_open(c[0], c[1]), cell.neighbors)
        neighbors = [self.maze[c[1]][c[0]] for c in valid_coords]
        return neighbors if neighbors else None

    def _build_path_string(
        self, entry: tuple[int, int], exit_coords: tuple[int, int]
    ) -> str:
        out = ""
        curr_cell = self.maze[exit_coords[1]][exit_coords[0]]
        while (curr_cell.x, curr_cell.y) != entry:
            prev_cell = self.shortest_path.get(curr_cell)
            if not prev_cell:
                break
            prev_cell.has_solver_visited = "1"
            if prev_cell.x + 1 == curr_cell.x:
                out += "E"
            elif prev_cell.x - 1 == curr_cell.x:
                out += "W"
            elif prev_cell.y + 1 == curr_cell.y:
                out += "S"
            elif prev_cell.y - 1 == curr_cell.y:
                out += "N"
            curr_cell = prev_cell
        return out[::-1]

    def show_path(self, entry: tuple[int, int]) -> None:
        self.is_path_visible = not self.is_path_visible
        if self.is_path_visible is False:
            self.generate(entry)
            return
        # TODO add show path logic

    # def print_maze(self, config: dict[str, Any]) -> None:
    #     if not self.is_valid_maze():
    #         print("Error: The generated maze is invalid (contains isolated cells).")
    #         return
    #     self.save_to_hex_file(config["output_file"])

    #     solution = self.solve(
    #         entry=config["entry"],
    #         exit_coords=config["exit"])
    #     print(f"Shortest path length: {len(solution)}")
    #     print(f"Path: {solution}")

    #     binary_format = self.get_binary_maze()
    #     print_maze_from_binary_list(
    #         binary_format,
    #         config["width"],
    #         config["height"],
    #         config["entry"],
    #         config["exit"],
    #     )
