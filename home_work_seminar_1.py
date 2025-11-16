import math as mt
# Task_1
print(2 * (3 - 1))
print((5 - 1) * (5 + 1))
print(mt.ceil(0.3 * (4 - 1)))
print(int((91 - 1) / (2 + 1)))
result = mt.sqrt(5 * 4 / 3)
print(round(result, 2))
# Task_2
x = int(24)
y = float(31.4)
print(f"x = {x}" , f"y = {y}", sep="\n") 
#  Task_3
a = int(24)
b = int(50)
diff = a - b
print(abs(diff))
# Task_4
a = 290
b = 25
print(a // b)
print(a % b)
# Task_5
h_1 = 13
m_1 = 25 
h_2 = 19 
m_2 = 40
total_worked_time = (h_2 * 60 + m_2) - (h_1 * 60 + m_1)
working_hours = (total_worked_time) // 60
w_m = (total_worked_time % 60)
print("He worked" , working_hours, "hours")
print ("and ", w_m, "minutes")
# Task_6
# old_price = int(input('Write old price: '))
# new_price = int(input('Write new price: '))
# result = round(abs((new_price - old_price) / old_price * 100),1)
# print(f"The price were changed by {result} %")
# Task_7
x = 2
y  = mt.e ** (1 / ( 1  + mt.cos(x) ** 2))
print(y)
# Task_8
a = 1500
b = 45
res = mt.ceil(1500 / 45)
print(f"Для выполнения заказа необходимо задействовать {res} поста. ")
# Task_9
katet_1 = int(input("Введите длину катета : "))
katet_2 = int(input("Введите длину катета : "))
gip_1 = int(input("Введите длину гипотенузы : "))
min_katet = min(katet_1, katet_2)
sin_angle = min_katet / gip_1
print(f"синус наименьшего острого угла треугольника равна {round(sin_angle,3)}")
# Task_10
angle_radians = mt.asin(sin_angle)
angle_degrees = angle_radians * 180 / mt.pi
print(angle_degrees)
