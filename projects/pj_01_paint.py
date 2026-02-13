
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
adj_size = 10
adj_vert = 5


shape_norm = {
    "br_size":25,
    "br_color":color(0)
    }

shape_stats = shape_norm

scribble_norm = {
    "w":1, # weight
    "c":0,  # color
    "v":5  # vertices
    }

scribble_stats = scribble_norm

def setup():
    size(1000,1000)
    background(255)
    
    fill(0)
    start_info()
    
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
        stroke(0)
        stroke_weight(1)
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
    if drawing:
        if shape_sel == 0:
            square_sel()
        elif shape_sel == 1:
            circle_sel()
        elif shape_sel == 2:
            scr_sel()
        else:
            tri_sel()
        
def square_sel():
    square(mouse_x-shape_stats["br_size"]/2,mouse_y-shape_stats["br_size"]/2,shape_stats["br_size"])
        
def circle_sel():
    circle(mouse_x,mouse_y,shape_stats["br_size"])
        
def tri_sel():
    triangle(mouse_x, mouse_y-shape_stats["br_size"]/2,mouse_x-shape_stats["br_size"]/2,mouse_y+shape_stats["br_size"]/2,mouse_x+shape_stats["br_size"]/2,mouse_y+shape_stats["br_size"]/2)
    
def scr_sel():
    randScribble(mouse_x, mouse_y)
    
def randScribble(x,y):
    begin_shape()
    c = scribble_stats["c"]
    stroke(c)
    stroke_weight(scribble_stats["w"])
    for a in range(int(random(5))):
        for b in range(int(random(5))):
            vertex(x+random(shape_stats["br_size"])-shape_stats["br_size"]/2,y+random(shape_stats["br_size"])-shape_stats["br_size"]/2)
    end_shape(CLOSE)
    stroke(0)
    stroke_weight(1)

def key_pressed():
    global shape_sel
    global drawing
    global shape_stats
    global scribble_stats
    
    #brush
    if key == "b":
        print(shape_sel)
        shape_sel = shape_sel + 1
        
        if shape_sel == 3:
            shape_sel = 0
            
    #reset
    if key == "r":
        background(255)
        shape_sel = 0
        shape_stats = shape_norm
        scribble_stats = scribble_norm
        start_info()
        
    #start/stop
    if key == " ":
        drawing = not drawing
        
    #big
    if key_code == UP and shape_stats["br_size"] < height-height/10:
        shape_stats["br_size"] += adj_size
        
    #small
    if key_code == DOWN and shape_stats["br_size"] > 5:
        shape_stats["br_size"] -= adj_size

    #big
    if key_code == LEFT:
        print("more vert")
        print(scribble_stats["v"])
        scribble_stats["v"] += adj_vert
        
    #small
    if key_code == RIGHT and scribble_stats["v"] > 5:
        print("less vert")
        print(scribble_stats["v"])
        scribble_stats["v"] -= adj_vert
        
    #erase
    if key == "e":
        no_stroke()
        fill(255)
        circle(mouse_x,mouse_y,shape_stats["br_size"])


def start_info():
    fill(0)
    text_align(LEFT,TOP)
    text_size(25) #make font bigger
    
    #put text in bottom left (press this to do this)
    text("Press LEFT to make more vertices of scribble", 0, height-50)
    text("Press RIGHT to make less vertices of scribble", 0, height-25)
    text("Press DOWN to make brush smaller", 0, height-75)
    text("Press UP to make brush bigger", 0, height-100)
    text("Press SPACE to draw", 0, height-125)
    
    #put text in bottom right
    text_align(RIGHT,TOP)
    text("Press r to reset canvas", width, height-25)
    text("Press b to change brush", width, height-50)
    text("Press e to erase in a circle (same as brush size)", width, height-75)

