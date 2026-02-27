

def setup():
    size(500,500)
    
def draw():
    fill(255)
    circle(width/2,height/2,250)
    
    fill(0)
    arc(width/2,height/2,250,250,HALF_PI,HALF_PI*3,CHORD)
    
    circle(width/2,height/2-height/8,125)
    
    fill(255)
    no_stroke()
    circle(width/2,height/2+height/8,125)
    
    circle(width/2,height/2-height/8,20)
    fill(0)
    circle(width/2,height/2+height/8,20)
    