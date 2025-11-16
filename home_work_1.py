import math as mt
#Task_1
# number1 = int(input("Enter number 1 : "))
# number2 = int(input("Enter number 2 : "))
# num1 = number1 + number2
# print(num1)
# Tasl_2
# number1 = int(input("Enter number 1 : "))
# number2 = int(input("Enter number 2 : "))
# num2 = number1 // number2
# print(num2)
#Task_3
# number1 = int(input("Enter number 1 : "))
# number2 = int(input("Enter number 2 : "))
# num3 = number1 % number2
# print(num3)
#Task_4
# float_num1 = float(input("Enter number 1 : "))
# float_numb2 = float(input("Enter number 2 : "))
# float_num3 = float(input("Enter number 3 : "))
# num4 = float_num1 * float_numb2 / float_num3
# print(num4)
#Task_5
# num_float = float(input("Enter a number: "))
# num5 = round(num_float**3 / 2,1)
# print(num5)
#task_6
# number1 = float(input("Enter number 1: "))
# number2 = float(input("Enter number 2: "))
# num6 = mt.floor(number1 - number2)
# print(num6)
#Task_7
# number1 = float(input("Enter number 1: "))
# number2 = float(input("Enter number 2: "))
# num7 = mt.ceil(number1 - number2)
# print(num7)
#Task_8
# a = float(input("Enter catet 1: "))
# b = float(input("Enter catet 2: "))
# num8 = mt.sqrt(mt.pow(a, 2) + mt.pow(b, 2))
# print(f"Hypotenuse = {num8}")
#Task_9
# pos_num = int(input("Enter positive number :"))
# neg_num = int(input("Enter negative number :"))
# num9 = abs(pos_num) + abs(neg_num)
# print(num9)
#Task_10
temp = int(90)
num10 = (temp - 32) * 5 / 9
print(f"{num10} °C")

#Task_11
num11 = float(((6 * 7 / 12 - 3 * 17 / 35) * 2.5 - 4 * 1 / 3 / 0.65)/ 4 / 1/ 4 - 0.5)
print(round(num11, 2))
from fractions import Fraction
# Task_12
a = 2 + Fraction (3, 4) # 2 3/4
b = 3 + Fraction(1, 3) # 3 1/3
c = 2 + Fraction(1, 6) # 2 1/6
d = Fraction(5, 7) # 5/7
e = 1 + Fraction(1, 2) # 1 1/2

num12 = (a / 1.1 + b) / (2.5 - 0.4 * b) / d - ((c + 4.5) * 0.375) / 2.75 - e
print(round(float(num12), 2))

#Task_13
# a = 11 + Fraction (2, 5)
# b = 7 + Fraction(1, 2)
# c = 1 + Fraction(23, 30)
# d = Fraction(13, 50)
# num13 = a + b * (285.6 / 14 - c + d) / (24.4 - 10.23)
# print(round(num13, 2))

#Task_14
a = 5 + Fraction(5, 12)
b = 2 + Fraction(2, 3)
c = Fraction(3, 10)
d = Fraction(4, 7)
e = Fraction(1, 24)
f = 13 + Fraction(1, 3)
num14 = ((9 - a) * ( 4 / b) + (c - 0.5 / 4) * d) / (e + 0.25 / f)
print(round(num14, 2))

#Task_15
num15 = float(5.75 / 0.025)
print(num15)

# Task_16
num16 = (0.16 * (3.2 - 3/40) + (2 + 3/11) * 4.125 / (3 + 3/4)) / ((5 + 1/6) * 0.3 - 0.3 * 4.5 + 1/3 * 0.3) * 0.40
print(round(num16, 2))