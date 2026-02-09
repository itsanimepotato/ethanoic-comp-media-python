
scribble_template = {}
pressed = False

def setup():
    size(500,500)
    global scribble_template
    scribble_template = {
        "w":1, # wei
        "c":0  #col
        }
    
    
def draw():
    randScribble(mouse_x, mouse_y)
    
def randScribble(x,y):
    begin_shape()
    if not pressed:
        c = scribble_template["c"]
        stroke(c)
        stroke_weight(scribble_template["w"])
        for a in range(int(random(10))):
            for b in range(int(random(10))):
                vertex(x+random(25)-25/2,y+random(25)-25/2)
    else:
        c = color(random(255),random(255),random(255))
        stroke(c)
        stroke_weight(random(5))
        for a in range(int(random(10))):
            for b in range(int(random(10))):
                vertex(x+random(50)-50/2,y+random(50)-50/2)
    end_shape(CLOSE)
    stroke(0)
    
def mouse_pressed():
    global pressed
    pressed = !pressed

def mouse_released():
    global pressed
    pressed = !pressed

    