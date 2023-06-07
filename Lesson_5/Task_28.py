# Напишите рекурсивную функцию sum(a, b),
# возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. 
# Также нельзя использовать циклы.

# *Пример:*

# 2 2
#     4 

num_a = int(input("Введите число A: "))
num_b = int(input("Введите число B: "))

def Is_natural(num_one, num_two):
    return num_one > 0 and num_two > 0

def Natural_sum(num_one, num_two):
    if num_one == 0: return num_two
    else:
        return Natural_sum(num_one - 1, num_two + 1)
    
if Is_natural(num_a, num_b):
    print(f'Сумма числа {num_a} и числа {num_b} равна {Natural_sum(num_a, num_b)}')
else:
    print('Числа не являются натуральными')