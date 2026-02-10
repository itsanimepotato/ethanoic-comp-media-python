def setup():
    size(400,600)
def draw():
    background(220)
    text(str(mouse_x) + ", " + str(mouse_y), 20, 20)
    
    global left, middle, right, top, bottom, rad
    
    left = 100
    middle = 200
    right = 300
    
    top = 200
    bottom = 300
    rad = 75
    
    circle(100, 200, 75) #top left
    circle(200, 200, 75) #top middle
    circle(300, 200, 75) #top right
    circle(100, 300, 75) #bottom left
    circle(200, 300, 75) #bottom middle
    circle(300, 300, 75) #bottom right
    
    fill_color(left,bottom)
    
    fill_color(middle,bottom)
    
    fill_color(right,bottom)
    
    fill_color(left,top)
    
    fill_color(middle,top)
    
    fill_color(right,top)
    

    
def hover_rad(x,y):
    if dist(x,y,mouse_x,mouse_y) < rad/2:
        return True
    else:
        return False
    
def fill_color(x,y):
    if hover_rad(x,y):
        if y == top:
            if x == left:
                fill(135,206,235)
                circle(left, top, rad)
            if x == middle:
                fill(128,0,128)
                circle(left, bottom, rad)
                circle(right, bottom, rad)
            if x == right:
                fill(0)
                circle(right, top, rad)
                circle(middle, bottom, rad)
        if y == bottom:
            if x == left:
                fill(255,0,0)
                circle(left, top, rad)
                circle(middle, top, rad)
                circle(right, top, rad)                
            if x == middle:
                fill(0,128,0)
                circle(left, middle, rad)
            if x == right:
                fill(255,165,0)
                circle(left, bottom, rad)
    fill(255)

                
