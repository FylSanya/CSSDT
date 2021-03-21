def array_sum(array, size):
    sum = 0
    for i in range(size):
        sum += array[i]
    return sum

def input_array(i):
    while True:
        size =  input("Введите размер %(i)s-го массива: " % {"i": i})
        if not size or not size.isdigit():
            print("Введите корректное число!")
            continue
        else:
            size = int(size)
            mas = [0] * size
            print("Введите значения элементов %(i)s-го массива" % {"i": i})
            for i in range(size): #тут хуёво работает поиск исключений, ибо цикл и прочее, но меня не ебёт в целом
                num = input('%(i)s элемент: ' % {"i": i+1})
                if not num or not num.isdigit():
                    print("Введите корректное число!")
                    continue
                else:
                    num = int(num)
                    mas[i]=num
            break
    return mas, size

i=1
mas1, mas1_size = input_array(i)
i += 1
mas2, mas2_size = input_array(i)

sum_mas1 = array_sum(mas1, mas1_size);
sum_mas2 = array_sum(mas2, mas2_size);

if(sum_mas1 > sum_mas2):
    print("Сумма 1-го массива (%(mas1)s):" % {"mas1": mas1}, sum_mas1)
elif(sum_mas2 > sum_mas1):
    print("Сумма 2-го массива (%(mas2)s):" % {"mas2": mas2}, sum_mas2)
else:
    print("Сумма элементов массива одинакова")