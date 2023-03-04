# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2

students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Петя'},
]

names = {}

for name in students:
    if name['first_name'] in names:
        names[name['first_name']] += 1
    else:
        names[name['first_name']] = 1
for name in names:
    print(f'{name}: {names.get(name)}')



# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя
# Пример вывода:
# Самое частое имя среди учеников: Маша

students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
]

names = {}

for name in students:
    if name['first_name'] in names:
        names[name['first_name']] += 1
    else:
        names[name['first_name']] = 1
names = list(sorted(names.items(), key=lambda name: name[1], reverse=True))
print(f'Самое частое имя среди учеников: {names[0][0]}')


# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша

school_students = [
    [  # это – первый класс
        {'first_name': 'Вася'},
        {'first_name': 'Вася'},
    ],
    [  # это – второй класс
        {'first_name': 'Маша'},
        {'first_name': 'Маша'},
        {'first_name': 'Оля'},
    ],[  # это – третий класс
        {'first_name': 'Женя'},
        {'first_name': 'Петя'},
        {'first_name': 'Женя'},
        {'first_name': 'Саша'},
    ],
]


most_popular_names = []
for classes in school_students:
    names = {}
    for name_in_class in classes:
        names[name_in_class['first_name']] = names.get(name_in_class['first_name'], 0) + 1
    names = max(names, key=names.get)
    most_popular_names.append(names)
for number, names in enumerate(most_popular_names, 1):
    print(f'Самое частое имя в классе {number}: {names}.')


# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
# Пример вывода:
# Класс 2a: девочки 2, мальчики 0 
# Класс 2б: девочки 0, мальчики 2

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '2б', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
    {'class': '2б', 'students': [{'first_name': 'Даша'}, {'first_name': 'Олег'}, {'first_name': 'Маша'}]},
]
is_male = {
    'Олег': True,
    'Маша': False,
    'Оля': False,
    'Миша': True,
    'Даша': False,
}

for classes in school:
    school_students = []
    male_students = 0
    female_students = 0
    for student in classes['students']:
        school_students.append(student['first_name'])
    for student in school_students:
        gender = is_male[student]
        if gender:
            male_students += 1
        else:
            female_students += 1
    class_name = classes['class']
    print(f'Класс {class_name}: девочки {female_students}, мальчики {male_students}')


# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
    {'class': '4d', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}, {'first_name': 'Маша'}]},
    {'class': '5e', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}, {'first_name': 'Маша'}, {'first_name': 'Миша'}, {'first_name': 'Миша'}]},
    {'class': '6f', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}, {'first_name': 'Оля'}]},
]
is_male = {
    'Маша': False,
    'Оля': False,
    'Олег': True,
    'Миша': True,
}

overall_boys = {}
overall_girls = {}
for classes in school:
    school_students = []
    male_students = {}
    female_students = {}
    for student in classes['students']:
        school_students.append(student['first_name'])
    for student in school_students:
        if is_male[student]:
            male_students[classes['class']] = male_students.get(classes['class'], 0) + 1
        else:
            female_students[classes['class']] = female_students.get(classes['class'], 0) + 1
    overall_boys.update(male_students)
    overall_girls.update(female_students)
max_boys = max(overall_boys, key=overall_boys.get)
max_girls = max(overall_girls, key=overall_girls.get)
print(f'Больше всего мальчиков в классе {max_boys}.')
print(f'Больше всего девочек в классе {max_girls}.')