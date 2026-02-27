
def setup():
    size(500,500)
    
def draw():
    rect_bg()
    
def rect_bg():
    for x in range(int(width/20)):
        for y in range(int(height/20)):
            if dist(x*width/20,y*height/20,mouse_x+width/20,mouse_y+height/20) < 50:
                fc = dist(x+width/20,y,mouse_x,mouse_y)
            else:
                fc = 0
            
            fill(x*25,y*25,fc)
            rect(x*width/25,y*height/25,width/25,height/25)