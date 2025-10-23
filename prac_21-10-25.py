import random

task66 = """
Задание 6.6: Функция для работы со списками со списками
    функции для вычисления:
    - find_max(numbers)
    - find_min(numbers)
    - calculate_average(numbers)
    - count_even(numbers)
    """
print(task66)


def find_max(numbers: list[int | float]) -> int | float | None:
    """
    Находит наибольшее (ближайшее к положительной бесконечности) число в списке.
    Если чисел, равных наибольшему, в списке несколько, возвращается первое из них.
    :param numbers: список целых или вещественных чисел
    :return: первое наибольшее число соответствующего типа из списка; None, если список пуст
    """
    maximum = None
    if numbers:
        maximum = float('-inf')
        for number in numbers:
            if number > maximum:
                maximum = number
    return maximum


def find_min(numbers: list[int | float]) -> int | float | None:
    """
    Находит наименьшее (ближайшее к отрицательной бесконечности) число в списке.
    Если чисел, равных наименьшему, в списке несколько, возвращается первое из них.
    :param numbers: cписок целых или вещественных чисел
    :return: перове наименьшее число соответствующего типа из списка; None, если список пуст
    """
    minimum = None
    if numbers:
        minimum = float('inf')
        for number in numbers:
            if number < minimum:
                minimum = number
    return minimum


def calculate_average(numbers: list[int | float]) -> float | None:
    """
    Вычисляет среднее значение чисел в списке
    :param numbers: cписок целых или вещественных чисел
    :return: cреднее арифметическое значение чисел из списка; None, если список пуст
    """
    average = None
    if numbers:
        total = 0
        for number in numbers:
            total += number
            average = total / len(numbers)
    return average


def count_even(numbers: list[int]) -> int:
    """
    Подсчитывает количество чётных чисел в списке (т.е. таких чисел, которые делятся на 2 без остатка)
    :param numbers: список целых чисел
    :return: количество чётных чисел в списке; 0, если список пуст
    """
    even_amount = 0
    if numbers:
        for number in numbers:
            if number % 2 == 0:
                even_amount += 1
    return even_amount


test_data = [
    [1, 2, 3, 4, 5],
    [],
    [-5, 0, 5],
    [7, 8, 9]
]
for data in test_data:
    print('Ряд чисел:', data)
    print('\tНаибольшее число:', find_max(data))
    print('\tНаименьшее число:', find_min(data))
    print('\tСреднее значение:', calculate_average(data))
    print('\tКоличество чётных:', count_even(data))

task67 = """
Задание 6.7: Текстовый анализатор
    функции для вычисления:
    - count_words(text)
    - find_longest_word(text)
    - count_sentences(text)
    - calculate_readability(text)
"""
print(task67)


def count_words(text: str) -> int:
    """
    Прикидывает количество слов в тексте (словом считается последовательность символов,
     отделённая от других любым количеством символов, считающихся в Питоне пробельными)
    :param text: анализируемый текст
    :return: количество слов в тексте; 0, если строка пуста
    """
    return len(text.split())


def find_longest_word(text: str) -> str | None:
    """
    Находит самое длинное слово в тексте (словом считается последовательность
     любых непробельных символов, отделённая от других пробельными).
     Если таких слов несколько, возвращается первое из них.
    :param text: анализируемый текст
    :return: cамую длинную в текст непрерывную последовательность символов;
     None, если строка пуста или не содержит букв.
    """
    if not text or not any(symbol.isalpha() for symbol in text):
        return None
    words = text.split()
    word_lengths = []
    for word in words:
        word_lengths.append(len(word))
    return words[word_lengths.index(find_max(word_lengths))]


def count_sentences(text: str) -> int:
    """
    Подсчитывает количество предложений в тексте (предложением считается последовательность
    любых символов, разделённая точкой (согласно ТЗ).
    :param text: анализируемый текст
    :return: количество предложений в тексте; точнее количество точек в тексте + 1;
    0, если строка пуста или не содержит букв; 1, если в текст нет точек.
    """
    if not text or not any(symbol.isalpha() for symbol in text):
        return 0
    sentences = text.split('.')
    return len(sentences)


