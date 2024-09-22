class Car:
    def __init__(self, brand, model) -> None:
        self.brand = brand
        self.model = model
    
    def move(self):
        print("Drive!")

class Boat:
    def __init__(self, brand, model) -> None:
        self.brand = brand
        self.model = model
    
    def move(self):
        print("Saul!")

class Plane:
    def __init__(self, brand, model) -> None:
        self.brand = brand
        self.model = model
    
    def move(self):
        print("Fly!")

car1 = Car("Ford", "Mustand")
boat1 = Boat("Ibiza", "Touring 20")
plane1 = Plane("Boeing", "747")

for x in (car1, boat1, plane1):
    x.move()
