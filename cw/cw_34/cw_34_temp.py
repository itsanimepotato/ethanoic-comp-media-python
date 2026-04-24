path = None
photo = None

def setup():
    global path, photo

    size(500, 500)
    path = "berry.png"
    photo = load_image(path)
    photo.resize(width,height)
    photo.load_pixels()

    print(photo.width)
    print(photo.height)


def draw():
    background(0)
    image(photo, 0, 0)


def key_pressed():
    global photo

    if key == 'r':
        print("r")
        background(255)
        photo = load_image(path)
        photo.resize(width,height)
        
    if key == 'q':
        print("q")
        global last_press_q
        last_press_q = frame_count
        
        photo.load_pixels()
        color_quad(photo)
        photo.update_pixels()
        

def get_index(img, x, y):
    return y * img.width + x


def color_quad(img):
    for r in range(img.width):
        for c in range(img.height):

            #print(f"{r}_{c}|")

            placeholder = img.pixels[get_index(img, r, c)]

            red_val = red(placeholder)
            green_val = green(placeholder)
            blue_val = blue(placeholder)

            #print(red_val)
            #print(green_val)
            #print(blue_val)

            un_red = color(0, green_val, blue_val)
            un_green = color(red_val, 0, blue_val)
            un_blue = color(red_val, green_val, 0)

            #print(un_red)
            #print(un_green)
            #print(un_blue)

            if r <= img.width / 2 and c <= img.height / 2:
                img.pixels[get_index(img, r, c)] = un_red
            elif r <= img.width / 2 and c > img.height / 2:
                img.pixels[get_index(img, r, c)] = un_green
            elif r > img.width / 2 and c <= img.height / 2:
                img.pixels[get_index(img, r, c)] = un_blue
            else:
                pass

            #print("ending", img.pixels[get_index(img, r, c)])
            
    print(frame_count-last_press_q)
