
def setup():
    size(500, 500)
    rect_mode(CENTER)
    #print("width: " + str(width))
    #print("height: " + str(height))
    
    
def draw():
    background(128)
    fill(255)
    corner_squares()


def corner_squares():
    square(25,25,50)
    square(width-25,25,50)
    square(25,height-25,50)
    square(width-25,height-25,50)
    
