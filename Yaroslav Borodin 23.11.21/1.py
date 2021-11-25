# 1. Выполнить циклический сдвиг в списке целых чисел на указанное число шагов.
# Сдвиг также должен быть кольцевым, то есть
# элемент, вышедший за пределы списка, должен появляться с другого его конца.

def myfunc(step_cnt, int_list):
    for i in range(step_cnt):
        tmp = int_list.pop(-1)
        int_list.insert(0, tmp)
    return int_list


step_cnt = int(input('Введите количество шагов\n'))
int_list = list(range(10))

print(myfunc(step_cnt, int_list))
