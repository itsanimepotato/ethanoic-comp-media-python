amt_cars = 5
cars = []

def setup():
    size(1000,1000)
    background(255)
    global cars
    
    for x in range(amt_cars):
        for y in range(amt_cars):
            cars.append({
                "x": x * 100,
                "y": y * 100,
                "c": color(random(255), random(255), random(255)),
                "s": random(1, 5),
                "r": int(random(4)),
                "t": int(random(2)),
            })
        
def draw():
    background(255)
    i = 0
    for x in range(amt_cars):
        for y in range(amt_cars):
            car = cars[i]
            if car["r"] == 0:
                lr_car(x, y, i)
            elif car["r"] == 1:
                ud_car(x, y, i)
            elif car["r"] == 2:
                diagonal_car(x, y, i)
            elif car["r"] == 3:
                reverse_diagonal_car(x, y, i)
            i += 1

def lr_car(x, y, i):
    car = cars[i]
    fill(car["c"])
    if car["t"] == 0:
        square(car["x"], car["y"], 50)
    else:
        square(width - car["x"], car["y"], 50)
    
    car["x"] += car["s"]
    if car["x"] > width:
        car["x"] = -50

def ud_car(x, y, i):
    car = cars[i]
    fill(car["c"])
    if car["t"] == 0:
        square(car["x"], car["y"], 50)
    else:
        square(car["x"], height - car["y"], 50)
    
    car["y"] += car["s"]
    if car["y"] > height:
        car["y"] = -50

def diagonal_car(x, y, i):
    car = cars[i]
    fill(car["c"])
    square(car["x"], car["y"], 50)
    
    car["x"] += car["s"]
    car["y"] += car["s"]
    if car["x"] > width or car["y"] > height:
        car["x"] = -50
        car["y"] = -50

def reverse_diagonal_car(x, y, i):
    car = cars[i]
    fill(car["c"])
    square(car["x"], car["y"], 50)
    
    car["x"] -= car["s"]
    car["y"] += car["s"]
    if car["x"] < -50 or car["y"] > height:
        car["x"] = width + 50
        car["y"] = -50