
def setup():
    size(500,500)
    
    try_rotate()

def draw():
    bg_change()


def try_rotate():
    rect(10,10,20,20)
    rotate(PI/10)
    rect(50,60,30,23)

def bg_change():
    xbgcolor = remap(mouse_x,0,width,0,255)
    ybgcolor = remap(mouse_y,0,height,0,255)
    d = dist(0,0,mouse_x,mouse_y)
    c = color(xbgcolor,ybgcolor,d)
    background(c)