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

    def get_random_valid_cells(self, x: int, y: int) -> list[Cellule] | None:
        width = self.maze.width
        height = self.maze.height
        maze = self.maze.maze

        north = 0b0000_0001
        south = 0b0000_0100
        east = 0b0000_0010
        west = 0b0000_1000

        if not (0 <= x < width and 0 <= y < height):
            return None

        curr_cell = maze[y][x]
        curr_cell.has_visited = True

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
                curr_cell.neighbors
            )
        )

        if len(valid_neighbors) == 0:
            return None

        neighbors: list[Cellule] = []
        for x, y in valid_neighbors:
            neighbors.append(maze[y][x])

        print(f"curr_cell neighbors: {neighbors}")
        return neighbors

    def bfs(self) -> None:  # bientot fini

        shortest_path = {}

        maze = self.maze.maze
        exit = (self.exit[0], self.exit[1])

        x = self.entry[0]
        y = self.entry[1]

        curr_cell = maze[y][x]
        curr_cell.has_visited = True

        queue = []

        while True:
            if (curr_cell.x, curr_cell.y) == exit:
                break

            # recup toutes les cellules voisines valides non visiter
            queue = self.get_random_valid_cells(curr_cell.x, curr_cell.y)
            if queue is None:
                print("the maze is broken.")
                return None

            next_cell = queue.pop(0)  # nouvelle cellule

            shortest_path[next_cell] = curr_cell  # pour

            curr_cell = next_cell
