class Bullet:
    def __init__(self, id, x0, y0):
        self.id = id
        self.x0 = x0
        self.y0 = y0

    def move(self):
        self.canvas.move(self.id, 0, -10)
        self.y0 -= 10
