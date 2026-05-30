import numpy as np

def setup_pixels():
    
    haitch(width/2,height/2,20)
    
    load_np_pixels()
    update_np_pixels()

def haitch(x,y,s):
    topX = x - s/2
    topY = y - s/2
    
    for l in range(s):
        for w in range(s):
            stroke(255,0,0)
            point(topX+w,topY+l)
    
    cutout = int(s/3)
    
    for w in range(cutout,2*cutout,1):
        stroke(0)
        for l in range(0,cutout,1):
            point(topX+w,topY+l)
        for l in range(cutout*2,s,1):
            point(topX+w,topY+l)
        
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

def transition():
    global s
    for x in range(width):
        for y in range(height):
            arr = np.array([s[x][y]])
            np_pixels[x, y, :] = np.append(arr.mean(axis=0), 255)
    update_np_pixels()

def draw():
    evaluate_neighbors()
    transition()