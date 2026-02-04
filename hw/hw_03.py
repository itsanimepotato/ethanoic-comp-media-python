boxes = 4
box_length = 500/boxes


def setup():
    size(500,500)
    boxes = 4
    box_length = width/boxes
    
    randSquares()
    
def randSquares():
    for x in range(boxes):
        for y in range(boxes):
            rand_num = int(random(4))
            
            if rand_num == 0:
                randArc(x*box_length,y*box_length)
            elif rand_num == 1:
                randTri(x*box_length,y*box_length)
            elif rand_num == 2:
                randQuad(x*box_length,y*box_length)
            else:
                randScribble(x*box_length,y*box_length)
    
def randArc(x,y):
    square(x,y,box_length)
    x1 = x+(box_length/2)
    y1 = y+(box_length/2)
    w = random(box_length)
    h = random(box_length)
    start = random(TWO_PI)
    stop = TWO_PI - start
    mode = random(3)
    if random == 0:
        mode = OPEN
    elif random == 1:
        mode = CHORD
    else:
        mode = PIE
    c = color(random(255),random(255),random(255))
    fill(c)
    arc(x1,y1,w,h,start,stop,mode)
    arc(x1,y1,h,w,stop,start,mode)
    fill(255)
    
def randTri(x,y):
    square(x,y,box_length)
    x1 = x+random(box_length)
    y1 = y+random(box_length)
    
    x2 = x+random(box_length)
    y2 = y+random(box_length)
    
    x3 = x+random(box_length)
    y3 = y+random(box_length)
    
    c = color(random(255),random(255),random(255))
    fill(c)
    triangle(x1,y1,x2,y2,x3,y3)
    fill(255)

    
def randQuad(x,y):
    square(x,y,box_length)
    
    x1 = x+random(box_length)
    y1 = y+random(box_length)
    
    x2 = x+random(box_length)
    y2 = y+random(box_length)
    
    x3 = x+random(box_length)
    y3 = y+random(box_length)
    
    x4 = x+random(box_length)
    y4 = y+random(box_length)
    
    c = color(random(255),random(255),random(255))
    fill(c)
    quad(x1,y1,x2,y2,x3,y3,x4,y4)
    fill(255)
    
def randScribble(x,y):
    square(x,y,box_length)
    begin_shape()
    c = color(random(255),random(255),random(255))
    stroke(c)
    for a in range(int(10)):
        for b in range(int(10)):
            vertex(x+random(box_length),y+random(box_length))
    end_shape(CLOSE)
    stroke(0)

    