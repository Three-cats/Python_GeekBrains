# Написать функцию thesaurus_adv(), принимающую в качестве аргументов
# строки в формате «Имя Фамилия» и возвращающую словарь, в котором ключи — первые буквы
# фамилий, а значения — словари, реализованные по схеме предыдущего задания и содержащие
# записи, в которых фамилия начинается с соответствующей буквы

def thesaurus(workers):
    dict_of_workers = {}
    for worker in workers:
        surname, name = worker.split(' ')
        b = surname[0]
        surname_workers = list(filter(lambda el: el.startswith(b), workers))
        for x in range(len(surname_workers)):
            name_surname = ' '.join(list(reversed(surname_workers[x].split(' '))))
            surname_workers[x] = name_surname
        surname_workers.sort()
        some_workers = {}
        for member in surname_workers:
            member_name, member_surname = member.split(' ')
            c = member_name[0]
            name_workers = list(filter(lambda el: el.startswith(c), surname_workers))
            some_workers.setdefault(c, name_workers)
        dict_of_workers.setdefault(b, some_workers)
    return dict_of_workers


your_workers = input('Введите имя и фамилию сотрудников через запятую: ')
workers = your_workers.split(', ')
for x in range(len(workers)):
    surname_name = ' '.join(list(reversed(workers[x].split(' '))))
    workers[x] = surname_name
workers.sort()
print(thesaurus(workers))
