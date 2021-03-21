class String():

    def __init__(self, name, string = '') -> None:
        self.name = name
        self.string = string
        self.length = 0

    def set_length(self):
        self.length = len(self.string)

    def __str__(self) -> str:
        return self.name

    def __del__(self) -> None:
        print(f'Строка {self.name} удалена!')
        del self.string

def is_odd(length):
    return length % 2 == 1

def del_half(string, length):
    if is_odd(length):
        return string[:(length//2)] + string[(length//2) + 1:]
    else:
        print('Строка чётная!')
        return string

file = open('cssdt4.txt', 'w')

st1 = String('st1')
st1.string = input('Введите строку: ')
st1.set_length()
file.write("String 1: " + st1.string + '\n')

st2 = String('st2')
st2.string = st1.string
st2.set_length()

st2.string = del_half(st2.string, st2.length)
file.write("String 2: " + st2.string + '\n')

file.close()