
colors = [color(0),
          color(255,0,0),
          color(0,255,0),
          color(0,0,255),
          color(255,255,0),
          color(0,255,255),
          color(255,0,255),
          color(255,165,0),
          color(128,0,128),
          color(255)]

color_bool = []

shape_sel = 0

drawing = False

amt_colors = 10

br_size = 25

def setup():
    size(1000,500)
    global color_bool
    for i in range(10):
        color_bool.append(False)
    color_bool[0] = True
    
def draw():
    color_selector()
    shape_selector()
    
    
    
def color_selector():
    cs_disp()
    cs_logic()
    
def cs_disp():
    
    rect(0,0,width,height/amt_colors)
    for i in range(amt_colors):
        fill(colors[i])
        rect((i*width)/amt_colors, 0, width/amt_colors, height/amt_colors)

def cs_logic():
    for i in range(amt_colors):
        if mouse_x > ((i*width)/amt_colors) and mouse_x < (((i*width)/amt_colors)+(width/amt_colors)) and mouse_y <= height/amt_colors:
            for a in range(amt_colors):
                color_bool[a] = False
            color_bool[i] = True
    
    for i in range(amt_colors):
        if color_bool[i]:
            fill(colors[i])
    
            
def shape_selector():
    if shape_sel == 0:
        square_sel()
    elif shape_sel == 1:
        circle_sel()
    else:
        tri_sel()
        
def square_sel():
    square(mouse_x-br_size/2,mouse_y-br_size/2,br_size)
        
def circle_sel():
    circle(mouse_x,mouse_y,br_size)
        
def tri_sel():
    triangle(mouse_x, mouse_y-br_size/2,mouse_x-br_size/2,mouse_y+br_size/2,mouse_x+br_size/2,mouse_y+br_size/2)
    
def key_pressed():
    if key == "s":
        global shape_sel
        print(shape_sel)
        shape_sel = shape_sel + 1
        
        if shape_sel == 3:
            shape_sel = 0
            

