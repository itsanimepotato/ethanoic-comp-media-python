angle = 0

def setup():
    size(500,500)
    
def draw():
    global angle
    background(0)
    push_matrix()
    translate(width/2,height/2)
    color_mode(HSB,360,100,100)
    for i in range(8):
        fill((i*angle)%360,100,100)
        rotate(TWO_PI / 8)
        pulse = 1 + 0.3 * sin(angle + i * 0.5)
        scale(pulse)
        ellipse(80, 0, 60, 30)
    angle += 0.05
    pop_matrix()