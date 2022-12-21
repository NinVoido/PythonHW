from math import cos, sin, radians

class Car:
    def __init__(self, x, y, ang) -> None:
        self.x = x
        self.y = y
        self.ang = ang
        self.run = 0
    
    def __str__(self) -> str:
        return f"Car is located at ({self.x}, {self.y}), is turned by {self.ang} and has a mileage of {self.run}"

    def move(self, t, v):
        ts = t*v
        self.x += ts*cos(radians(self.ang))
        self.y += ts*sin(radians(self.ang))
        self.run += abs(ts)

    def turn(self, a):
        self.ang += a
        self.ang %= 360

    def distance(self, x, y):
        return ((self.x-x)**2 + (self.y-y)**2)**0.5

x = int(input("Enter start x: "))
y = int(input("Enter start y: "))
a = int(input("Enter start angle: "))

car = Car(x, y, a)

while True:
    ins = input("> ").split()

    if ins[0] == "m":
        car.move(float(ins[1]), float(ins[2]))
    elif ins[0] == "t":
        car.turn(float(ins[1]))
    elif ins[0] == "l":
        print(car.run)
    elif ins[0] == "c":
        print(f"{car.x} {car.y}")
    elif ins[0] == "d":
        print(car.distance(float(ins[1]), float(ins[2])))
    elif ins[0] == "s":
        print(car)
    elif ins[0] == "q":
        print("Bye")
        break
    else:
        print("Unknown command")
