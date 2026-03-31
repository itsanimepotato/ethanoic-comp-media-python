
def setup():
    size(500,500)
    
def draw():
    background(0)
    translate(width/2,height/2)
    #rect_mode(CENTER)
    for i in range(100):
        spiral(i)
    
def spiral(i):
    color_mode(HSB,100,100,100)
    fill(i,100,100,i*0.9)
    rect(0,0,25,i+10*i)
    rotate(radians(frame_count/180))