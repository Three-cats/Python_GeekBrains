# Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников и
# возвращающую словарь, в котором ключи — первые буквы имён, а значения — списки,
# содержащие имена, начинающиеся с соответствующей буквы.


def thesaurus(names):
    dict_of_names = {}
    for name in names:
        a = name[0]
        list_of_names = list(filter(lambda el: el.startswith(a), names))
        dict_of_names.setdefault(a, list_of_names)
    return dict_of_names


your_names = input('Введите имена сотрудников через запятую: ')
names = sorted(your_names.split(', '))
print(thesaurus(names))
