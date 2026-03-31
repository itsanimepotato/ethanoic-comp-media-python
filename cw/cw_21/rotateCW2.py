a = random(degrees(360))

def setup():
  size(510,350)

def draw():
  global a
  background(220)
  
  #2. move the origin to the pivot point (what you want to rotate around)
  translate(width/2,height/2)
  
  #3. then rotate the grid around the pivot point using the variable you created
  rotate(a)
  rect(50,50,100,20)
  
  #4. Increment your rotation variable to make the rotation animated
  
  fill(0)
  rect(0, 0, 100, 100)
  text(a,0,-50)
  a = mouse_y%(width/10)