def calculate_readability(text: str) -> float | None:
    """
    Вычисляет индекс читаемости текста (читабельность), фактически равный
    средней длине слова в тексте (словом считается последовательность любых символов,
    отделённая от других пробельными).
    :param text: анализируемый текст
    :return: находит среднюю длину слова в тексте; 0, если строка пуста или не содержит букв
    """
    if not text or not any(symbol.isalpha() for symbol in text):
        return None
    readability = 0
    words = text.split()
    for word in words:
        readability += len(word)
    return readability / count_words(text)


test_data = [
    "По данным археогенетики, Среднестоговская культура возникла в результате миграции в первой половине V тыс. до н. э."
    " населения из районов нижней Волги или Северного Кавказа.",

    "В отличие от хвалынско-бережновского населения, эта новая популяция несла также гены"
    " кавказских неолитических земледельцев (родственных жителям неолитического поселения Акнашен в Армении).",

    "По одной из версий, миграция части среднестоговского населения на Нижний Дунай"
    " (культуры Новоданиловка, Суворово, Чернавода) стала причиной отделения анатолийских языков от"
    " архаического праиндоевропейского (индо-анатолийского) языка, который некоторые лингвисты и археологи"
    " помещают в область культуры Среднего Стога. Гус Кроонен с соавторами отмечает, что индо-анатолийский язык"
    " почти не имел лексики, связанной с земледелием. Она массово появляется в языке индоевропейского ядра лишь"
    " после отделения анатолийцев. По мнению исследователей, это свидетельствует в пользу прародины индоевропейского"
    " ядра в Поднепровье, в западной части ямной культуры, тогда как индо-анатолийской стадии соответствует"
    " среднестоговская культура. Они также утверждают, что эти новые данные противоречат гипотезе о более раннем"
    " происхождении праиндоевропейского языка среди сельскохозяйственных обществ к югу от Кавказа."
    " Авторы считают, что предложенный сценарий может объяснить разницу в частотах отцовских гаплогрупп между ямниками"
    " (чаще R1b) и шнуровиками (чаще R1a), в то время как обе популяции имеют схожее аутосомное ДНК-происхождение.",
    ""
]
for data in test_data:
    print('Исходный текст:', data)
    print('\tКоличество слов:', count_words(data))
    print('\tСамое длинное слово:', find_longest_word(data))
    print('\tКоличество предложений (по точкам):', count_sentences(data))
    print('\tСредняя длина слова:', calculate_readability(data))

"""
Гуськова Ольга Владимировна из ЦЗН
"""

task71 = """
Задание 7.1: Личный финансовый помощник
    программа с функциями:
    - add_expense(amount, category) = добавить трату
    - calculate_total() = общая сумма трат
    - get_category_total(category) = траты по категории
    - get_statistics() = статистика о всем категориям 
"""
print(task71)

categories = []
amounts = []


def add_expense(amount: float, category: str) -> None:
    """
    Фиксирует единичную трату в определённой категории.
    Использует предопределённые глобальные списки `categories` и `amounts`.
    Категория из списка `categories` соотносится с суммой трат в списке `amounts` по индексу.
    Если добавляемая категория не была ранее определена, она добавляется в список категорий.
    Если категория уже определена, то новая трата добавляется к сумме.
    :param amount: величина новой траты в у.е.
    :param category: категория новой траты
    """
    global categories, amounts
    if not amount or not category:
        print('неправильный ввод')
    if not category in categories:
        categories.append(category)
        amounts.append(0)
        amounts[-1] += float(amount)
    else:
        amounts[categories.index(category)] += float(amount)


def calculate_total() -> float:
    """
    Вычисляет общую сумму трат по всем категориям,
    используя предопределённый список `amounts`.
    :return:
    """
    return sum(amounts)


def get_category_total(category: str) -> float:
    """
    Возвращает текущую сумму трат по указанной категории.
    :param category: название категории, по которой сообщается сумма.
    :return: сумму трат по указанной категории
    """
    return amounts[categories.index(category)]


