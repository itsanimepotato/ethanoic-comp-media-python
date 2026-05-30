#S7

import numpy as np

draw_circle_bool = False

smooth_bool = False
static_bool = False

tint_amt = 128

#S4
def setup(): 
    size(500,500)
    background(0)
    
    global og
    
    #makes the background
    bg()
    
    load_np_pixels()
    og = np_pixels.copy()
    
    #makes the background leveled
    chopped(0,0,width,height)

            
            
def draw(): 
    if draw_circle_bool:
        draw_circle()
        

#S5
def key_pressed():
    global draw_circle_bool, chopped_bool
    if key == 'd': #turns on the rotating circle
        draw_circle_bool = not draw_circle_bool
        print("draw circle")
        
    if key == '1':
        smooth_bool = True
    if key == '2':
        static_bool = True


def draw_circle():
    #creates a rotating circle around the center #S6
    push_matrix()
    
    r = 50
    translate(width/2,height/2)
    s = r * sin(radians(frame_count)) 
    c = r * cos(radians(frame_count))
    
    color_mode(HSB,360,100,100)
    fill(frame_count%360,100,100)
    circle(c + random(-5,5),s + random(-5,5),50)
    
    pop_matrix()
    
def chopped(x,y,h,k):
    np_pixels[x:x+h,y:y+k,1] = np.clip(np.round(og[x:x+h,y:y+k,1],-1), 0, 255)
    np_pixels[x:x+h,y:y+k,2] = np.clip(np.round(og[x:x+h,y:y+k,2],-1), 0, 255)
    np_pixels[x:x+h,y:y+k,3] = np.clip(np.round(og[x:x+h,y:y+k,3],-1), 0, 255)
    update_np_pixels()
    
def bg():
    global og
    if smooth_bool:
    #makes the background rainbow
        for x in range(width):
            for y in range(height):
                stroke(x,y,0) #S2 + 3
                point(x,y) #S1
        return
    
    if static_bool:
    #makes the background static
        img = load_image("static.jpg")
        img.resize(width,height)
        image(img,0,0)
        
        return
    
    rand = int(random(2))
    if rand == 0:
        print("smooth bg")
        for x in range(width):
            for y in range(height):
                stroke(x,y,0) #S2 + 3
                point(x,y) #S1
    else:
        print("smooth bg")
        img = load_image("static.jpg")
        img.resize(width,height)
        image(img,0,0)
        
        load_np_pixels()
        og = np_pixels.copy()

        np_pixels[int(width/2):,:int(height/2),1] = np.clip(og[int(width/2):,:int(height/2),1] + tint_amt, 0, 255)
        np_pixels[int(width/2):,:int(height/2),2] = np.clip(og[int(width/2):,:int(height/2),1] + tint_amt, 0, 255)
        np_pixels[int(width/2):,:int(height/2),3] = np.clip(og[int(width/2):,:int(height/2),1] - tint_amt, 0, 255)
    
        np_pixels[:int(width/2),int(height/2):,1] = np.clip(og[:int(width/2),int(height/2):,2] + tint_amt, 0, 255)
        np_pixels[:int(width/2),int(height/2):,2] = np.clip(og[:int(width/2),int(height/2):,2] - tint_amt, 0, 255)
        np_pixels[:int(width/2),int(height/2):,3] = np.clip(og[:int(width/2),int(height/2):,2] + tint_amt, 0, 255)


        np_pixels[int(width/2):,int(height/2):,1] = np.clip(og[int(width/2):,int(height/2):,3] - tint_amt, 0, 255)
        np_pixels[int(width/2):,int(height/2):,2] = np.clip(og[int(width/2):,int(height/2):,3] + tint_amt, 0, 255)
        np_pixels[int(width/2):,int(height/2):,3] = np.clip(og[int(width/2):,int(height/2):,3] + tint_amt, 0, 255)
        
        np_pixels[:,:,0] += int(random(frame_count%255))
        
        update_np_pixels()