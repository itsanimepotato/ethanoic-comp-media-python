
def setup():
    size(500,500)
    global minion, minion_tall, minion_short
    minion = Minion(width/2,400,"the 1st minion",100)
    minion_tall = Minion(width/2-150,400,"the 2nd minion",200)
    minion_short = Minion(width/2+150,400,"the 3rd minion",75)


class Minion:
    
    def __init__(self, xPos, yPos, n, h):
        self.color = color(255,255,0)
        
        self.x = xPos
        self.y = yPos
        
        self.name = n
        self.height = h
    
    def display(self):
        fill(self.color)
        rect(self.x-25,self.y,50,-self.height)
        
        
        fill(0)
        text_align(CENTER,CENTER)
        text_size(20)
        text(self.name,self.x,self.y-self.height-25)
        
def draw():
    minion.display()
    minion_tall.display()
    minion_short.display()