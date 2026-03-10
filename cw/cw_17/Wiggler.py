# PY5 IMPORTED MODE CODE

class Wiggler:
    def __init__(self, w, h):
        speed = 5
        
        self.x = random(w,width-w)
        self.y = random(h,height-h) 
        self.w = w
        self.h = h
        self.xSpd = random(-speed, speed)
        self.ySpd = random(-speed, speed)
        self.c = color(random(256),random(256),random(256))
        
    def display(self):
        rect(self.x, self.y, self.w, self.h)

    def move(self):
        self.x += self.xSpd
        self.xSpd = random(-3, 3) #pick a new speed so it looks 'wiggly'
        self.y += self.ySpd
        self.ySpd = random(-3, 3) #pick a new speed so it looks 'wiggly'

    def bounceOnEdge(self):
      if self.x > width or self.x < 0:
        self.xSpd*=-1
        self.x = width/2
        background(220)
      if self.y > height or self.y < 0:
        self.ySpd*=-1
        self.y = height/2
        background(220)
        
    def changeColor(self):
        self.c = color(random(256),random(256),random(256))
        
    def animate(self, x, y):
      self.changeColor()
      fill(self.c)
      self.distance(x,y)
      self.display()
      self.move()
      self.bounceOnEdge()

    def distance(self, x1,y1):
        if dist(self.x, self.y, x1, y1) < sqrt(self.w*self.w + self.h*self.h):
            self.w += random(-5,5)
            self.h += random(-5,5)
