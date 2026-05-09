
import numpy as np

def setup():
    global original
    size(500,500)
    img = load_image("bg.jpg")
    img.resize(width, height)
    image(img, 0, 0)
    load_np_pixels()
    original = np_pixels.copy()

def draw():
    #temp = remap(mouse_x, 0, width, -100, 100)
    #apply_temp(temp)
    
    d = dist(mouse_x, mouse_y, width/2, height/2)
    tin = remap(d, 0, width/2, -100,100)
    apply_tint(tin)

def apply_temp(temp):
    global original

    # 3D array (y, x, color); color->[Alpha,red,green,blue]

    A,r,g,b = 0,1,2,3 # unpack variables for the color indices

    np_pixels[:, :, r] = np.clip(original[:, :, r] + temp, 0, 255)
    np_pixels[:, :, g] = np.clip(original[:, :, g] + temp * 0.4, 0, 255)
    np_pixels[:, :, b] = np.clip(original[:, :, b] - temp, 0, 255)

    update_np_pixels()

def apply_tint(tint_amt):
    global original

    # 3D array (y, x, color); color->[Alpha,red,green,blue]
    A,r,g,b = 0,1,2,3 # unpack variables for the color indices

    
    np_pixels[int(width/2):,:int(height/2),1] = np.clip(original[int(width/2):,:int(height/2),1] + tint_amt, 0, 255)
    np_pixels[int(width/2):,:int(height/2),2] = np.clip(original[int(width/2):,:int(height/2),1] + tint_amt, 0, 255)
    np_pixels[int(width/2):,:int(height/2),3] = np.clip(original[int(width/2):,:int(height/2),1] - tint_amt, 0, 255)
    
    np_pixels[:int(width/2),int(height/2):,1] = np.clip(original[:int(width/2),int(height/2):,2] + tint_amt, 0, 255)
    np_pixels[:int(width/2),int(height/2):,2] = np.clip(original[:int(width/2),int(height/2):,2] - tint_amt, 0, 255)
    np_pixels[:int(width/2),int(height/2):,3] = np.clip(original[:int(width/2),int(height/2):,2] + tint_amt, 0, 255)


    np_pixels[int(width/2):,int(height/2):,1] = np.clip(original[int(width/2):,int(height/2):,3] - tint_amt, 0, 255)
    np_pixels[int(width/2):,int(height/2):,2] = np.clip(original[int(width/2):,int(height/2):,3] + tint_amt, 0, 255)
    np_pixels[int(width/2):,int(height/2):,3] = np.clip(original[int(width/2):,int(height/2):,3] + tint_amt, 0, 255)
    
    np_pixels[:,:,A] += int(random(frame_count%255))

    update_np_pixels()