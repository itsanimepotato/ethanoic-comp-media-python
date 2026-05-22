
color_pts_enabled = False
background_pts_enabled = False
static_full_pts_enabled = False
full_pts_enabled = False
recip_full_pts_enabled = False


def setup():
    size(255, 255)
    background(255)


def draw():
    if color_pts_enabled:
        color_pts()

    if background_pts_enabled:
        background_pts()

    if static_full_pts_enabled:
        static_full_pts()

    if full_pts_enabled:
        full_pts()

    if recip_full_pts_enabled:
        recip_full_pts()


def color_pts():
    c = color(mouse_x, 0, mouse_y)
    stroke(c)
    point(mouse_x, mouse_y)


def static_full_pts():
    for w in range(width):
        for l in range(height):

            c = color(
                w,
                random_int(mouse_x + mouse_y) % 255,
                l
            )

            stroke(c)
            point(w, l)


def full_pts():
    for w in range(width):
        for l in range(height):

            c = color(w, 0, l)

            stroke(c)
            point(w, l)


def recip_full_pts():
    for w in range(width):
        for l in range(height):

            c = color(w, l, (w * l) / 2)

            stroke(c)
            point(w, l)


def key_pressed():
    global color_pts_enabled
    global background_pts_enabled
    global static_full_pts_enabled
    global full_pts_enabled
    global recip_full_pts_enabled

    if key == '1':
        background(255)

    if key == 'c':
        color_pts_enabled = not color_pts_enabled

    if key == 's':
        static_full_pts_enabled = not static_full_pts_enabled

    if key == 'f':
        full_pts_enabled = not full_pts_enabled

    if key == 'r':
        recip_full_pts_enabled = not recip_full_pts_enabled