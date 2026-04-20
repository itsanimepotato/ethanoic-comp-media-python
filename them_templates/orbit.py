
balls = []

class Ball:
    
    def __init__(self, px, py, vx, vy, ax, ay):
        self.pos = Py5Vector(px,py)
        self.vel = Py5Vector(vx,vy)
        self.r = r
        
    def update(self, other):
       self.collision(other)
       self.forces(other)
        
    def collision(self,other):
        d = dist(self.pos.x,self.pos.y,other.pos.x,other.pos.y)
        if d <= self.r:
            self.vel *= -1
            other.vel *= -1
    
    def display(self):
        circle(self.x,self.y,self.r)

ballCount = 10
r = 50
startVel = 5
startAcc = 5

def setup():
    size(750,750)
    global balls
    for i in range(ballCount):
        balls.append(Ball(int(random(width-r)),int(random(height-r)),-random(startVel),random(startVel),-random(startVel),random(startVel)))
        
def draw():
    for i in range(ballCount):
        for o in range(ballCount):
            balls[i].update(balls[o])
        balls[i].display()
     