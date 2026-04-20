
class Bar:
    def __init__(self,x,y,rw,rh,t):
        self.x = x
        self.y = y
        self.rw = rw
        self.rh = rh
        self.t = t
        
    def time_drop(self):
        fill(255)
        if self.t == "Hour":
            circle(self.x,(self.y-self.rh)+((self.y)/24)*hour()+self.rw,self.rw*2)
        if self.t == "Min":
            circle(self.x,(self.y-self.rh)+((self.y)/60)*minute()+self.rw,self.rw*2)
        if self.t == "Sec":
            circle(self.x,(self.y-self.rh)+((self.y)/60)*second()+self.rw,self.rw*2)
        
    def time_text(self):
        if hour() >= 6 and hour() <= 18:
            fill(0)
        else:
            fill(255)
        
        text_align(CENTER,CENTER)
        text_size(50)
        if self.t == "Hour":
            text(hour(),self.x,(self.y-self.rh)+((self.y)/24)*hour()+self.rw)
        if self.t == "Min":
            text(minute(),self.x,(self.y-self.rh)+((self.y)/60)*minute()+self.rw)
        if self.t == "Sec":
            text(second(),self.x,(self.y-self.rh)+((self.y)/60)*second()+self.rw)
        
    def time(self):
        self.time_drop()
        self.time_text()
    
    def display(self):
        color_mode(HSB,120,100,100)
        fill(frame_count%120,100,100)
        color_mode(RGB,255,255,255)
        
        rect_mode(RADIUS)
        rect(self.x,self.y,self.rw,self.rh)
        
        if hour() >= 6 and hour() <= 18:
            fill(0)
        else:
            fill(255)
        
        self.time()
        
        text_align(CENTER,CENTER)
        text_size(25)
        text(self.t,self.x,self.y-self.rh-25)
        
        
def setup():
    size(500,1000)
    global hr,mn,sec,dx,dy
    
    dx = width/4
    dy = 300
    
    hr = Bar(dx,height/2,50,dy,"Hour")
    mn = Bar(2*dx,height/2,50,dy, "Min")
    sec = Bar(3*dx,height/2,50,dy, "Sec")
    
    
def draw():
    
    if hour() >= 6 and hour() <= 18:
        background(255)
    else:
        background(0)
    
    global hr,mn,sec,dx,dy
    hr.display()
    mn.display()
    sec.display()
    
    if hour() >= 6 and hour() <= 18:
        fill(0)
    else:
        fill(255)
    text_size(50)
    text(":", dx+width/8, height/2)
    text(":", 2*dx+width/8, height/2)


