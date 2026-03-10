circ1 = {
      "x":0,
      "xSpeed":2,
      }
def setup():
    size(510,350)
def draw():
    global circ1
    background(220)
    circle(circ1["x"], 50, 20)
    circ1["x"] += circ1["xSpeed"] #Move slightly to right
    if circ1["x"] > width:
        circ1["x"] = 0
