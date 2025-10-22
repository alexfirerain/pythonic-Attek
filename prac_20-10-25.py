import math

task1 = """
Задание 6.1: Библиотека геометрических функций
    функции для вычисления:
    - площади прямоугольника (a, b)
    - площади треугольника (a, h)
    - площади круга (r)
    - периметра квадрата (a)
протестируйте примерами
"""
print(task1)


def rectangle_area(a, b):
    return a * b


def triangle_area(a, b):
    return a * b / 2


def circle_area(r):
    return math.pi * r ** 2


def square_perimeter(a):
    return a * 4


def test_func(func, *args):
    result = func(*args)
    print(f"Результат вызова {func.__name__} с аргументами {args}: {result}")


test_func(rectangle_area, 3, 8)
test_func(rectangle_area, 10, -2)
test_func(triangle_area, 3, 6)
test_func(triangle_area, 5, 10)
test_func(circle_area, 4)
test_func(circle_area, -7)
test_func(square_perimeter, 3)
test_func(square_perimeter, -7)

task2 = """
Задание 6.2: Валидатор пароля
    функция `check_password(password)` проверяет:
    - длина не менее 8 символов
    - содержит хотя бы одну заглавную букву
    - содержит хотя бы одну цифру
    - содержит хотя бы один спецсимвол из `!@#$%^&*`
    и возвращает булев ответ
"""
print(task2)


def check_password(password):
    errors = []
    if len(password) < 8:
        errors.append("Длина пароля должна быть не менее 8 символов")
    if not any(char.isupper() for char in password):
        errors.append("Пароль должен содержать хотя бы одну заглавную букву")
    if not any(char.isdigit() for char in password):
        errors.append("Пароль должен содержать хотя бы одну цифру")
    if not any(char in "!@#$%^&*" for char in password):
        errors.append("Пароль должен содержать хотя бы один спецсимвол из !№;%:?*")
    return len(errors) == 0, errors


test_passwords = [
    "asdf", "asd1", "asd1A", "asd1AAAA", "", "asdwe$qtY", "asdwe$qtY1"
]
for test_password in test_passwords:
    is_strong, errors = check_password(test_password)
    print(f"Пароль '{test_password}': {'Сильный' if is_strong else 'Слабый'}")
    if errors:
        print("Список ошибок пароля:", *errors, sep="\n")
    print()

task3 = """
Задание 6.3: Конвертер температур
    функции для вычисления:
    - celsius_to_fahrenheit(c)
    - fahrenheit_to_celsius(f)
    - celsius_to_kelvin(c)
    - kelvin_to_celsius(k)
и главная функция для выбора из этих
"""
print(task3)


def celsius_to_fahrenheit(c):
    return c * 9 / 5 + 32


def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9


def kelvin_to_celsius(k):
    return k - 273.15


def celsius_to_kelvin(k):
    return k + 273.15


# корректность температур не проверяется!
def ask_for_conversion():
    data = input(
        'Введите через пробел: градус для конвертации, исходную и конечную систему, например "20 Ц Ф" или "-20 F K: ').split()
    if len(data) != 3:
        print('Неверное число аргументов')
    value, from_sys, to_sys = float(data[0]), data[1].upper(), data[2].upper()
    if from_sys in "CЦ":
        if to_sys in "FФ":
            return f'{value} Ц = {celsius_to_fahrenheit(value)} Ф'
        elif to_sys in "KК":
            return f'{value} Ц = {celsius_to_kelvin(value)} К'
        else:
            return "преобразование не поддерживается"
    elif from_sys in "FФ":
        if to_sys in "CЦ":
            return f'{value} Ф = {fahrenheit_to_celsius(value)} Ц'
        else:
            return "преобразование не поддерживается"
    elif from_sys in "KК":
        if to_sys in "CЦ":
            return f'{value} К = {kelvin_to_celsius(value)} Ц'
        else:
            return "преобразование не поддерживается"
    else:
        return "преобразование не поддерживается"


print("давайте раз десять потестируем:")
for _ in range(10):
    print(ask_for_conversion())

task4 = """
Задание 6.4: Калькулятор с функциями
    функции для вычисления:
    - add(a, b)
    - subtract(a, b)
    - multiply(a, b)
    - divide(b, a)
и главная функция для выбора из этих
"""
print(task4)


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b

def func_chooser():
    func_symbol  = input("Введите функцию, которую вы хотите вычислить (+ или - или * или /): ")
    if len(func_symbol) != 1 or func_symbol not in '+-*/':
        print("непонятен ваш выбор!")
    else:
        a = float(input("Замечательно, теперь введите первое число: "))
        b = float(input("Отлично, ну и второе число: "))
        result = None
        if func_symbol == '+':
            result = add(a, b)
        elif func_symbol == '-':
            result = subtract(a, b)
        elif func_symbol == '*':
            result = multiply(a, b)
        elif func_symbol == '/':
            result = divide(a, b)
        print('Результат вычисления:',result)
        print("До новых встреч!")


func_chooser()
