# PY5 IMPORTED MODE CODE

class Tamagotchi:

    def __init__(self, x, y, s):
        self.health = 100
        self.hunger = 100

        self.size = 200
        self.pos = Py5Vector(x, y)
        self.speed = Py5Vector(random(-s, s), random(-s, s))

    def display(self):

        # Decide color based on state
        if self.hunger < 30 and self.health < 30:
            c = color(150, 0, 150)   # both bad
        elif self.hunger < 30:
            c = color(255, 0, 0)     # hungry
        elif self.health < 30:
            c = color(0, 255, 0)     # sick
        else:
            c = color(135, 207, 236) # healthy

        fill(c)
        circle(self.pos.x, self.pos.y, self.size)

        # Eyes
        fill(0)
        circle(self.pos.x - 30, self.pos.y - 20, 15)
        circle(self.pos.x + 30, self.pos.y - 20, 15)

        # Mouth / face
        if self.hunger < 30 and self.health < 30:
            text("X X", self.pos.x - 20, self.pos.y + 30)
        elif self.hunger < 30:
            line(self.pos.x - 30, self.pos.y + 40, self.pos.x + 30, self.pos.y + 20)
        elif self.health < 30:
            line(self.pos.x - 30, self.pos.y + 20, self.pos.x + 30, self.pos.y + 40)
        else:
            line(self.pos.x - 30, self.pos.y + 30, self.pos.x + 30, self.pos.y + 30)

    def move(self):
        self.pos += self.speed

    def wall_collide(self):

        if self.pos.x < self.size/2 or self.pos.x > width - self.size/2:
            self.speed.x *= -1
            self.health -= 10

        if self.pos.y < self.size/2 or self.pos.y > height - self.size/2:
            self.speed.y *= -1
            self.health -= 10

    def hunger_step(self):
        if frame_count % 90 == 0:
            self.hunger -= 5

    def feed(self):
        if self.hunger < 100:
            self.hunger += 10

    def heal(self):
        if self.health < 100:
            self.health += 10