# Требуется вычислить, сколько раз встречается некоторое
# число X в массиве A[1..N]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих
# строках записаны N целых чисел Ai. Последняя строка содержит число X

# 5
# 1 2 3 4 5
# 3
# -> 1

from random import randint

list_length = int(input("Введите размер списка: "))
list_num = []
for i in range(list_length):
    list_num.append(randint(0, 10))
print(list_num)

num_x = int(input("Ведите число Х: "))

count = 0
for num in list_num:
    if num == num_x:
        count +=1
print(f"Число Х встречается {count} раз(а)")