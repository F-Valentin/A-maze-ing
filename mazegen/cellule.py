class Cellule:
    def __init__(self, x: int, y: int, walls: int,
                 has_visited: bool, forty_patherne: bool):
        self.x = x
        self.y = y
        self.walls = walls
        self.has_visited = has_visited
        self.has_solver_visited = "0"
        self.neighbors = [(x + 1, y), (x - 1, y), (x, y - 1), (x, y + 1)]
        self.forty_patherne = forty_patherne
