class Card:
    def __init__(self, holiday, date, desc, toggle):
        self.name = holiday
        self.date = date
        self.desc = desc
        self.togg = toggle
        
    def display(self):
        text_size(100)
        text(self.name, width/2, height/2)
        text_size(20)
        text(self.date, width/2, height/2 + 80)
        text(self.desc, width/2, height/2 + 100)
        text(self.togg, width/2, height/2 + 120)
        

sequence = 0
yC = height/2 - 75

shell = True
pause = False
def setup():
    size(750, 500)
    global card
    card = Card("fibonacci day!",
                "11/23",
                "a day where the date is the fibonacci sequence!",
                "Press SPACE to pause and F to turn the spiral on")
    
def draw():
    if not pause:
        global sequence, yC
        
        background(0) 
        fib_spiral_bg()
        if shell:
            fib_shell(width/3,height/3,sequence)
        
        text_align(CENTER, TOP)
        text_size(25)
        color_mode(HSB, 360, 100, 100)
        fill(frame_count % 360, 100, 100)
        text(f"Fibonacci number using the {sequence} number", width/2, height-25)
        text(str(fibonacci(sequence)), width/2, height-50)

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
        
        square(0, 0, side)
        arc(side, 0, side * 2, side * 2, HALF_PI, PI)
        
        translate(side, side)
        rotate(-HALF_PI)
        
        a, b = b, a + b
        
    pop_matrix()
    
def fib_shell(x, y, p):
    text_align(CENTER,TOP)
    stroke(255)
    text("The shell is an example of fibonacci in nature!",width/2,10)
    push_matrix()
    translate(x+15*cos(radians(frame_count)), y+15*sin(radians(frame_count)))
    rotate(radians(dist(width/2,height/2,mouse_x,mouse_y)))
    
    color_mode(HSB,p,100,100)
    for i in range(p):
        stroke(i,100,100)
        rotate(-TWO_PI / p)  
        ellipse(50, 0, 75+i*2, 25)
    color_mode(RGB,255,255,255)
    stroke(255)
    circle(0,0,50)
    pop_matrix()
    
def key_pressed():
    if key == 'f':
        global shell
        shell = not shell
        
    if key == ' ':
        global pause
        pause = not pause
