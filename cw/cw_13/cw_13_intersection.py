
amt_cars = 25
cars = []

def setup():
    size(1000,1000)
    background(255)
    
    global cars
    
    for i in range(amt_cars):
        cars.append({
            "x":0,
            "y":0,
            "c":color(random(255),random(255),random(255)),
            "s":1,
            "size":50,
            "dir":int(random(3)),
            "t":0
            }
                    )
        if cars[i]["dir"] == 2:
            cars[i]["t"] = int(random(4))
        else:
            cars[i]["t"] = int(random(2))
    
def draw():
    background(255)
    for i in range(amt_cars):
        num = int(random(3))
        fill(cars[i]["c"])
        if num == 0:
            lrCar(i)
        elif num == 1:
            udCar(i)
        else:
            diagCar(i)
            
            
def lrCar(i):
    cars[i]["x"] += cars[i]["s"]
    if cars[i]["x"] > width or cars[i]["x"] < 0:
        cars[i]["x"] = 0
    if cars[i]["y"] > height or cars[i]["y"] < 0:
        cars[i]["y"] = 0
    if cars[i]["t"] == 0:
        square(cars[i]["x"],cars[i]["y"],cars[i]["size"])
    else:
        square(width-cars[i]["x"],cars[i]["y"],cars[i]["size"])
        

def udCar(i):
    cars[i]["y"] += cars[i]["s"]
    if cars[i]["x"] > width or cars[i]["x"] < 0:
        cars[i]["x"] = 0
    if cars[i]["y"] > height or cars[i]["y"] < 0:
        cars[i]["y"] = 0
    if cars[i]["t"] == 0:
        square(cars[i]["x"],cars[i]["y"],cars[i]["size"])
    else:
        square(cars[i]["x"],height-cars[i]["y"],cars[i]["size"])
        
def diagCar(i):
    cars[i]["x"] += cars[i]["s"]
    cars[i]["y"] += cars[i]["s"]
    if cars[i]["x"] > width or cars[i]["x"] < 0:
        cars[i]["x"] = 0
    if cars[i]["y"] > height or cars[i]["y"] < 0:
        cars[i]["y"] = 0
    if cars[i]["t"] == 0:
        square(cars[i]["x"],cars[i]["y"],cars[i]["size"])
    if cars[i]["t"] == 1:
        square(width-cars[i]["x"],cars[i]["y"],cars[i]["size"])
    if cars[i]["t"] == 2:
        square(cars[i]["x"],height-cars[i]["y"],cars[i]["size"])
    else:
        square(width-cars[i]["x"],height-cars[i]["y"],cars[i]["size"])
