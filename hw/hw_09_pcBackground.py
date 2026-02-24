
def setup():
    size(500,500)
    
def draw():
    rect_bg()
    
def rect_bg():
    for x in range(int(width/25)):
        for y in range(int(height/25)):
            fill(x,y,0)
            rect(x*width/25,y*height/25,width/25,height/25)