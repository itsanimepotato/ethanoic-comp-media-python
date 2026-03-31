from Bubble import *

bubbles = []
bubble_amt = 25

def setup():
    size(500, 500)
    global bubbles
    for i in range(bubble_amt):
        bubbles.append(Bubble())

def draw():
    background(255)

    for b in bubbles:
        b.move()

    for i in range(len(bubbles)):
        for j in range(i + 1, len(bubbles)):
            bubbles[i].collide(bubbles[j])

    for b in bubbles:
        b.display()

def mouse_pressed():
    global bubbles
    for b in bubbles[:]:
        if dist(mouse_x, mouse_y, b.x, b.y) < b.r:
            bubbles.remove(b)