import random
from types import CellType

from cellule import Cellule


class Maze:
    from typing import Any

    def __init__(self, config_data: dict[str, Any]):
        self.config_data = config_data
        self.width = self.config_data["width"]
        self.height = self.config_data["height"]

        self.maze = []
        self.init_maze(self.width, self.height)

    def get_random_valid_cell(self, x: int, y: int) -> Cellule | None:
        width = self.width
        height = self.height

        if not (0 <= x < width and 0 <= y < height):
            return None

        cell = self.maze[x][y]

        if len(cell.neighbors) == 0:
            return None

        random.shuffle(cell.neighbors)

        for _ in cell.neighbors:
            x = cell.neighbors[0][0]
            y = cell.neighbors[0][1]
            if not (
                0 <= x < width and 0 <= y < height
            ):
                cell.neighbors.remove((x, y))
            else:
                break

        if len(cell.neighbors) == 0:
            return None

        Maze.open_walls(cell, self.maze[x][y])

        cell = self.maze[x][y]
        cell.has_visited = True

        return cell

    def init_maze(self, width, height) -> None:
        for x in range(0, width):
            self.maze.append([])
            for y in range(0, height):
                self.maze[x].append(Cellule(x, y, 0x0F, False))

    def print_hexa_walls(self):
        width = self.width
        height = self.height
        output_file = self.config_data["output_file"]

        with open(output_file, "w") as f:
            for row in range(0, height):
                for col in range(0, row):
                    cell = self.maze[row][col]
                    f.write(str(hex(cell.walls).lstrip("0x").upper()))
                f.write("\n")

    @staticmethod
    def open_walls(cell: Cellule, cell1: Cellule):
        north = 0b0000_0001
        south = 0b0000_0100
        east = 0b0000_0010
        west = 0b0000_1000

        if cell.x + 1 == cell1.x:
            cell.walls ^= east
            cell1.walls ^= west
        elif cell.x - 1 == cell1.x:
            cell.walls ^= west
            cell1.walls ^= east
        elif cell.y + 1 == cell1.y:
            cell.walls ^= north
            cell1.walls ^= south
        elif cell.y - 1 == cell1.y:
            cell.walls ^= south
            cell1.walls ^= north

        def perfect_maze(self):
            x = self.config_data["entry"][0]
            y = self.config_data["entry"][1]
            curr_cell = self.maze[x][y]
            curr_cell.has_visited = True
            maze_path = [curr_cell]
            while len(maze_path) > 0:
                next_cell = self.get_random_valid_cell(
                    curr_cell.x, curr_cell.y)
                if next_cell:
                    print((next_cell.x, next_cell.y))
                if next_cell is None:
                    curr_cell = maze_path.pop()
                else:
                    maze_path.append(next_cell)
                    curr_cell = next_cell

    def imperfect_maze(self):
        pass
