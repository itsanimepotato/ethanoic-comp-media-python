
def setup():
    size(500,500)
    background(0)
    stroke(255)
    grid()    

def draw():
    grid()

def grid():
    for x in range(10):
        for y in range(10):
            line(x*width/10,0,x*width/10,height)
            line(0,y*height/10,width,y*height/10)


