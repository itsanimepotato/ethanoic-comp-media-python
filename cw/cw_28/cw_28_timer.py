
class Face:
    
    def __init__(self,t,x,y):
        self.t = t
        self.x = x
        self.y = y
        
        
    def display(self):
        fill(255)
        if self.t == 0:
            circle(self.x,self.y,100)
        elif self.t == 1:
            square(self.x-50,self.y-50,100)
        elif self.t == 2:
            triangle(self.x,self.y-50,self.x-50,self.y+50,self.x+50,self.y+50)
        else:
            circle(self.x,self.y,100)
        
        fill(0)
        circle(self.x-10,self.y+10,10)
        circle(self.x+10,self.y+10,10)
        line(self.x-20,self.y+25,self.x+20,self.y+25)
                
        
def setup():
    size(500,500)
    global face, sequence, time
    face = Face(0,width/2,height/2)
    sequence = 0
    time = 3

    
def draw():
    background(0)
    global face, sequence, time
    stroke(0)
    
    if frame_count % (60/3) == 0:
        time -= 1
    
    if frame_count % 60 == 0:
        sequence += 1
        face.t = sequence % 3
        time = 3
    face.display()

    fill(255)
    stroke(255)
    text_align(CENTER,BOTTOM)
    text_size(25)
    text(time,width/2,height/2+100)