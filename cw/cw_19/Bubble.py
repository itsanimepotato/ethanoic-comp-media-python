# PY5 IMPORTED MODE CODE

class Bubble:

    def __init__(self):
        self.x = random(width)
        self.y = random(height)
        self.c = color(random(255), random(255), random(255), random(255))
        self.r = random(25, 50)
        self.xS = random(-3, 3)
        self.yS = random(-3, 3)

    def display(self):
        fill(self.c)
        circle(self.x, self.y, self.r * 2)

    def move(self):
        self.wallCollide()
        self.x += self.xS
        self.y += self.yS

    def wallCollide(self):
        if self.x < self.r or self.x > width - self.r:
            self.xS *= -1
        if self.y < self.r or self.y > height - self.r:
            self.yS *= -1

    def collide(self, other):
        d = dist(self.x, self.y, other.x, other.y)
        if d < self.r + other.r:
            self.xS, other.xS = other.xS, self.xS
            self.yS, other.yS = other.yS, self.yS