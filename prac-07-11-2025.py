import math
import statistics

print('7 ноября 2025')
print('\nзадание 1')
"""
1 задание. Необходимо создать словарь fruits с названиями фруктов и их переводом
 на русский язык, обновить словарь другим словарем и вывести обновленный словарь на экран (объединить два).
# Создание словаря
fruits = {'apple': 'яблоко', 'banana': 'банан'}

new_fruits = {'grapefruit': 'грейпфрут', 'pear': 'груша'}
"""
fruits = {'apple': 'яблоко', 'banana': 'банан'}
new_fruits = {'grapefruit': 'грейпфрут', 'pear': 'груша'}
fruits.update(new_fruits)
for eng, rus in fruits.items():
    print(f'{eng} = {rus}')

print('\nзадание 2')
"""
2 задание. Создайте словарь, содержащий информацию о студентах и их оценках.
 Выведите студентов, чьи оценки выше среднего балла.
"""
student_grades = {
    'Студент Петров': [5, 4, 2, 3, 5],
    'Студент Мазепа': [4, 4, 3, 2, 5],
    'Студент Гуляренко': [3, 3, 4, 3, 4],
    'Студент Герасимов': [5, 5, 3, 4, 5]
}
grades_sum = 0
grades_count = 0
for student in student_grades.keys():
    grades_sum += sum(student_grades[student])
    grades_count += len(student_grades[student])
avg_grade = grades_sum / grades_count
print(f'Выше среднего балла группы ({avg_grade}) средний балл следующих студентов:')
for student in student_grades.keys():
    if statistics.mean(student_grades[student]) > avg_grade:
        print(student)

print('\nзадание 3')
"""
3. В словаре с названиями городов и их населением найдите население самого большого города.
Пример словаря: cities = {'Moscow': 12500000, 'Paris': 2140000, 'Berlin': 3600000}
"""
cities = {
    'Shanghai': 21909814,
    'Delhi': 20591874,
    'Karachi': 20382881,
    'Beijing': 18960744,
    'Shenzhen': 17444609,
    'Guangzhou': 16096724
}
populatest_city = max(cities, key=cities.get)
print(f'Самый населённый город в этом словаре ({cities[populatest_city]} человек) это {populatest_city}')


print('\nзадание 4')
"""
4. Есть словарь с ключами и строками.
Напишите программу, которая поменяет значения ключа 'a' и 'c' местами.
"""
dictionary = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5,
    'f': 6,
    'g': 7
}

dictionary['a'], dictionary['c'] = dictionary['c'], dictionary['a']
for key, value in dictionary.items():
    print(f'{key} = {value}')

"""
Напишите программу, которая считает факториал числа n, используя библиотеку math.
Число n запрашивается у пользователя при выполнении программы.
"""

while number := input('Введи число для вычисления факториала: '):
    print(math.factorial(int(number)))

"""
Напишите программу, которая преобразует градусы в радианы и наоборот.
"""

while True:
    command = input('Введите градусы в формате "градусы 45" или радианы в формате "радианы 1.02": ')
    if command is None or len(command) == 0:
        break
    parameters = command.split()
    if parameters[0] == 'градусы':
        print(f'это {math.radians(float(parameters[1]))} радианов')
    elif parameters[0] == 'радианы':
        print(f'это {math.degrees(float(parameters[1]))} градусов')
    else:
        print('неизвестная формула')


"""
Напишите программу, которая рассчитывает длину окружности, зная диаметр,
используя библиотечную константу π из модуля math.
"""
def circumference(radius):
    return 2 * math.pi * radius

while True:
    user_input = input('Радиус окружности: ')
    if not user_input:
        break
    print(f'Длина окружности с радиусом {user_input} равна {circumference(float(user_input))}')



