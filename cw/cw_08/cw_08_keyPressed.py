
circ_size = {}

adj_size = 5

def setup():
    size(500,500)
    global circ_size
    circ_size = {
        "r":200
        }
    
def draw():
    background(0)
    circle(width/2,height/2,circ_size["r"])
    if is_key_pressed():
        if key == 'b' and circ_size["r"] < width:
            circ_size["r"] += adj_size
        if key == 's' and circ_size["r"] > 5:
            circ_size["r"] -= adj_size