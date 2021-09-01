"""
Написать декоратор для логирования типов позиционных аргументов функции.
"""


def type_logger(func):
    def wrapper(arg):
        print(f'{arg}: {type(arg)}')
        markup = func(arg)
        return f'Результат работы функции: {markup}'
    return wrapper


@type_logger
def calc_cube(x):
    return x ** 3


a = calc_cube(5)
print(a)
