
def setup():
    global img
    size(500, 500)
    img = load_image("berry.png")
    img.resize(width, height)
    image(img, 0, 0)
    load_pixels()
    
    quadrant_tint(0,0,int(width/2),int(height/2),1,1,1)
    quadrant_tint(int(width/2),0,int(width),int(height/2),100,1,1)
    quadrant_tint(int(width/2),int(height/2),int(width),int(height),50,1,50)
    quadrant_tint(0,int(height/2),int(width/2),int(height),1,1,100)

    update_pixels()


def quadrant_tint(x0,y0,x1,y1,rm,gm,bm):
    # 1rst quadrant (red tint)
    for x in range(x0, x1):
        for y in range(y0,y1):
            #location of (x,y) in the 1D list
            loc = x + y * width
            #pixel's color
            clr = pixels[loc]
            # red tint
            nr = red(clr) * rm      # new red
            ng = green(clr) * gm    # new green
            nb = blue(clr) * bm     # new blue
            #load the new color
            pixels[loc] = color(nr%255, ng%255, nb%255)
