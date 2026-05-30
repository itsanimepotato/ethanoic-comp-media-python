def randScribble(x,y):
    begin_shape()
    c = color(random(255),random(255),random(255))
    stroke(c)
    for a in range(int(10)):
        for b in range(int(10)):
            vertex(x+random(box_length),y+random(box_length))
    end_shape(CLOSE)
    stroke(0)

    