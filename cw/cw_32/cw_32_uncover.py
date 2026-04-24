
def setup():
    size(500,500)
    global arr
    background(0)
    img = load_image("berry.png")
    img.resize(width,height)
    image(img,0,0)
    pxls = load_pixels()
    no_stroke()
    
    arr = []
    for x in range(width):
        row = []
        for y in range(height):
            #print(f"{x},{y}:{pixels[x*y+x]}")
            row.append(get_pixels(x,y))
        arr.append(row)
    
    background(255)
    
def mouse_dragged():
    if mouse_x >= width or mouse_x <= 0 or mouse_y >= height or mouse_y <= 0:
        return 0
    
    fill(arr[mouse_x][mouse_y])
    circle(mouse_x,mouse_y,25)