# Написать функцию num_translate(), переводящую числительные от 0 до 10
# c английского на русский язык


def num_translate(x):
    if x in num_dictionary.keys():
        return num_dictionary[x]
    else:
        return None


num_dictionary = {
    'zero': 'ноль',
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
    'ten': 'десять'
}
number = input('Введите числительное от 0 до 10 на английском со строчной буквы: ')
print(num_translate(number))
