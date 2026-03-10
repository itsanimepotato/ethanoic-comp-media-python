circ1 = {
      "x":0,
      "xSpeed":random(5),
      }

circ2 = {
      "x":0,
      "xSpeed":random(5),
      }

circ3 = {
      "x":0,
      "xSpeed":random(5),
      }

circ4 = {
      "x":0,
      "xSpeed":random(5),
      }

circ5 = {
      "x":0,
      "xSpeed":random(5),
      }

circs = [circ1,circ2,circ3,circ4,circ5]

def setup():
    size(510,350)
    
def draw():
    global circ1
    background(220)
    for i in range(5):
        circ_row(circs[i], i*50+50)

def circ_row(circ_list, y):
    fill(circ_list["x"],circ_list["x"],0)
    circle(circ_list["x"], y, 20)
    circ_list["x"] += circ_list["xSpeed"]
    if circ_list["x"] > width:
        circ_list["x"] = 0