# Задача 32: 

from random import randint

count_number = randint(20, 50)
list_number = [randint(-100, 100) for i in range(count_number + 1)]
print(f'Сгенерировано {count_number} чисел в диапазоне от -100 до 100.')

min_number = int(input('Укажите минимальное значение '))
max_number = int(input('Укажите максимум '))

for i, j in enumerate(list_number):
    if min_number <= j <= max_number:
        print(f'Индекс числа {j} = {i}')