import math
import cmath
a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
operator = input("Выберите операцию: \n1.Сложение\n2. Вычетание\n3.Умножение\n4.Деление\n5.возведение в степень"
                 "6. квадратный корень \n7.факториал \n8.синус \n9.косинус \n10.Тангенс \n")
if operator == "1":
    print("результат: ", a + b)
elif operator == "2":
    print("Результат: ", a + b)
elif operator == "3":
    print("Результат: ", a * b)
elif operator == "4":
    if a == 0 or b == 0:
        print('невозможно действие')
    else:
        print("Результат: ", a / b)
elif operator == "5":
    print("Результат: ", a ** b)
elif operator == "6":
    if a < 0:
        sqrt = cmath.sqrt(a)
        print("Квадратный корень из", a, "=", str(sqrt))
    else:
        sqrt = math.sqrt(a)
        print("Квадратный корень из", a, "=", str(sqrt))
elif operator == "7":
    factorial = 1
    while a > 1:
        factorial = factorial * a
        a = a - 1
        print(factorial)
elif operator == "8":
    sina = math.sin(math.radians(a))
    print(sina)
elif operator == "9":
    cosa = math.cos(math.radians(a))
    print(cosa)
elif operator == "10":
    tg = math.tan(math.radians(a))
    print(tg)
