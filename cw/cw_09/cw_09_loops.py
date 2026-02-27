
def setup():
    size(500,500)
    

def draw():
    circle_grid()
    
def circle_grid():
    r=width/5
    
    for x in range(5):
        for y in range(5):
            for i in range(int(r)):
                rad_change = r/5
                rad = r+random(-rad_change,rad_change)
                color_mode(HSB, 360, 100, 255)
                fill(0,0,random(rad))
            circle(x*r+r/2,y*r+r/2,rad)