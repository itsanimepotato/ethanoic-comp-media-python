#S7

import numpy as np
import matplotlib.colors as mp

draw_circle_bool = False
chopped_bool = False
wave_bool = False

dc = 50

def setup(): #S4
    size(500,500)
    background(0)
    
    global og
    
    for x in range(width):
        for y in range(height):
            #stroke(remap(x,0,width,0,255),remap(y,0,height,0,255),0)
            stroke(x,y,0)
            point(x,y)
            
    load_np_pixels()
    og = np_pixels.copy()

            
            
def draw(): #S4
    if wave_bool:
        wave()
    
    if draw_circle_bool:
        draw_circle(dc)
        
    if chopped_bool:
        chopped(0,0,int(width/2),int(height/2))

def key_pressed():
    global draw_circle_bool, chopped_bool, wave_bool
    if key == 'd': #S5
        draw_circle_bool = not draw_circle_bool
        print("draw circle")
        
    if key == 'c': #S5
        chopped_bool = not chopped_bool
        print("chopped")

    if key == 'w': #S5
        wave_bool = not wave_bool
        print("wave")

def draw_circle(r):
    # draws a circle filled with random colors #S6
    if is_mouse_pressed: #S5
        for x in range(width):
            for y in range(height):
                d = dist(mouse_x, mouse_y,x,y)
                if d < r:
                    stroke(random(255),random(255),random(255)) #S2 S3
                    point(x,y) #S1
                
    
def chopped(x,y,h,k):
    np_pixels[x:x+h,y:y+k,1] = np.clip(np.round(og[x:x+h,y:y+k,1],-1), 0, 255)
    np_pixels[x:x+h,y:y+k,2] = np.clip(np.round(og[x:x+h,y:y+k,2],-1), 0, 255)
    np_pixels[x:x+h,y:y+k,3] = np.clip(np.round(og[x:x+h,y:y+k,3],-1), 0, 255)
    update_np_pixels()
    
def wave():
    for x in range(width):
        for y in range(height):
            #stroke(remap(x,0,width,0,255),remap(y,0,height,0,255),0)
            stroke((x+frame_count)%255,y,0)
            point(x,y)
            
    load_np_pixels()
            