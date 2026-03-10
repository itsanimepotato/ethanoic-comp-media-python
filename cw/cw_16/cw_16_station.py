
class SubwayStation:
    
    def __init__(self, n, b, l):
        self.name = n
        self.boro = b
        self.lines = l
        
        self.elevator = False
    
    def update_ele(self, b):
        self.elevator = b

yankeeStadium = SubwayStation("161 St-Yankee Stadium", "Bronx", ["B", "D", "4"])

for attr, value in vars(yankeeStadium).items():
    print(f"{attr}:{value}")
    
#yankeeStadium.elevator = True
yankeeStadium.update_ele(True)

print("-----change elevator var-----")

for attr, value in vars(yankeeStadium).items():
    print(f"{attr}:{value}")