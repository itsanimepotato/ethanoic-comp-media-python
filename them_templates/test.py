def setup():
    size(400,400)
    
def draw():
  background(0)
    
  stroke_weight(7)

  color_mode(HSB,360,100,100)
  stroke(0,100,100) #red

  color_mode(RGB,255,255,255)
  fill(0,255,0) #blue

  #head
  rect(100,100,200,200)

  #hat
  fill(60,0,20)
  arc(100,100,200,100,PI,TWO_PI,CHORD)
  
  #eyes on head
  fill(0)
  circle(150,150,20)
  circle(250,150,20)

  #eyes on hat
  circle(150,75,10)
  circle(250,75,10)
