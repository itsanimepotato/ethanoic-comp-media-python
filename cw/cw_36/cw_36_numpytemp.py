
import numpy as np

def setup():
    global img
    size(500, 500)
    img = load_image("bg.jpg")
    img.resize(width, height)
    image(img, 0, 0)
    load_np_pixels()
    
def draw():
    unmouse_x = width-mouse_x
    
    np_pixels[int(width/2):,:int(height/2),1] = mouse_x % 255
    np_pixels[int(width/2):,:int(height/2),3] = unmouse_x % 255

    np_pixels[:int(width/2),int(height/2):,1] = unmouse_x % 255
    np_pixels[:int(width/2),int(height/2):,3] = mouse_x % 255 

    np_pixels[int(width/2):,int(height/2):,1] = 128
    np_pixels[int(width/2):,int(height/2):,3] = 128
        
    update_np_pixels()
    
