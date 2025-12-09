class EMA:
    def __init__(self, alpha=0.6):
        self.alpha = alpha
        self.x = None
        self.y = None

    def update(self, nx, ny):
        if self.x is None:
            self.x = nx
            self.y = ny
        else:
            self.x = self.alpha * nx + (1 - self.alpha) * self.x
            self.y = self.alpha * ny + (1 - self.alpha) * self.y
        return int(self.x), int(self.y)
