
class Ball:

    def __init__(self, p, v, a, r, c, m):
        self.pos = p
        self.vel = v
        self.acc = a
        
        self.r = r
        self.c = color(c)
        self.m = m
    
    def update(self, other):
        self.acc = self.gravitation(other)
        self.vel += self.acc
        self.pos += self.vel
    
    def gravitation(self, other):
        ab = other.pos - self.pos
        r = mag(ab)
        nab = norm(ab)
        g = -6.674 * pow(10,-11)
        
        num = g * other.m * self.m
        den = r * r
        
        return num/den
        
    
    def display(self):
        fill(self.c)
        circle(self.pos.x,self.pos.y,self.r)

balls = []
numBalls = 2
rad = 50

def setup():
    size(500,500)
    
    for i in range(numBalls):
        balls.append(Ball(Py5Vector(random(rad, width-rad), random(rad, height-rad)),
                          Py5Vector(0,0),
                          Py5Vector(0,0),
                          rad,
                          color(random(255),random(255),random(255)),
                          1
                          ))

def draw():
    background(0)
    
    for i in range(len(balls)):
        for o in range(len(balls)):
            balls[i].update(balls[o])
    
    for i in range(len(balls)):
            balls[i].display()
        