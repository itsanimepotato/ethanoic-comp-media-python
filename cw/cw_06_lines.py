
lineDict = {}

def setup():
    size(500,500)
    
    global lineDict
    lineDict = {
        "weight":5,
        "r":65,
        "g":53,
        "b":102,
        "opacity":100
        }
    
def draw():
    
    if mouse_x > 200:
        stroke_weight(lineDict["weight"])
    else:
        stroke_weight(1)
        
    if dist(mouse_x, mouse_y, width/2, height/2) < 100:
        stroke(lineDict["r"],lineDict["g"],lineDict["b"])
    else:
        stroke(0,0,255)
        
    line(mouse_x, mouse_y, pmouse_x, pmouse_y)
    