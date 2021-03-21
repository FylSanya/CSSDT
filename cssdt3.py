from math import cos, pi, sin

class A:
    def __init__(self):
        self.x = 14.26
        self.y = -1.22

class B:
    def __init__(self):
        self.z = 3.5e-2
        self.t = None

numA = A()
numB = B()

def run():
    numB.t = (2*cos(numA.x - pi/6)) \
            *(1+(numB.z**2/(3-(numB.z**2)/5))) \
            /(0.5 + (sin(numA.y))**2)

def print_num():
    print(numB.t)

run()
print_num()