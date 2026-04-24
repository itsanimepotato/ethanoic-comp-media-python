# ---- Color Selector Class ----
class ColorSelector:
    def __init__(self, palette):
        self.colors = palette
        self.selected = 0
        self.amt = len(palette)

    def display(self):
        for i, c in enumerate(self.colors):
            fill(c)
            stroke(0)
            stroke_weight(1)
            rect((i * width) / self.amt, 0, width / self.amt, height / self.amt)

    def handle_click(self, mx, my):
        if my <= height / self.amt:
            for i in range(self.amt):
                if (mx > (i * width) / self.amt and
                    mx < ((i * width) / self.amt) + (width / self.amt)):
                    self.selected = i

    def current_color(self):
        return self.colors[self.selected]


# ---- Brush Class ----
class Brush:
    def __init__(self):
        self.size = 25
        self.mode = 0  # 0 square, 1 circle, 2 scribble, 3 triangle

    def next_mode(self):
        self.mode = (self.mode + 1) % 4

    def grow(self):
        if self.size < height - height / 10:
            self.size += 10

    def shrink(self):
        if self.size > 5:
            self.size -= 10

    def draw(self, x, y, color, scribble):
        fill(color)
        stroke(color)

        if self.mode == 0:
            square(x - self.size/2, y - self.size/2, self.size)
        elif self.mode == 1:
            circle(x, y, self.size)
        elif self.mode == 2:
            scribble.draw(x, y, self.size, color)
        else:
            triangle(
                x, y - self.size/2,
                x - self.size/2, y + self.size/2,
                x + self.size/2, y + self.size/2
            )


# ---- Scribble Class ----
class Scribble:
    def __init__(self):
        self.weight = 1
        self.vertices = 5

    def more_vertices(self):
        self.vertices += 5

    def fewer_vertices(self):
        if self.vertices > 5:
            self.vertices -= 5

    def draw(self, x, y, size, color):
        stroke(color)
        stroke_weight(self.weight)
        no_fill()

        begin_shape()
        for _ in range(self.vertices):
            vx = x + random(size) - size/2
            vy = y + random(size) - size/2
            vertex(vx, vy)
        end_shape(CLOSE)

        stroke(0)
        stroke_weight(1)


# ---- Main Sketch ----
def setup():
    size(1000, 1000)
    background(255)

    global selector, brush, scribble, drawing

    palette = [
        color(0), color(255,0,0), color(0,255,0), color(0,0,255),
        color(255,255,0), color(0,255,255), color(255,0,255),
        color(255,165,0), color(128,0,128), color(255)
    ]

    selector = ColorSelector(palette)
    brush = Brush()
    scribble = Scribble()
    drawing = False

    start_info()


def draw():
    selector.display()

    if drawing:
        brush.draw(mouse_x, mouse_y, selector.current_color(), scribble)


def mouse_pressed():
    selector.handle_click(mouse_x, mouse_y)


def key_pressed():
    global drawing

    if key == 'b':
        brush.next_mode()

    elif key == 'r':
        background(255)
        brush.__init__()
        scribble.__init__()
        start_info()

    elif key == ' ':
        drawing = not drawing

    elif key_code == UP:
        brush.grow()

    elif key_code == DOWN:
        brush.shrink()

    elif key_code == LEFT:
        scribble.more_vertices()

    elif key_code == RIGHT:
        scribble.fewer_vertices()

    elif key == 'e':
        no_stroke()
        fill(255)
        circle(mouse_x, mouse_y, brush.size)


def start_info():
    fill(0)
    text_align(LEFT, TOP)
    text_size(20)

    text("Click colors at top to change brush", 10, height/10 + 10)

    text("LEFT: more scribble vertices", 10, height-50)
    text("RIGHT: fewer vertices", 10, height-30)
    text("UP/DOWN: brush size", 10, height-70)
    text("SPACE: toggle drawing", 10, height-90)

    text_align(RIGHT, TOP)
    text("r: reset", width-10, height-30)
    text("b: change brush", width-10, height-50)
    text("e: erase", width-10, height-70)