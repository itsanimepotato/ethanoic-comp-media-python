
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

def setup():
    size(1000,1000)
    
    
def draw():
    color_selector()
    shape_selector()
    
    
    
def color_selector():
    print("cs")
    cs_disp()
    
def cs_disp():
    amt_colors = 10
    
    rect(0,0,width,height/amt_colors)
    for i in range(amt_colors):
        fill(colors[i])
        rect((i*width)/amt_colors, 0, width/amt_colors, height/amt_colors)


def shape_selector():
    print("ss")
    square_sel()
    circle_sel()
    tri_sel()
        
def square_sel():
    print(2)
        
def circle_sel():
    print(2)
        
def tri_sel():
    print(2)
        
        