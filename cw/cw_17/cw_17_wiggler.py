from Wiggler import *

def setup():
    size(250,250)
    global wiggler1, wiggler2, wiggler3
    no_stroke()
    wiggler1 = Wiggler(35, 35)
    wiggler2 = Wiggler(63, 76)
    wiggler3 = Wiggler(25, 53)

def draw():
    if frame_count % 300 == 0:
        background(220)
    wiggler1.animate(wiggler2.x, wiggler2.y)
    wiggler2.animate(wiggler3.x, wiggler3.y)
    wiggler3.animate(wiggler1.x, wiggler1.y)