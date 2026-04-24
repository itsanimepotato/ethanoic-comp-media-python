
def setup():
    size(500,500)
    global img
    img = load_image("IMAGE PATH HERE")
    img.resize(width,height)
    image(img,0,0)
    pxls = load_pixels()
    
    r,c = (width,height)
    arr = []
    for x in range(width):
        row = []
        for y in range(height):
            row.append(get_pixels(x,y))
        arr.append(row)
        
