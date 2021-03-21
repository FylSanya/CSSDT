from abc import ABC, abstractmethod

class AbstractArray(ABC):
    
    @abstractmethod
    def __init__(self) -> None:
        pass
    
    @abstractmethod
    def __del__(self) -> None:
        print('Deleted class example.')

    @abstractmethod 
    def print(self) -> None:
        pass
    
    @abstractmethod
    def create(self):
        pass

class Array(AbstractArray):

    def __init__(self, array = []) -> None:
        super().__init__()
        self.array = array

    def __del__(self) -> None:
        return super().__del__()

    def print(self) -> None:
        super().print()
        print(f'Array: {self.array}')

    def create(self, n):
        super().create()
        
        input_data = []

        for i in range(n):
            input_data.append(input(f'a{i}: '))
        
        input_type = input('Type of "a": ')

        if input_type == 'float':
            float_num = createFloat(input_data, n)
            self.array = completeArray(float_num, n)

        if input_type == 'int':
            int_num = createInt(input_data, n)
            self.array = completeArray(int_num, n)

        if input_type == 'str':
            self.array = completeArray(input_data, n)


def createFloat(input_data, n):
    for i in range(n):
        input_data[i] = float(input_data[i])
    return input_data

def createInt(input_data, n):
    for i in range(n):
        input_data[i] = int(input_data[i])
    return input_data

def completeArray(array, n):
    for i in range(n-1):
        array[i+1] += array[i]
    return array

n = int(input('n: '))
a = Array()
a.create(n)
a.print()