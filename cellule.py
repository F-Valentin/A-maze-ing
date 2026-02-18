class Cellule:
    def __init__(self, x: int, y: int, walls: int, has_visited: bool):
        self.x = x
        self.y = y
        self.walls = walls
        self.has_visited = has_visited
