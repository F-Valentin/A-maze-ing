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
        if not (0 <= x < width and 0 <= y < height):
            return None

        cell = self.maze[x][y]

        if len(cell.cells_coords) == 0:
            return None

        # the coordinates of the cells around the current cell.
        random.shuffle(cell.cells_coords)  # shuffle cell_coords to randomize the array

        # get a cell
        for _ in range(0, 4):
            x = cell.cells_coords[0][0]
            y = cell.cells_coords[0][1]
            if not (0 <= x < width and 0 <= y < height):  # if out of range, we remove the current cell
                cell.cells_coords.remove((cell.cells_coords[0][0], cell.cells_coords[0][1]))
            elif self.maze[x][y].has_visited is True:  # if the cell has already been visited, we remove the cell
                cell.cells_coords.remove((cell.cells_coords[0][0], cell.cells_coords[0][1]))
            else:
                break

        # if there are no cells available then we return None
        if (len(cell.cells_coords) == 0):
            return None

        x = cell.cells_coords[0][0]  # get x coordinate
        y = cell.cells_coords[0][1]  # get y coordinate

        cell = self.maze[x][y]  # get the cell
        cell.has_visited = True  # set the cell has visited
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
            for row in range(0, width):
                for col in range(0, height):
                    cell = self.maze[row][col]
                    f.write(str(hex(cell.walls).lstrip('0x').upper()))
                f.write("\n")

    def perfect_maze(self):
        x = self.config_data["entry"][0]
        y = self.config_data["entry"][1]
        curr_cell = self.maze[x][y]
        maze_path = [curr_cell]
        while len(maze_path) > 0:
            pass

    def imperfect_maze(self):
        pass
