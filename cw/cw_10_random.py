
star_list = []

def setup():
    size(500,500)
    background(0)
    
    for i in range(500):
        star_list.append({
            "x":random(width),
            "y":random(height),
            "c":color(random(255),random(255),random(255))})
    
    
def draw():
    if key == 'f':
        fake_stars()
    else:
        real_stars()

amt = 20

def fake_stars():
    if frame_count % 20 == 0:
        background(0)
    for x in range(int(width/amt)):
        for y in range(int(height/amt)):
            rand = random(500)
            if rand > 400:
                rand_alpha = random(100)*2
                stroke(255,255,255,rand_alpha)
                stroke_weight(random(10))
                point(x*width/amt+random(-width/amt,width/amt),y*height/amt+random(-height/amt,height/amt))
                
def real_stars():
    for i in range(len(star_list)):
        stroke(star_list[i]["c"])
        stroke_weight(random(10))
        point(star_list[i]["x"],star_list[i]["y"])