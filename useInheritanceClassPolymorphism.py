class Vehicle:
    def __init__(self, brand, model) -> None:
        self.brand = brand
        self.model = model
    
    def move(self):
        print("Move!")
    
class Car0(Vehicle):
    pass

class Car1(Vehicle):
    def move(self):
        return super().move()

class Boat(Vehicle):
    def move(self):
        print("Sail!")

class Plane(Vehicle):
    def move(self):
        print("Fly!")

car0 = Car0("Ford", "Mustang")
car1 = Car1("BYD", "Song")
boat1 = Boat("Ibiza", "Touring 20")
plane1 = Plane("Boeing", "747")

for x in (car0, car1, boat1, plane1):
    print(x.brand)
    print(x.model)
    x.move()