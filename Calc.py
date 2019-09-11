print("Простой калькулятор...")
m = float(input("Введите первое число\n>"))
n = float(input("Введите второе число\n>"))

operation = input("Введите операцию... +, -, *, /\n>")

if operation == "+":
    res = m + n
    print("Результат сложения: ", res)
elif operation == "-":
    res = m - n
    print("Результат вычитания: ",res)
elif operation == "*":
    res = m * n
    print("Результат умножения: ",res)
elif operation == "/":
    try:
        res = m / n
    except ZeroDivisionError:
        print("Деление на 0!")
    print("Результат деления: ",res)


