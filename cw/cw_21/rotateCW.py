def setup():
  size(510,350)

def draw():
  background(220)
  rotate(radians(50))
  rect(0,0,100,20)

#COMPLETE THE FOLLOWING AND LEAVE YOUR ANSWERS AS COMMENTS:

#1. Play with the values for rotation (keep them below 6.28 for now - that's 2 pi!)
#rotates rect
#2. What happens if you move the rectangle to (0, 0)?
#corner of rect at (0,0)
#3. What happens if you add a translation before the rotation? (Try changing where it translates to!)
#moves to other edge
#4. What if you make the rortation the center of the page with a translation?
#rotates from center
#5. What if the rotation is controlled by mouseX or mouseY?
#rotates when mouse changes
#6. What if you plug in radians(50) to rotate()?
#rect at 50 deg