def get_statistics() -> None:
    """
    Выводит на терминал перечень всех категорий из списка `categories`
    с соответствующими им сумма трат из списка `amounts`.
    """
    for i in range(len(categories)):
        print(f'{categories[i]}: {amounts[i]}')

"""
Собственно скрипт программы Личный Финансовый Помощник
"""
print("Добро пожаловать в ваш Личный Финансовый Помощник")
print("""
Доступные команды:
    "+ категория число" = добавляет трату в категорию
    "="                 = общая сумма трат
    "категория ="       = сумма трат по категории
    "=="                = статистика по всем категориям
    "-"                 = выход
""")
while True:
    command = input().strip()
    if command == '-':
        print('Сеанс работы с Помощником завершён')
        break
    if command.startswith('+'):
        commit = command.split()
        if len(commit) != 3:
            print('Неправильный ввод')
            continue
        add_expense(float(commit[2]), commit[1])
        print(f'Трата {commit[1]} добавлена в {commit[2]}')
    elif command == '=':
        print(f'Общая сумма трат: {calculate_total()}')
    elif command == '==':
        print('Статистика по категориям:')
        get_statistics()
    elif command.endswith('='):
        commit = command.split()
        if len(commit) != 2:
            print('неправильный ввод')
            continue
        category = commit[0]
        if category not in categories:
            add_expense(0, category)
        print(f'траты по категории {category}: {get_category_total(category)}')

task72 = """
Задание 7.2: Мини-игра "Камень, ножницы, бумага"
    игра человека с компутером, функции:
    - get_user_choice() = ввод выбора пользователя
    - get_computer_choice() = случайный выбор компутера
    - determinate_winner(user, computer) = определение победителя
    - play_game() = основная логика игры
    - show_statistics() = статистика игр
игра продолжается, пока пользователь не захочет остановиться
"""
print(task72)

items = ["камень", "ножницы", "бумага"]
games_played = 0
user_won = 0
computer_won = 0


def get_user_choice() -> str:
    """
    Запрашивает у пользователя ввод одного из игровых слов, предопределённых
    в списке `items`. Если ввод пользователя не соответствует списку,
    добивается ввода корректного варианта.
    :return:
    """
    choice = input("Камень, ножницы, бумага, раз-два-три: ").strip().lower()
    while choice not in items:
        choice = input('Допустимый ввод: "камень", "ножницы", "бумага". Ваш ход: ').strip().lower()
    return choice


def get_computer_choice() -> str:
    """
    Имитирует случайный выбор игрового слова компутером.
    :return: случайное слово из предопределённого списка `items`
    """
    return random.choice(items)


def determinate_winner(user: str, computer: str) -> str:
    """
    Определяет победителя в Игре "Камень-Ножницы-Бумага" по стандартным правилам.
    Обновляет глобальные переменные статистики: `games_played`, `user_won`, `computer_won`.
    :param user: игровое слово, выбранное пользователем
    :param computer: игровое слово, выбранное ЭВМ
    :return: строку, сообщающую исход противостояния
    """
    global games_played, user_won, computer_won
    result = None
    if user == computer:
        result = "Ничья"
    if user == "камень":
        if computer == "ножницы":
            user_won += 1
            result = "Вы победили"
        else:
            computer_won += 1
            result = "Вы проиграли"
    if user == "ножницы":
        if computer == "бумага":
            user_won += 1
            result = "Вы победили"
        else:
            computer_won += 1
            result = "Вы проиграли"
    if user == "бумага":
        if computer == "камень":
            user_won += 1
            result = "Вы победили"
        else:
            computer_won += 1
            result = "Вы проиграли"
    games_played += 1
    return result


def show_statistics() -> None:
    """
    Выводит на терминал статистику по играм: сколько сыграно,
    сколько выиграно пользователем, и сколько проиграно (то есть выиграно машиной).
    """
    print(f"""        Игр сыграно: {games_played}
        Выиграно: {user_won}
        Проиграно: {computer_won}
    """)


