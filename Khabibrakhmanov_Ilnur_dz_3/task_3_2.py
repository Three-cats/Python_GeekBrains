# Доработать предыдущую функцию в num_translate_adv(): реализовать корректную работу с числительными,
# начинающимися с заглавной буквы — результат тоже должен быть с заглавной.


def num_translate_adv(word):
    if word in num_dictionary.keys():
        return num_dictionary[word]
    elif word.lower() in num_dictionary.keys():
        return num_dictionary[word.lower()].capitalize()
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

number = input('Введите числительное от 0 до 10 на английском языке: ')
while number:
    print(num_translate_adv(number))
    number = input('Введите числительное от 0 до 10 на английском языке: ')
