#S7

import numpy as np

draw_circle_bool = False
draw_scribble_bool = False
fill_bool = False
tint_amt = 128

#S10
class Text:
    
    def __init__(self, w, h):
        #initializes variables
        self.w = w
        self.h = h
        
    def display(self):
        #displays text #S6
        text_align(CENTER,CENTER)
        text_size(20)
        
        push_matrix()
        color_mode(HSB,360,100,100)
        fill(frame_count%360,100,100)
        text("Press C to make a rotating random circle!", self.w, self.h)
        
        color_mode(HSB,360,100,100)
        fill(2*frame_count%360,100,100)
        text("Press S to make scribbles!", self.w, self.h+25)
        
        color_mode(HSB,360,100,100)
        fill(3*frame_count%360,100,100)
        text("Press F to add color (to edge of scribble and inside of circle)", self.w, self.h+50)
        
        fill(4*frame_count%360,100,100)
        text("Press 1 to reset to either background", self.w, self.h+75)
        pop_matrix()


def setup(): #S4
    size(500,500)
    background(0)
    
    global og, txt
    
    #makes the background
    bg()
    
    load_np_pixels()
    og = np_pixels.copy()
    
    #makes the background leveled
    chopped(0,0,width,height)
    
    txt = Text(width/2, height/2 + height/4)
    txt.display()
    
            
def draw(): #S4
    #separating to separate functions
    if draw_circle_bool: 
        draw_circle()
        
    if draw_scribble_bool:
        draw_scribble(mouse_x, mouse_y)
    
    txt.display() #S10

def key_pressed(): #S5
    global draw_circle_bool, draw_scribble_bool, fill_bool, chopped_bool
    if key == 'c': #turns on the rotating circle #S6
        draw_circle_bool = not draw_circle_bool
        print("draw circle")
    if key == 's': # turns on random scribble #S6
        draw_scribble_bool = not draw_scribble_bool
        print("draw scribble")
    if key == 'f': # turns on fill bool #S6
        fill_bool = not fill_bool
        print("fill")
    if key == "1": # resets the background #S6
        bg()
        print("bg")
    if key == "l": # levels out the colors #S6
        load_np_pixels()
        og = np_pixels.copy()
        chopped(0,0,width,height)
        
def draw_circle():
    #creates a rotating circle around the center #S6
    push_matrix() #S11
    
    r = 50
    translate(width/2,height/2) #S11
    s = r * sin(radians(frame_count)) #S9
    c = r * cos(radians(frame_count)) #S9
    
    if fill_bool:
        color_mode(HSB,360,100,100) #S3
        fill(frame_count%360,100,100) #S2
    else:
        color_mode(RGB,255,255,255) #S3
        fill(0,0,0,0) #S2
    circle(c + random(-5,5),s + random(-5,5),50) #S9
    
    pop_matrix()

def draw_scribble(x,y):
    #makes a scribble #S6
    difference = 50
    stroke_weight(1)
    
    begin_shape() #S1
    c = color(random(255),random(255),random(255))
    if fill_bool:
        color_mode(RGB,255,255,255)
        c = color(random(255),random(255),random(255))
    else:
        color_mode(RGB,255,255,255)
        c = color(0,0,0,0)
    stroke(c)
    
    for a in range(int(10)):
        for b in range(int(10)):
            vertex(x+random(-int(random(difference)),int(random(difference))),y+random(-int(random(difference)),int(random(difference))))
    end_shape(CLOSE)
    stroke(0)


def chopped(x,y,h,k):
    #levels out colors #S6
    #S12
    np_pixels[x:x+h,y:y+k,1] = np.clip(np.round(og[x:x+h,y:y+k,1],-1), 0, 255)
    np_pixels[x:x+h,y:y+k,2] = np.clip(np.round(og[x:x+h,y:y+k,2],-1), 0, 255)
    np_pixels[x:x+h,y:y+k,3] = np.clip(np.round(og[x:x+h,y:y+k,3],-1), 0, 255)
    update_np_pixels()
    
def bg():
    global og
    color_mode(RGB,255,255,255)
    
    #changes background
    #if smooth then the rainbow bg
    #if static then the static picture
    
    rand = int(random(4))
    print(rand)
    if rand == 0:
        print("smooth color bg")
        background(0)
        for x in range(width):
            for y in range(height):
                stroke(x,y,0) #S2 + 3
                point(x,y) #S1
    elif rand == 1:
        print("static color bg")
        img = load_image("static.jpg") #S8
        img.resize(width,height)
        image(img,0,0)
    
    elif rand == 2:
        print("smooth gray bg")
        background(0)
        for x in range(width):
            for y in range(height):
                stroke(x,y,0) #S2 + 3
                point(x,y) #S1
        #S12
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
    else:
        print("static gray bg")
        img = load_image("static.jpg") #S8
        img.resize(width,height)
        image(img,0,0)
        
        #S12
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
        