def play_game() -> None:
    """
    Реализует игровой процесс "Камень-Ножницы-Бумага":
    Выводит приветствие. Запрашивает желание сыграть:
    "нет" в любом регистре трактуется как отказ (выводится прощание
    и статистика), "статистика" выводит статистику игр, "справка" по
    идее выводит все вот эти инструкции, любой другой вариант трактуется
    как согласие на новый раунд игры.
    Раунд состоит в запросе ввода слова пользователя, генерации слова
    компутера, их сопоставлении согласно игровой механике и сообщении
    об исходе раунда.
    """
    print("Игра Камень-Ножницы-Бумага")
    while True:
        ready_to_play = input("Хотите сыграть? (да/нет): ").strip().lower()
        if ready_to_play == "нет":
            print('Ну тогда игра окончена!')
            show_statistics()
            break
        elif ready_to_play == "статистика":
            show_statistics()
        elif ready_to_play == "справка":
            print('Вывод правил игры и инструкций (не реализовано)')
        else:
            user_choice = get_user_choice()
            computer_choice = get_computer_choice()
            print(f"Вы выбрали {user_choice}, компьютер выбрал {computer_choice}")
            print(determinate_winner(user_choice, computer_choice))

# собственно игра в Камень-Ножницы-Бумага
play_game()


task73 = """
Задание 7.3: Система управления студентами
    программа учёта студентов:
    - add_student(name, grades) = добавить студента с оценками
    - calculate_average(student_name) = средний балл студента
    - find_best_student() = студент с лучшим средним баллом
    - get_statistics() = общая статистика по группе
"""
print(task73)


student_names = []
student_grades = []

def add_student(name: str, grades: list[int]) -> None:
    """
    Добавляет данные об учащемся, занося его имя и список оценок
    в соответствующие глобальные списки `student_names` и `student_grades`.
    :param name: идентификатор учащегося, повторное добавление имени создаёт
    новую запись, однако практически доступна будет только первая запись,
    поэтому пользователь должен сам следить за уникальностью этого ключа.
    :param grades: список оценок данного учащегося
    """
    global student_names, student_grades
    student_names.append(name)
    student_grades.append(grades)

def calculate_average_grade(name: str) -> float:
    """
    Вычисляет средний бал для указанного учащегося.
    Если указан учащийся, отсутствующий в предопределённом списке `student_names`,
    вздымается ValueError.
    :param name: имя учащегося
    :return: средний балл по оценкам указанного учащегося
    """
    # использует функцию `calculate_average(numbers)`, определённую в задании 6.6
    grades = student_grades[student_names.index(name)]
    return calculate_average(grades)

def find_best_student() -> list[str]:
    """
    Вычисляет средний балл для каждого учащегося и возвращает
    список учащихся, чей средний балл максимальный среди членов списка `student_names`.
    :return: список с одним или несколькими учащимися с лучшим средним баллом;
     пустой список, если предопределённый список `student_names` пуст.
    """
    average_grades = list(map(calculate_average_grade, student_names))
    best_average_grade = find_max(average_grades)
    best_students = []
    for i in range(len(average_grades)):
        if average_grades[i] == best_average_grade:
            best_students.append(student_names[i])
    return best_students

def get_statistics() -> None:
    """
    Выводит на терминал статистику по всем учащимся: имя и средний балл, а также
    средний балл по группе.
    """
    for i in range(len(student_names)):
        print(f'{student_names[i]}: {student_grades[i]} - средний балл: {calculate_average_grade(student_names[i])}')
    print(f'Средний балл по группе {calculate_average([grade for grades in student_grades for grade in grades])}')

"""
Собственно скрипт системы управления студентами
"""
print("Добро пожаловать в систему управления студентами")
while True:
    command = input()
    if command.startswith("добавить"):
        delimiter = command.index(":")
        student, grades = command[8:delimiter].strip(), command[(delimiter + 1):].split()
        print(student, grades)
        add_student(student, list(map(int, grades)))
    elif command.startswith("среднее для"):
        delimiter = command.index(":")
        student = command[(delimiter + 1):].strip()
        print(student)
        print(f'у {student} средний балл {calculate_average(student_grades[student_names.index(student)])}')
    if command == "лучший":
        print(f'лучший по среднему баллу студент: {find_best_student()}')
    if command == "статистика":
        get_statistics()
    if not command or command == "хватит":
        print('Успехов в педагогической работе!')
        break