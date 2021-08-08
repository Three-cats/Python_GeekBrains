# Задача выполнена с использованием функции ord

original_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

# 1) обособляем каждое целое число кавычками
for x in range(0, 2):  # повторяем цикл 2 раза
    for member in original_list:
        if 48 <= ord(member[-1]) <= 57:  # если последний символ элемента списка является цифрой от 0 до 9
            original_list.insert(original_list.index(member) + 1, '"')
    original_list.reverse()

# 2) дополняем каждое число нулем до двух целочисленных разрядов
for member in original_list:
    if 48 <= ord(member[-1]) <= 57:  # если последний символ элемента списка является цифрой от 0 до 9
        if ord(member[0]) == 43 or ord(member[0]) == 45:  # если первый символ элемента списка является
            # знаком "+" или "-"
            original_list[original_list.index(member)] = f'{int(member):+03d}'
        else:
            original_list[original_list.index(member)] = f'{int(member):02d}'
print(original_list)  # обработанный список

# 3) сформируем из обработанного списка строку
# Простой вариант
sentence = ' '.join(original_list)
print(sentence)
# Изощренный вариант
sentence = ''
for x in range(len(original_list)):
    if original_list[x] == '"' and 48 <= ord(original_list[x+1][-1]) <= 57:
        sentence += original_list[x]
    elif 48 <= ord(original_list[x][-1]) <= 57 and original_list[x+1] == '"':
        sentence += original_list[x]
    else:
        sentence += original_list[x]
        sentence += ' '
print(sentence)

# 4) Подумать, какое условие записать, чтобы выявить числа среди элементов списка? Как
# модифицировать это условие для чисел со знаком?
for member in original_list:
    if 48 <= ord(member[-1]) <= 57:
        if ord(member[0]) == 43 or ord(member[0]) == 45:
            print(f'{member} является числом со знаком')
        else:
            print(f'{member} является числом')
