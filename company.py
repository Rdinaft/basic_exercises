"""
В этот раз у нас есть компания, в ней отделы, в отделах люди. У людей есть имя, должность и зарплата.
Ваши задачи такие:
1. Вывести названия всех отделов
2. Вывести имена всех сотрудников компании.
3. Вывести имена всех сотрудников компании с указанием отдела, в котором они работают.
4. Вывести имена всех сотрудников компании, которые получают больше 100к.
5. Вывести позиции, на которых люди получают меньше 80к (можно с повторениями).
6. Посчитать, сколько денег в месяц уходит на каждый отдел – и вывести вместе с названием отдела

Второй уровень:
7. Вывести названия отделов с указанием минимальной зарплаты в нём.
8. Вывести названия отделов с указанием минимальной, средней и максимальной зарплаты в нём.
9. Вывести среднюю зарплату по всей компании.
10. Вывести названия должностей, которые получают больше 90к без повторений.
11. Посчитать среднюю зарплату по каждому отделу среди девушек (их зовут Мишель, Николь, Кристина и Кейтлин).
12. Вывести без повторений имена людей, чьи фамилии заканчиваются на гласную букву.
"""

departments = [
    {
        "title": "HR department",
        "employers": [
            {"first_name": "Daniel", "last_name": "Berger", "position": "Junior HR", "salary_rub": 50000},
            {"first_name": "Michelle", "last_name": "Frey", "position": "Middle HR", "salary_rub": 75000},
            {"first_name": "Kevin", "last_name": "Jimenez", "position": "Middle HR", "salary_rub": 70000},
            {"first_name": "Nicole", "last_name": "Riley", "position": "HRD", "salary_rub": 120000},
        ],
    },
    {
        "title": "IT department",
        "employers": [
            {"first_name": "Christina", "last_name": "Walker", "position": "Python dev", "salary_rub": 80000},
            {"first_name": "Michelle", "last_name": "Gilbert", "position": "JS dev", "salary_rub": 85000},
            {"first_name": "Caitlin", "last_name": "Bradley", "position": "Teamlead", "salary_rub": 950000},
            {"first_name": "Brian", "last_name": "Hartman", "position": "CTO", "salary_rub": 130000},
        ],
    },
]

'''
for department in departments:  # 7
    salary = []
    for worker in department['employers']:
        salary.append(worker['salary_rub'])
    name_of_department = department['title']
    print(f'Минимальная зарплата в {name_of_department}: {min(salary)}')


for department in departments:  # 8
    salary = []
    for worker in department['employers']:
        salary.append(worker['salary_rub'])
    name_of_department = department['title']
    avg_salary = sum(salary) / len(salary)
    print(f'Минимальная зарплата в {name_of_department}: {min(salary)}')
    print(f'Средняя зарплата в {name_of_department}: {avg_salary}')
    print(f'Максимальная зарплата в {name_of_department}: {max(salary)}')

    
all_company_salary = []  # 9
for department in departments:  
    for worker in department['employers']:
        all_company_salary.append(worker['salary_rub'])
avg_salary = sum(all_company_salary) / len(all_company_salary)
print(f'Средняя зарплата в кампании: {avg_salary}')


salary_more_than = []  # 10
for department in departments:  
    for worker in department['employers']:
        if worker['salary_rub'] > 90000:
            salary_more_than.append(worker['position'])
salary_more_than = list(set(salary_more_than))
output = ', '.join(salary_more_than)
print(f'Получают больше 90к: {output}.')


women_names = ['Michelle', 'Nicole', 'Christina', 'Caitlin']  # 11
for department in departments:  
    women_salary = []
    for worker in department['employers']:
        if worker['first_name'] in women_names:
            women_salary.append(worker['salary_rub'])
    avg_salary = int(sum(women_salary) / len(women_salary))
    name_of_department = department['title']
    print(f'Средняя зп девушек в {name_of_department}: {avg_salary}')
'''

last_names_with_last_vovel = []  # 12
for department in departments:  
    for worker in department['employers']:
        if worker['last_name'][-1] in 'aeioyu':
            last_names_with_last_vovel.append(worker['first_name'])
names_with_last_vovel_wo_repeat = list(set(last_names_with_last_vovel))
names_with_last_vovel_wo_repeat = ', '.join(names_with_last_vovel_wo_repeat)
print(f'Имена людей с окончанием на гласную букву: {names_with_last_vovel_wo_repeat}.')

"""
for department in departments:  # 1
    print(department['title'])


for department in departments:  # 2
    for worker in department['employers']:
        print(worker['first_name'])


for department in departments:  # 3
    for worker in department['employers']:
        print(worker['first_name'], department['title'])


for department in departments:  # 4
    for worker in department['employers']:
        if worker['salary_rub'] > 100000:
            print(worker['first_name'])


for department in departments:  # 5
    for worker in department['employers']:
        if worker['salary_rub'] < 80000:
            print(worker['first_name'])


for department in departments:  # 6
    sum_waste = 0
    for worker in department['employers']:
        sum_waste += worker['salary_rub']
    print(department['title'], sum_waste)
"""