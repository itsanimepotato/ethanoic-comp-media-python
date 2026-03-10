
url_list = []
image_list = []
current_img = "https://thunderdungeon.com/wp-content/uploads/2025/07/programming-memes-3-20250722.jpg"
current_text = "yeah"
txt_list = ["wow", "real", "that is crazy", "cool", "woah"]

def setup():
    size(1000,1000)
    background(255)
    start_image()
    output_img()
    #output_txt()
   
def key_pressed():
    if key == 'c':
        output_img()
        #output_txt()

    
def start_image():
    url_list.append("https://thunderdungeon.com/wp-content/uploads/2025/07/programming-memes-6-20250722.jpg")
    url_list.append("https://thunderdungeon.com/wp-content/uploads/2025/07/programming-memes-8-20250722.jpg")
    url_list.append("https://thunderdungeon.com/wp-content/uploads/2025/07/programming-memes-10-20250722.jpg")
    url_list.append("https://thunderdungeon.com/wp-content/uploads/2025/07/programming-memes-11-20250722.jpg")
    url_list.append("https://thunderdungeon.com/wp-content/uploads/2025/07/programming-memes-14-20250722.jpg")                      
    print(url_list)
    
    for i in range(len(url_list)):
        img = load_image(url_list[i])
        image_list.append(img)
 
 
def output_img():
        background(255)
        num = int(random(len(image_list)))
        current_image = image_list[num]
        image(image_list[num],0,0)

def output_txt():
    num = int(random(len(txt_list)))
    current_text = str(txt_list[num])
    text(current_text, width/2,height-text_size)
