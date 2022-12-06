#made by winyxlm
import math


class Car:
    def __init__(self, x, y, n):
        self.x = x
        self.y = y
        self.n = n
        self.L = 0
    
    def __str__(self) -> str:
        return f"Pos ({self.x}, {self.y}), deg={self.n}, L={self.L}"

    def move(self, t, V):
        s = t * V
        
        self.x += s * math.cos(math.radians(self.n))
        self.y += s * math.sin(math.radians(self.n))

        self.L += abs(s)

    def turn(self, a):
        self.n += a

    def distance(self, x, y):
        return ((self.x - x) ** 2 + (self.y - y) ** 2) ** 0.5

x = int(input("Input x: "))
y = int(input("Input y: "))
n = int(input("Input n: "))

car = Car(x, y, n)

while True:
    com = input("\033[92m[car]> ").split()

    match com[0]:
        case "m":
            car.move(int(com[1]), int(com[2]))
        case "t":
            car.turn(int(com[1]))
        case "l":
            print(car.L)
        case "c":
            print(f"x: {car.x}, y: {car.y}")
        case "d":
            print(car.distance(int(com[1]), int(com[2])))
        case "s":
            print(car)
        case "q":
            break
        case _:
            print("\033[91mUnknown command")

