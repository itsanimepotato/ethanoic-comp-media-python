
def setup():
    size(500,500)
    how_tl()
    
def draw():
    #orbs()
    stack()

def how_tl():
    # translate moves origin
    rect(0,0,55,55)
    translate(30,20)
    rect(0,0,55,55)
    translate(14,14)
    rect(0,0,55,55)

def orbs():
    background(0)
    translate(mouse_x, mouse_y)
    circle(-40,0,65)
    circle(40,0,32)
    circle(0,40,86)
    circle(0,-40,12)
    
    translate(-mouse_x, -mouse_y)
    circle(10,50,85)
    circle(25,64,34)
    
def stack():
    fill(255,0,0)
    push_matrix()
    translate(50,50)
    rect(0,0,100,100)
    pop_matrix()
    
    fill(0,255,0)
    push_matrix()
    translate(250,150)
    rect(0,0,100,100)
    pop_matrix()
    
    fill(0,0,255)
    push_matrix()
    translate(140,280)
    rect(0,0,100,100)
    pop_matrix()
    
    