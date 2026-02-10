def hover_rad(x,y,r):
    if dist(x,y,mouse_x,mouse_y) < r:
        return True
    else:
        return False