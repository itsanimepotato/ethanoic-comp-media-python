

def setup():
    size(500,500)
    global press
    press = False

    
def draw():
    background(0)
    fill(255)
    rect(150,50,200,400)
    
    if press == True:
        circ_color(150,press,color(255,0,0))
        circ_color(250,press,color(255,255,0))
        circ_color(350,press,color(0,255,0))
        print(press)
    else:
        fill(255,0,0,50)
        circle(250,150,100)
        fill(255,255,0,50)
        circle(250,250,100)
        fill(0,255,0,50)
        circle(250,350,100)
        print(press)

    
def circ_color(y,press,c):
    fill(c)
    circle(250,y,100)

def mouse_pressed():
    press = True
    print(press)
    