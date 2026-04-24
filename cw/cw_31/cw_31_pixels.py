
def setup():
    size(100,100)
    img = load_image("berry.png")
    img.resize(width,height)
    image(img,0,0)
    pxls = load_pixels()
    
    r,c = (width,height)
    arr = []
    for x in range(width):
        row = []
        for y in range(height):
            #print(f"{x},{y}:{pixels[x*y+x]}")
            row.append(get_pixels(x,y))
        arr.append(row)
    print(arr)
    print(arr[35])
    print(arr[35][36])