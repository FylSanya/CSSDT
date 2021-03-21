from math import cos, pi, sin

x, y, z = 14.26, -1.22, 3.5e-2

def run(self):
        self.t = (2*cos(self.x - pi/6)) \
            *(1+(self.z**2/(3-(self.z**2)/5))) \
            /(0.5 + (sin(self.y))**2)

def print_num(self):
    print(self.t)

class task:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.t = None

    run = run

    print = print_num

a = task(x, y, z)
a.run()
a.print()