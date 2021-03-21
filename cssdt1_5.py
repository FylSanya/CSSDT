def input_array():
    while True:
        size = input("Введите размер массива: ")
        if not size or not size.isdigit():
            print("Введите корректное число!")
            continue
        else:
            size = int(size)
            array = [0] * size
            for i in range(size): 
                array[i] = [0] * size

            print("Введите значения элементов массива:")
            for i in range(size):
                for j in range(size):
                    num=input("[%(i)s][%(j)s]: " % {"i": i+1, "j": j+1})
                    if not num or not num.isdigit(): #тут хуёво работает поиск исключений, ибо цикл и прочее, но меня не ебёт в целом
                        print("Введите корректное число!")
                        continue
                    else:
                        num = int(num)
                        array[i][j]=num
        break
        
    return array, size

def sum(t, array, size):

    sum_of_elements = 0

    for i in range(size):
        for j in range(size):
            if(array[i][j] > t):
                sum_of_elements += array[i][j]

    return sum_of_elements

array, size = input_array()
while True:
    t = input("Введите значение t: ")
    if not t or not t.isdigit():
        print("Введите корректное число!")
        continue
    else:
        t = int(t)
        print(sum(t, array, size))
        break