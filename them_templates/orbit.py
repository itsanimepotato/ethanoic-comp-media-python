
balls = []

class Ball:
    
    def __init__(self, px, py, vx, vy, ax, ay):
        self.pos = Py5Vector(px,py)
        self.vel = Py5Vector(vx,vy)
        self.acc = Py5Vector(ax,ay)

        self.r = r
        
    def collision(self,other):
        d = dist(self.pos.x,self.pos.y,other.pos.x,other.pos.y)
        if d <= self.r:
            self.vel *= -1
            other.vel *= -1
        
        if self.pos.x > width-self.r/2:
            self.vel.x *= -1
            self.pos.x = width-self.r
        if self.pos.x < self.r/2:
            self.vel.x *= -1
            self.pos.x = self.r
            
        if self.pos.y > height-self.r/2:
            self.vel.y *= -1
            self.pos.y = height-self.r
        if self.pos.y < self.r/2:
            self.vel.y *= -1
            self.pos.y = self.r

            
    def apply_force(self, force):
        self.vel += force
    
    def gravity(self):
        return Py5Vector(0,1)
    
    def gravitation(self,other):
        ab = other.pos-self.pos
        r = mag(ab)
        ab = normalize(ab)
        g = 6.674 * pow(10,-11)
        rSq = r * r
        return ab*(g/rSq)
        
    def move(self):
        self.vel += self.acc
        self.pos += self.vel
        
    def display(self):
        circle(self.pos.x,self.pos.y,self.r)

ballCount = 10
r = 50
startVel = 5

def setup():
    size(500,500)
    global balls
    for i in range(ballCount):
        balls.append(
            Ball(int(random(r,width-r)),
                 int(random(r,height-r)),
                 -random(startVel),
                 random(startVel),
                 0,
                 0
                 )
            )
        print(f"{i}: {balls[i].pos}")

def draw():
    background(0)

    for i in range(ballCount):
        balls[i].move()
        balls[i].display()
        print(f"{i}: {balls[i].pos}")

    
    for i in range(ballCount):
        for o in range(ballCount):
            balls[i].collision(balls[o])
            balls[i].apply_force(balls[i].gravity())
            