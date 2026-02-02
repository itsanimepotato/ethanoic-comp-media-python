
side_length = 50
offset = 25

def setup():
    size(500, 500)
    rect_mode(CENTER)
    #print("width: " + str(width))
    #print("height: " + str(height))
    
    
def draw():
    background(220)
    fill(255)
    corner_squares()
    inside_squares()
    
    semicircle(width/2,50)
    stroke(0)
    fill(255)


def corner_squares():
    square(offset,offset,side_length)
    square(width-offset,offset,side_length)
    square(offset,height-offset,side_length)
    square(width-offset,height-offset,side_length)
    
    circle(offset,offset,side_length)
    circle(width-offset,offset,side_length)
    circle(offset,width-offset,side_length)
    circle(width-offset,width-offset,side_length)

def inside_squares():
    square(width/2-0.5*side_length,height/2-0.5*side_length,side_length)
    square(width/2+0.5*side_length,height/2-0.5*side_length,side_length)
    square(width/2-0.5*side_length,height/2+0.5*side_length,side_length)
    square(width/2+0.5*side_length,height/2+0.5*side_length,side_length)


def semicircle(x,y):
    stroke(0)
    fill(255)
    circle(x,y,side_length)
    
    no_stroke()
    fill(220)
    square(x,y+side_length/2,side_length+2)
    

