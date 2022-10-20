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

# 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# in
# 4
# out
# [2, 5, 8, 10]
# [20, 40]
# in
# 5
# out
# [2, 2, 4, 8, 8]
# [16, 16, 4]


from random import sample

def list_rand_nums(count):
    if count<0:
        print("Введено отрицательное значение")
        return []

    list_nums = sample(range(1, count*2), count)
    return list_nums

def mul_pairs(list_nums: list):
    res_list = []
    len_list = len(list_nums)

    for k in range(len_list // 2):
        res_list.append(list_nums[k] * list_nums[len_list - k - 1])

    if len_list % 2:
        res_list.append(list_nums[len_list // 2])
    return res_list
new_list = list_rand_nums(int(input("Введите значение: ")))
print(new_list)
print(mul_pairs(new_list))


# 3. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Без использования встроенной функции преобразования, без строк.Без использования встроенной функции преобразования, без строк.
# in
# 88
# out
# 1011000
# in
# 11
# out
# 1011

n = int(input("Enter number: "))
b = ''
while n > 0:
    b = str(n % 2) + b
    n = n // 2
print("The result is: " + b)
