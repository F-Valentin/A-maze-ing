import random
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

        cell_coords = [(x + 1, y), (x - 1, y), (x, y - 1), (x, y + 1)]
        random.shuffle(cell_coords)

        for _ in range(0, 4):
            x = cell_coords[0][0]
            y = cell_coords[0][1]
            if not (0 <= x < width and 0 <= y
                    < height):
                cell_coords.remove((cell_coords[0][0], cell_coords[0][1]))
            elif self.maze[x][y].has_visited is True:
                cell_coords.remove((cell_coords[0][0], cell_coords[0][1]))
            else:
                break

        if (len(cell_coords) == 0):
            return None

        x = cell_coords[0][0]
        y = cell_coords[0][1]

        cell = self.maze[x][y]
        cell.has_visited = True
        return cell

    def init_maze(self, width, height) -> None:
        for x in range(0, width):
            self.maze.append([])
            for y in range(0, height):
                self.maze[x].append(Cellule(x, y, 0x0F, False))

    def perfect_maze(self):
        pass

    def imperfect_maze(self):
        pass
