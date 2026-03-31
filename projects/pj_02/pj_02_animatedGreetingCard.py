class Card:
    def __init__(self, holiday, date, desc):
        self.name = holiday
        self.date = date
        self.desc = desc
        
    def display(self):
        text_size(100)
        text(self.name, width/2, height/2)
        text_size(25)
        text(self.date, width/2, height/2 + 75)
        text(self.desc, width/2, height/2 + 100)
        

sequence = 0
yC = height/2 - 75

def setup():
    size(750, 500)
    global card
    card = Card("fibonacci day!", "11/23", "a day where the date is the fibonacci sequence!")
    
def draw():
    global sequence, yC
    
    background(0) 
    fib_spiral_bg()
    fib_flower(width/4,height/4,10)
    
    text_align(CENTER, TOP)
    text_size(25)
    color_mode(HSB, 360, 100, 100)
    fill(frame_count % 360, 100, 100)
    text(f"Fibonacci number using the {sequence} number", width/2, 10)
    text(str(fibonacci(sequence)), width/2, 35)

    if frame_count % 30 == 0:
        sequence += 1
    
    card.display()

def fibonacci(n):
    a, b = 0, 1
    if n == 0: return a
    if n == 1: return b
    for i in range(1, n):
        c = a + b
        a = b
        b = c
    return b
    
def fib_spiral_bg():
    push_matrix()
    translate(width/2, height/2)
    
    a, b = 0, 1
    scale_factor = 4
    
    no_fill()
    stroke(255)
        
    for i in range(12):
        side = b * scale_factor
        
        rect(0, 0, side, side)
        arc(side, 0, side * 2, side * 2, HALF_PI, PI)
        
        translate(side, side)
        rotate(-HALF_PI)
        
        a, b = b, a + b
        
    pop_matrix()
    
def fib_flower(x, y, p):
    push_matrix()
    
    translate(x, y)
    rotate(radians(mouse_y))
    
    for i in range(p):
        rotate(TWO_PI / p)  
        ellipse(50, 0, 75, 50)
        
    circle(0,0,50)
    pop_matrix()