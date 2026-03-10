
dvd  = {}

def setup():
    size(1000,500)
    global dvd
    dvd = {
        "x":50,
        "y":50,
        "r":50,
        "h":5,
        "v":5,
    }        
    
def draw():
    background(0)
    
    dvd["x"] += dvd["h"]
    if dvd["x"] > width - dvd["r"] or dvd["x"] < dvd["r"]:
        dvd["h"] *=-1
        
    dvd["y"] += dvd["v"]
    if dvd["y"] > height - dvd["r"] or dvd["y"] < dvd["r"]:
        dvd["v"] *=-1
    
    fill(255)
    square(dvd["x"],dvd["y"],dvd["r"])
    
    fill(0)
    text_align(CENTER,CENTER)
    text_size(25)
    text("DVD",dvd["x"]+dvd["r"]/2,dvd["y"]+dvd["r"]/2)
    
