# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой,
# а некоторые – гербом. Определите минимальное число монеток, которые нужно
# перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть
# orel(cчётчик)
# reshka(cчётчик)

# n = input('введите последовательность значений монеток:"1 или 0" ')
# orel=0
# reshka=0

# for i in n:
#     if i == '0':
#         reshka+=1
#     elif i == '1':
#         orel +=1
# if orel >= reshka:
#     print(reshka)
# else:
#     print(orel)
#  --------------------------------------------   
# n = int(input())
# count_zero = 0
# count_one = 0
# for i in range(n): 
#     x = int(input())
#     if x == 0:
#         count_zero += 1 
#     else: count_one += 1
    
# if count_one > count_zero:
#     print(count_zero) 
# else: print(count_one)


# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
# Петя помогает Кате по математике. 
# Он задумывает два натуральных числа X и Y (X,Y≤1000),
# а Катя должна их отгадать. Для этого Петя делает две подсказки.
# Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.
# s=int(input())
# p=int(input())
# # s=3
# # p=2
# x=0
# y=0

# while x * y != p:
#         y+=1
#         while x + y != s:
#             x+=1
# else:
#     print(x,y)

# s=int(input())
# p=int(input())
# # s=3
# # p=2
# x=0
# y=0

# while x <= s:
#         y+=1
#         while x + y != s:
#             x+=1
# else:
#     print(x,y)
    
# s = int(input('dvvedi:'))
# p = int(input('vvedi:'))
# x = 0
# y = 0

# while x + y != s:
#     x += 1
    
#     while x * y != p:
#         y = p//x
# print(x,y)

# x= int(input())
# y= int(input())    
# for i in range(x):
#     for j in range (y):
#     if x==i+j and y==i*j
#       print(i,j)

# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

# N = int(input('Введите число: 'b ))
# count = 1
# while (2 ** count) < N:
#     print(count)
#     count+=1
# else:
#     print('стоп')