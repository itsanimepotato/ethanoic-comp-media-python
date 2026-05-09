
threshold = 10

def setup():
    global img
    size(500, 500)
    img = load_image("bg.jpg")
    img.resize(width, height)
    image(img, 0, 0)
    load_pixels()
    
 
    
    for x in range(width):
        for y in range(height):
            dr = 0
            dd = 0
            if x+1 >= width:
                dr = 0
            elif y+1 >= height:
                dd = 0
            else:
                dr = avg_c(x+1,y)-avg_c(x,y)
                dd = avg_c(x,y+1)-avg_c(x,y)
            
            if dd > threshold or dr > threshold:
                pixels[x+y*width] = color(255)
            else:
                pixels[x+y*width] = color(0)
    update_pixels()
    
def avg_c(x,y):
    i = x + y * width
    apx = red(pixels[i]) + green(pixels[i]) + blue(pixels[i])
    apx = apx/3
    return apx

