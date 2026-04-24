
def setup():
    size(500,500)
    global img
    img = load_image("berry.png")
    img.resize(width,height)
    image(img,0,0)

        
def draw():
    color_mode(HSB,360,100,100)
    tint(frame_count%360,100,100,128)
    image(img,0,0)
    color_mode(RGB,255,255,255)