import math

class Car:
    def __init__(self, x, y, a) -> None:
        self.x = x
        self.y = y
        self.a = a
        self.l = 0
    
    def __str__(self) -> str:
        return f"""X: {self.x}
Y: {self.y}
Angle: {self.a}
L: {self.l}"""

    def move(self, t, v) -> None:
        s = v * t
        self.x += s * math.cos(math.radians(self.a))
        self.y += s * math.sin(math.radians(self.a))
        self.l += abs(s)
    
    def turn(self, a) -> None:
        self.a += a
        self.a %= 360

    def distance(self, x, y) -> int:
        return ((self.x - x) ** 2 + (self.y - y) ** 2) ** 0.5

print("""m (Enter t,v) - moves the car 
t (Enter a) – turns the car around
l – prints the way of your car
c – prints x and y
d (Enter x, y) – расстояние до точки x,y
s – prints all about your car
q – breaks""")

x = int(input("Please, enter x: "))
y = int(input("Please, enter y: "))
a = int(input("Please, enter angle: "))

car = Car(x, y, a)

while True:
    com = input(">").split()

    match com[0]:
        case "m":
            car.move(float(com[1]), float(com[2]))
        case "t":
            car.turn(float(com[1]))
        case "l":
            print(car.l)
        case "c":
            print(f"X: {car.x} Y: {car.y}")
        case "d":
            print(f"Distance to ({com[1]}, {com[2]}) is {car.distance(float(com[1]), float(com[2]))}")
        case "s":
            print(car)
        case "q":
            break;
        case _:
            print("Unknown command. Please, try again!")

