import numpy as np

effect = False

gray = False
invert = False
level = False
img = None

def setup():
    global img, og
    size(500, 500)
    img = load_image("bg.jpg")
    img.resize(width, height)
    image(img, 0, 0)
    load_np_pixels()
    
    og = np_pixels.copy()

def draw():
    global img, effect
    
    if effect:
        load_np_pixels()
        if gray:
            #apply_filter(GRAY)
            gray_filter(int(width/2),0,int(width/2),int(height/2))
            print("gray")

        if invert:
            #apply_filter(INVERT)
            invert_filter(0,0,int(width/2),int(height/2))
            print("invert")
            
        if level:
            level_filter(0,int(height/2),int(width/2),int(height/2))
            print("level")
            
        effect = not effect

def key_pressed():
    global img, effect, gray, invert, level
    if key == "e":
        effect = not effect
    
    if key == "g":
        gray = not gray
        
    if key == "i":
        invert = not invert
        
    if key == "l":
        level = not level
        
    if key == "r":
        img = load_image("bg.jpg")
        img.resize(width, height)
        image(img, 0, 0)
        
def invert_filter(x,y,h,k):
    np_pixels[x:x+h,y:y+k,1] = np.clip(255-og[x:x+h,y:y+k,1], 0, 255)
    np_pixels[x:x+h,y:y+k,2] = np.clip(255-og[x:x+h,y:y+k,2], 0, 255)
    np_pixels[x:x+h,y:y+k,3] = np.clip(255-og[x:x+h,y:y+k,3], 0, 255)
    update_np_pixels()
    
def gray_filter(x,y,h,k):
    avg = og[x:x+h,y:y+k,1] + og[x:x+h,y:y+k,2] + og[x:x+h,y:y+k,3]
    avg = avg/3

    np_pixels[x:x+h,y:y+k,1] = np.clip(avg, 0, 255)
    np_pixels[x:x+h,y:y+k,2] = np.clip(avg, 0, 255)
    np_pixels[x:x+h,y:y+k,3] = np.clip(avg, 0, 255)
    update_np_pixels()
    
def level_filter(x,y,h,k):
    np_pixels[x:x+h,y:y+k,1] = np.clip(np.round(og[x:x+h,y:y+k,1],-2), 0, 255)
    np_pixels[x:x+h,y:y+k,2] = np.clip(np.round(og[x:x+h,y:y+k,2],-2), 0, 255)
    np_pixels[x:x+h,y:y+k,3] = np.clip(np.round(og[x:x+h,y:y+k,3],-2), 0, 255)
    update_np_pixels()