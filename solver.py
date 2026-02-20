from cellule import Cellule
from maze import Maze


class Solver:
    def __init__(self, maze: Maze) -> None:
        self.maze = maze

        if not self.is_valid_maze():
            print("The maze is not valid")
            return None

        self.shortest_path: dict[Cellule, Cellule] = {}
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

        def is_valid_neighbor(neighbor: tuple[int, int]) -> bool:
            n_x = neighbor[0]
            n_y = neighbor[1]

            if not (0 <= n_x < width and 0 <= n_y < height):
                return False

            cell = maze[n_y][n_x]

            if cell.has_visited:
                return False

            wall_open = False

            if y + 1 == n_y and not cell.walls & north:
                wall_open = True
            elif y - 1 == n_y and not cell.walls & south:
                wall_open = True
            elif x + 1 == n_x and not cell.walls & west:
                wall_open = True
            elif x - 1 == n_x and not cell.walls & east:
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

        return neighbors

    def get_shortest_path(self) -> str:  # pas fini
        out: str = ""
        maze = self.maze.maze
        shortest_path = self.shortest_path

        exit = self.exit
        curr_cell = maze[exit[1]][exit[0]]

        while (curr_cell.x, curr_cell.y) != self.entry:
            prev_cell = shortest_path[curr_cell]
            prev_cell.has_solver_visited = "1"
            if prev_cell.x + 1 == curr_cell.x:
                out += "E"
            if prev_cell.x - 1 == curr_cell.x:
                out += "W"
            elif prev_cell.y + 1 == curr_cell.y:
                out += "S"
            elif prev_cell.y - 1 == curr_cell.y:
                out += "N"
            curr_cell = prev_cell

        return out[::-1]

    def bfs(self) -> None:
        maze = self.maze.maze
        shortest_path = {}
        queue = []

        entry = self.entry
        entry = maze[entry[1]][entry[0]]
        exit = self.exit

        entry.has_visited = True
        queue.append(entry)

        while queue:
            curr_cell = queue.pop(0)

            if (curr_cell.x, curr_cell.y) == exit:
                break

            neighbors = self.get_random_valid_cells(curr_cell.x, curr_cell.y)

            if neighbors is None:
                continue

            for neighbor in neighbors:
                if not neighbor.has_visited:
                    neighbor.has_visited = True
                    shortest_path[neighbor] = curr_cell
                    queue.append(neighbor)

        print(len(shortest_path))
        self.shortest_path = shortest_path
        print(self.get_shortest_path())
