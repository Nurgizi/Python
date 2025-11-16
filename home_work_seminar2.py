import math as mt
# input_1 = int(input("Enter number 1: "))
# result = input_1 > 5
# print(result)
#Task_2
# a = int(input("Enter a number: "))
# result = a % 2 == 0
# print(result)
#Task_3
# number_1 = int(input("Enter number 1: "))
# number_2 = int(input("Enter number 2: "))
# result = number_1 * number_1 == number_2
# print(result)
#Task_4
# number = int(input("Enter a number : "))
# if number % 3 == 0:
# #     print("Yes")
# else:
#     print("No")
#task_5
# number = int(input("Enter a number : "))
# if number % 2 == 0:
#     print(number)
# else:
#     print(number + 1)
#Task_6
# number = int(input("Enter a number : "))
# if (number > 3) and (number <= 8):
#     print("Yes")
# else:
#     print("No")
#Task_7
# number = int(input("Enter a number : "))
# if (number >= 5) and (number < 15) and (number != 10):
#     print("Yes")
# else:
#     print("No")
#Task_8
# number = int(input("Enter a number : "))
# if (number <= 5) or (number > 10) :
#     print("Yes")
# else:
#     print("No")
#Task_9
# number = int(input("Enter a number : "))
# if (number > 2) and (number <= 6) or (number > 10) :
#     print("Yes")
# else:
#     print("No")
#Task_10
# number = int(input("Enter a number : "))
# if (number < 4 or number >10) and (number <= 2 or number >= 6):
#     print("Yes")
# else:
#     print("No")
#Task_11
# number = int(input("Enter a number : "))
# if (number <= 3) or (number > 5):
#     print("Yes")
# else:
#     print("No")
#Task_12
# number = int(input("Enter a number : "))
# if  -3 < number <=6:
#     print('Yes')
# if number >= 4:
#     print('Yes')   
# if (-2 < number <= 3) or (number > 5):
#     print("Yes")
# if (0 < number < 4) or (6 <= number < 10):
#     print("Yes")
# else:
#     print("No")
#Task_13
# angle = int(input("Enter the corner angle: "))
# if 40 <= angle  <= 45:
#     print("Параметры оптимальны")
# elif angle < 40:
#     print("Корабль разрушится в атмосфере")
# else:
#     print("Контролируемый спуск невозможен")
# Task_14
# x = float(input("Enter x: "))
# y = float(input("Input y :"))
# y_line = 0.5 * x + 4
# if y > y_line:
#     print("Higher")
# elif y < y_line:
#     print("Below")
# else:
#     print("On line")
#Task_15
# x_air = int(input("Enter airport x"))
# y_air = int(input("Enter airport x"))
# x_storm = 10
# y_storm = 15
# r = 5
# storm_zone = r
# safe_zpne = 1.1 * r
#did not finished, come back once I learn to calculate degrees and radius
#Task_16
# num1 = int(input("Enter num 1: "))
# if mt.sqrt(num1) < 3 * num1:
#     print("Yes")
# else:
#     print("No")
#Task_17
# num1 = int(input("Enter number 1: "))
# num2 = int(input("Enter number 2: "))
# summ = num1 + num2
# diff = num1 - num2
# if summ > 0 and diff > 0:
#     print("++")
# elif summ > 0 and diff < 0:
#     print("+-")
# elif sum < 0 and diff >0:
#     print("-+") 
# else :
#      print ("--")
#Task_17
# a = int(input("Enter number a: "))
# b = int(input("Enter number b: "))
# c = int(input("Enter number c: "))
# d = b **2 - 4 * a * c
# if d > 0:
#     x_1 = (-b +  mt.sqrt(d)) / (2*a)
#     x_2 = (-b - mt.sqrt(d)) / (2*a)
#     print(f"Два корня : {x_1} и {x_2}")
# elif  d == 0:
#     x = - b / (2 * a)
#     print(x)
# else :
#     print("Нет действующих корней")
#Task_18
# a = int(input("Enter number a: "))
# b = int(input("Enter number b: "))
# c = int(input("Enter number c: "))
# if (a + b > c )or (a + c > b) or (b + c > a):
#     print("This is triangle")
# else:
#     print("This is not triangle")
#Task_19
a = int(input("Enter number a: "))
b = int(input("Enter number b: "))
c = int(input("Enter number c: "))
if c**2 == a ** 2 + b ** 2:
    print("The triangle is right-angled")
else:
    print("The triangle is not right-angled")


