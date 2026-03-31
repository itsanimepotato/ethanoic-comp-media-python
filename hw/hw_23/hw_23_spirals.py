
r = 50

def setup():
    size(500,500)
    background(0)
    stroke(255)
    
    grid()    

def draw():
    background(0)
    grid()
    
    translate(width/2,height/2)
    circle(r*cos(radians(frame_count)),r*sin(radians(frame_count)),50+frame_count%10)

def grid():
    for x in range(10):
        for y in range(10):
            line(x*width/10,0,x*width/10,height)
            line(0,y*height/10,width,y*height/10)
