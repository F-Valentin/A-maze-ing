import random

from _typeshed import WriteableBuffer

from cellule import Cellule
from maze import Maze


class Solver:
    def __init__(self, maze: Maze) -> None:
        if not self.is_valid_maze():
            print("The maze is not valid")
            return None
        self.maze = maze
        self.entry = maze.config_data["entry"]
        self.exit = maze.config_data["exit"]

        self.reset_visited()

    def is_valid_maze(self) -> bool:
        width = self.maze.width
        height = self.maze.height

        for row in range(0, height):
            for col in range(0, width):
                maze = self.maze.maze
                if not maze[row][col].has_visited:
                    return False
        return True

    def reset_visited(self) -> None:
        width = self.maze.width
        height = self.maze.height

        for row in range(0, height):
            for col in range(0, width):
                maze = self.maze.maze
                maze[row][col].has_visited = False

    def get_random_valid_cell(self, x: int, y: int) -> Cellule | None:
        width = self.maze.width
        height = self.maze.height
        maze = self.maze.maze

        north = 0b0000_0001
        south = 0b0000_0100
        east = 0b0000_0010
        west = 0b0000_1000

        if not (0 <= x < width and 0 <= y < height):
            return None

        cell = maze[y][x]

        def is_valid_neighbor(neighbor: tuple[int, int]) -> bool:
            x = neighbor[0]
            y = neighbor[1]

            cell = maze[y][x]

            if not (0 <= x < width and 0 <= y < height) or cell.has_visited:
                return False

            wall_open = False

            if cell.walls & north:
                wall_open = True
            elif cell.walls & south:
                wall_open = True
            elif cell.walls & east:
                wall_open = True
            elif cell.walls & west:
                wall_open = True

            return wall_open

        valid_neighbors: list[tuple[int, int]] = list(
            filter(
                lambda coords: is_valid_neighbor(coords),
                cell.neighbors
            )
        )

        if len(valid_neighbors) == 0:
            return None

        neighbor_coord = random.choice(valid_neighbors)

        x = neighbor_coord[0]
        y = neighbor_coord[1]

        next_cell = maze[y][x]
        next_cell.has_visited = True

        return next_cell

    def bfs(self) -> None:

        maze = self.maze.maze
        exit = (self.exit[0], self.exit[1])

        x = self.entry[0]
        y = self.entry[1]

        curr_cell = maze[y][x]
        curr_cell.has_visited = True

        queue = [curr_cell]

        while queue:
            curr_cell = queue.pop(0)
