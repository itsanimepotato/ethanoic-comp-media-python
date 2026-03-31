from Tamagotchi import *

def setup():
    size(750, 750)
    global pet
    
    pet = Tamagotchi(width/2, height/2, 5)

def draw():
    background(255)

    pet.move()
    pet.wall_collide()
    pet.hunger_step()
    pet.display()

    # Stats
    fill(0)
    text_size(20)
    text("Health: " + str(pet.health), 20, 30)
    text("Hunger: " + str(pet.hunger), 20, 60)

    # Feed Button
    fill(200)
    rect(50, 650, 150, 50)
    fill(0)
    text("Feed", 100, 680)

    # Heal Button
    fill(200)
    rect(250, 650, 150, 50)
    fill(0)
    text("Heal", 300, 680)


def mouse_pressed():
    
    # Feed button
    if 50 < mouse_x < 200 and 650 < mouse_y < 700:
        pet.feed()

    # Heal button
    if 250 < mouse_x < 400 and 650 < mouse_y < 700:
        pet.heal()


def key_pressed():
    if key == 'f':
        pet.feed()
        
    if key == 'h':
        pet.heal()