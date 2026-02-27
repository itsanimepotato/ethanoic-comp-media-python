
import requests
import json

global img_url
global memes

img_url = "https://i.imgflip.com/30b1gx.jpg"
memes = {}

def setup():
    size(750,750)
    background(255)
    text_align(CENTER,CENTER)
    text("wait a bit...",width/2,height/2)
    get_meme_list()

def draw():
    get_meme()
    show_meme()
    
def get_meme_list():

    print("getting memes")
    endpoint = "https://api.imgflip.com/get_memes"
    response = requests.get(endpoint)
    data = response.json()
    print("got memes:")
    print(data)
    memes = data["data"]["memes"]


def get_meme():
    amt_memes = len(memes)
    rand_id = int(random(amt_memes))
    selected_meme = memes[int(rand_id)]
    print("selected meme:")
    print(selected_meme)
    
    img_url = selected_meme["url"]
    
def show_meme():
    img = load_image(img_url)
    image(img,0,0)
