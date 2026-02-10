
def setup():
    size(250,250) #window size
    
def draw():
    background(220)
    main_part()
    accs()


def main_part():
    fill(255,0,0) #red
    rect(100,50,50,100) #body
    
    rect(75,75,25,50) #backpack
    
    rect(130,150,15,25) #leg r
    rect(110,150,15,25) #leg l
    
    fill(0,255,255) #cyan
    circle(150,75,25) #glass
    circle(100,75,25) #glass
    fill(0)
    circle(150,75,10)
    circle(100,75,10)
    
def accs():
    fill(255,255,0)
    arc(125, 75, 25, 25, QUARTER_PI, PI-QUARTER_PI, PIE)    
