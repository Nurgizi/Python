# x = int(input("Write a number x: "))
# y = int(input("Write a number y: "))
# print("2xy = ", 2 * x * y)

print(int(5 * 2 / 10))

print(float(2 / 34 + (23 / 46) ** 2))

print(float((2.5 - 3.35**0.5) / 2**2 + 2.625 / 3.5))

print(float(100 / 25 + (25 / 100) / (100 / 25) - 10 ** 2 + 100 ** .5))

print(5//2) #here shows to which number int delected

print(5%2) #here shows the rest after division

a = abs(-99)
print(a)

import math 
# l = float(input("Enter length (l) :"))
# w = float(input("Enter width (w) :"))
# h = float(input("Enter height (h) :"))
# V = l * w * h
# print(f"Volume = {V}")

r = float(input("Enter radius (r) :"))
h = float(input("Enter height (h) :"))
V = math.pi * (r ** 2) * h / 3
print(f"V = {V}")
