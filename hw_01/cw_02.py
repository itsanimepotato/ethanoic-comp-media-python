
side_length = 50

def setup():
    size(500, 500)
    rect_mode(CENTER)
    #print("width: " + str(width))
    #print("height: " + str(height))
    
    
def draw():
    background(128)
    fill(255)
    corner_squares()
    inside_squares()


def corner_squares():
    square(25,25,side_length)
    square(width-25,25,side_length)
    square(25,height-25,side_length)
    square(width-25,height-25,side_length)
    

def inside_squares():
    square(width/2-0.5*side_length,height/2-0.5*side_length,side_length)
    square(width/2+0.5*side_length,height/2-0.5*side_length,side_length)
    square(width/2-0.5*side_length,height/2+0.5*side_length,side_length)
    square(width/2+0.5*side_length,height/2+0.5*side_length,side_length)

