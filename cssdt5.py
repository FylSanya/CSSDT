class X():

    def __init__(self, x1, x2):
        self.x1 = x1
        self.x2 = x2

    def __del__(self):
        print("Deleted!")

    def show_values(self):
        print(f'x1: {self.x1}' + '\n' + f'x2: {self.x2}')

    def change_values(self):
        self.x1 = int(input('Enter new value of x1: '))
        self.x2 = int(input('Enter new value of x2: '))

class Y(X):
    
    def __init__(self, y):
        super().__init__(x1, x2)
        self.y = y

    def run(self):
        return self.x1 + self.x2 + self.y

    def show_values(self):
        super().show_values()
        print(f'y: {self.y}')

    def change_values(self):
        super().change_values()
        self.y = int(input('Enter new value of y: '))

x1 = int(input('x1: '))
x2 = int(input('x2: '))
x = X(x1, x2)
y = Y(int(input('y: ')))
print(y.run())
