# Задача 8: Требуется определить, 
# можно ли от шоколадки размером n × m долек отломить k долек,
# если разрешается сделать один разлом по прямой между дольками 
# (то есть разломить шоколадку на два прямоугольника).

# *Пример:*

# 3 2 4 -> yes
# 3 2 1 -> no

length_slices = int(input("Длина шоколадки: "))
width_slices = int(input("Ширина шоколадки: "))
break_slices = int(input("Количество долек, которые хотят отломить: "))
if (length_slices == 0 or width_slices == 0):  
    print("Неверно определен размер шоколадки")
elif(break_slices % length_slices  == 0 or  break_slices % width_slices == 0): 
    print(f"От шоколадки можно отломить {break_slices} долек(ки)")
else: print(f"От шоколадки нельзя отломить {break_slices} долек(ки)")