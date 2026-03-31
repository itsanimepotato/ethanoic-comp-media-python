
star_list = []
num_stars = 500

def setup():
    size(500,500)
    background(0)
    
    for i in range(num_stars):
        star_list.append({
            "x":random(width),
            "y":random(height),
            "c":color(random(255))})
    
    
def draw():
    real_stars()
    
def real_stars():
    background(0)
    for i in range(len(star_list)):
        rand_weight = 2
        if frame_count % 2 == 0:
            rand_weight = random(5)
        
        stroke_weight(rand_weight)
        stroke(star_list[i]["c"])
        point(star_list[i]["x"],star_list[i]["y"])
        