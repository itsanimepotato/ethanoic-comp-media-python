
angle = 0

def setup():
    size(500,500)
    
def draw():
    global angle
    translate(width/2,height/2)
    background(0)
    
    s_val = sin(radians(angle))
    c_val = cos(radians(angle))

    fill(abs(s_val*255))
    circle(0,s_val*100,50)
    circle(c_val*100,0,50)
    
    circle(s_val*100,s_val*100,s_val*100)
    
    circle(s_val*75+125,-width/2+25,50)

    
    fill(0)
    text("sin",0,s_val*100)
    text("cos",c_val*100,0)

    angle += 5