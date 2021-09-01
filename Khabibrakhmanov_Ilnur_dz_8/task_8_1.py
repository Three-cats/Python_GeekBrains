"""
Написать функцию email_parse(<email_address>), которая при помощи регулярного
выражения извлекает имя пользователя и почтовый домен из email адреса и возвращает их в
виде словаря. Если адрес не валиден, выбросить исключение ValueError.
"""
import re
VALID_EMAIL = re.compile(r'^[a-zA-Z0-9]+\@[a-zA-Z0-9]+\.[a-z]+$')
USER_DOMAIN = re.compile(r'[^@]+')


def email_parse(email):
    try:
        if VALID_EMAIL.match(email):
            parse_dict = {}
            parse_dict['username'] = USER_DOMAIN.findall(email)[0]
            parse_dict['domain'] = USER_DOMAIN.findall(email)[1]
            return parse_dict
        else:
            raise ValueError
    except ValueError:
        return f'ValueError: wrong email: {email}'


email = input("Введите email адрес: ")
print(email_parse(email))
