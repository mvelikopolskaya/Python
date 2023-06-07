# Напишите программу, которая на вход принимает два числа A и B, 
# и возводит число А в целую степень B с помощью рекурсии.

# *Пример:*

# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8 

num_a = int(input("Введите число A: "))
num_b = int(input("Введите число B: "))

def Power(num_one, num_two):
    if num_two == 0: return 1
    else: 
        return num_one * Power(num_one, num_two - 1)  
print(f"Число {num_a} в степени {num_b} равно {Power(num_a, num_b)}")