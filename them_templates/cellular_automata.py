import numpy as np

def setup_pixels():
    update_np_pixels()
  
def setup():
    global s
    size(200,200)
    s = [ [ ] ]
    background(0)
    load_np_pixels()
    setup_pixels()
  
def evaluate_neighbors():
    global s
    for x in range(1,width-1):
        for y in range(1,height-1):
            s[x][y] = list(np_pixels[y, x, :3])

def transition():

    update_np_pixels()

def draw():
    evaluate_neighbors()
    transition()



