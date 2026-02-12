
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
    print("cs")
    cs_disp()
    cs_logic()
    
def cs_disp():
    amt_colors = 10
    
    rect(0,0,width,height/amt_colors)
    for i in range(amt_colors):
        fill(colors[i])
        rect((i*width)/amt_colors, 0, width/amt_colors, height/amt_colors)

def cs_logic():
    for i in range(amt_colors):
        if mouseX > ((i*width)/amt_colors) and mouseX < (((i*width)/amt_colors)+(width/amt_colors)) and mouseY <= width/amt_colors:
            for a in range(amt_colors):
                color_bool[a] = False
            color_bool[i] = True
            
            
def shape_selector():
    print("ss")
    if shape_sel == 0:
        square_sel()
    elif shape_sel == 1:
        circle_sel()
    else:
        tri_sel()
        
def square_sel():
    print("square sel")
        
def circle_sel():
    print("circle sel")
        
def tri_sel():
    print("triangle sel")
    
def keyPressed():
    if key == "s":
        shape_sel += 1
        if shape_sel == 3:
            shape_sel == 0
    if key == " ":
        drawing = !drawing
