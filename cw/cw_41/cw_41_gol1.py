import numpy as np

percentage = 10
def setup_pixels():
    for x in range(width):
        for y in range(height):
            r = int(random(100))
            if r < percentage:
                stroke(255)
                point(x,y)
    load_np_pixels()
    update_np_pixels()
  
def setup():
    global s
    size(200,200)
    s = [[[0,0,0] for x in range(width)] for y in range(height)]
    background(0)
    load_np_pixels()
    setup_pixels()
  
def evaluate_neighbors():
    global s
    for x in range(1,width-1):
        for y in range(1,height-1):
            s[x][y] = list(np_pixels[y, x, :3])
            
            neighbors = 0
            for i in range(3):
                for j in range(3):
                    a = s[x-1 + i][y-1 + j]
                    print(a)
def transition():
    update_np_pixels()

def draw():
    evaluate_neighbors()
    transition()


