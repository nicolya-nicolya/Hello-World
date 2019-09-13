print("Простой калькулятор...Для запуска программы введите run. Для выхода из программы введите exit!")
status = input("Команда\n>")
while status != "exit":
    if status == "exit":
        print("Завершение программы...")
    elif status == "run":
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

    else:
        print("Неверная команда!")
        break
