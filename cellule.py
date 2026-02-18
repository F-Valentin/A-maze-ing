class Cellule:
    def __init__(self, x: int, y: int, walls: int, has_visited: bool):
        self.x = x
        self.y = y
        self.walls = walls
        self.has_visited = has_visited
        self.cells_coords = [(x + 1, y), (x - 1, y), (x, y - 1), (x, y + 1)]
