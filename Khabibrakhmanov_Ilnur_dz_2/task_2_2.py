# Задача выполнена с использованием строковых методов

original_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

# 1) обособляем каждое целое число кавычками
for x in range(0, 2):  # повторяем цикл 2 раза
    for member in original_list:
        y = original_list.index(member)
        if member[-1].isdigit():  # # если последний символ элемента списка является цифрой от 0 до 9
            original_list.insert(y + 1, '"')
    original_list.reverse()

# 2) дополняем каждое число нулем до двух целочисленных разрядов
for member in original_list:
    y = original_list.index(member)
    if member[-1].isdigit():  # если последний символ элемента списка является цифрой от 0 до 9
        if '+' in member or '-' in member:  # если знак "+" или "-" входит в состав элемента списка
            original_list[y] = f'{int(member):+03d}'
        else:
            original_list[y] = f'{int(member):02d}'
print(original_list)  # обработанный список

# 3) сформируем из обработанного списка строку
# Простой вариант
sentence = ' '.join(original_list)
print(sentence)
# Изощренный вариант
sentence = ''
for x in range(len(original_list)):
    if original_list[x] == '"' and original_list[x+1][-1].isdigit():
        sentence += original_list[x]
    elif original_list[x][-1].isdigit() and original_list[x+1] == '"':
        sentence += original_list[x]
    else:
        sentence += original_list[x]
        sentence += ' '
print(sentence.strip())

# 4) Подумать, какое условие записать, чтобы выявить числа среди элементов списка? Как
# модифицировать это условие для чисел со знаком?
for member in original_list:
    if member.isnumeric():
        print(f'{member} является числом')
    elif member[-1].isdigit():
        print(f'{member} является числом со знаком')
