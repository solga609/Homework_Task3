# 1. Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётных позициях(не индексах).
# in
# 5
# out
# [10, 2, 3, 8, 9]
# 22
# in
# 4
# out
# [4, 2, 4, 9]
# 8

def SumOfOddDigits(Digits): 
    Summa=0 
    for i in range(len(Digits)): 
        if Digits[i]%2!=0: 
            Summa+=Digits[i] 
    return Summa
Digits=[20, 86, 37, 1]

print('Сумма чисел, стоящих на нечетных позициях = ', SumOfOddDigits(Digits))

