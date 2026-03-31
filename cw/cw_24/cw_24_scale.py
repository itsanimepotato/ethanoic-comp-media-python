
def setup():
    size(500,500)
    
def draw():
    background(0)
    push_matrix()
    translate(width/2,height/2)
    
    s = sin(frame_count/10)*10+10
    
    scale(s)
    
    rect_mode(CENTER)
    fill(s*10)
    square(0,0,10)
    
    pop_matrix()
    