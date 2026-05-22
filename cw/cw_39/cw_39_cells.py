import numpy as np

colors = [
    np.array([0, 255, 0, 255]),
    np.array([0, 100, 0, 255]),
    np.array([255, 200, 0, 255]),
    np.array([80, 65, 0, 255])
]

def setup():
    size(500, 500)
    global s
    s = np.zeros((width, height, 4), dtype=int)
    setup_pixels()
    
def setup_pixels():
    global s
    for x in range(width):
        for y in range(height):
            rand_color = colors[int(random(len(colors)))]
            s[x, y] = rand_color
    update_pixels()

def draw():
    evaluate_neighbors()
    transition()

def evaluate_neighbors():
    global s, new_s
    new_s = np.zeros_like(s)
    
    for x in range(width):
        for y in range(height):
            x_min = max(0, x-1)
            x_max = min(width, x+2)
            y_min = max(0, y-1)
            y_max = min(height, y+2)
            
            neighborhood = s[x_min:x_max, y_min:y_max].reshape(-1, 4)
            
            counts = {}
            for c in neighborhood:
                k = tuple(c)
                counts[k] = counts.get(k, 0) + 1
            
            mode_color = max(counts, key=counts.get)
            new_s[x, y] = np.array(mode_color)

def transition():
    global s
    s = new_s.copy()
    change_pixels()

def change_pixels():
    load_pixels()
    for x in range(width):
        for y in range(height):
            c = color(*s[x, y])
            pixels[y * width + x] = c
    update_pixels()