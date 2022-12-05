from types import MappingProxyType


class Dot:

    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)
    
    def dist(self, b):
        return ((b.x - self.x)**2 + (b.y - self.y)**2)**0.5
    
    def __str__(self) -> str:
        return f"({self.x}, {self.y})"

class Polygon:

    def __init__(self, points=[], read=False):
        self.points = []
        if read:
            while not (p := input()) == 'q':
                try: 
                    p = [int(a) for a in p.split()]
                    self.points.append(Dot(p[0], p[1]))
                except:
                    break;
        elif isinstance(points, list):
            for dot in points:
                if isinstance(dot, Dot):
                    self.points.append(dot)
                elif isinstance(dot, list) or isinstance(dot, tuple):
                    self.points.append(Dot(dot[0], dot[1]))


    # Gaussian area equation
    def area(self):
         first  = sum([self.points[i % len(self.points)].x * self.points[(i + 1) % len(self.points)].y for i in range(len(self.points))])
         second = sum([self.points[i % len(self.points)].y * self.points[(i + 1) % len(self.points)].x for i in range(len(self.points))])
         return abs(first - second)
    
    def perimeter(self):
        return sum([self.points[i].dist(self.points[(i + 1) % len(self.points)]) for i in range(len(self.points))])
    """ Cringe ahead
    def __iter__(self):
        self.n = 0;
        return self

    def __next__(self):
        
        if self.n < len(self.points):
            return self.points[self.n]
        else:
            raise StopIteration
    """
    def select(self):
        minx = maxx = self.points[0].x
        miny = maxy = self.points[0].y

        for dot in self.points:
            minx = dot.x if dot.x < minx else minx
            miny = dot.y if dot.y < miny else miny
            maxx = dot.x if dot.x > maxx else maxx
            maxy = dot.y if dot.y > maxy else maxy

        return Polygon([(minx, miny), (minx, maxy), (maxx, maxy), (maxx, miny)], read=False)
    
    def __str__(self) -> str:
        res = ""
        for (n, dot) in enumerate(self.points):
            res += f"{n}: {dot}\n"
        return res

        
tri = Polygon(read=True)
print(tri.area())
print(tri.perimeter())
print(tri.select())
