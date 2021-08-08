# Решить задачу 2, не создавая новый список (как говорят, in place)
# 1 вариант
original_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

for member in original_list:
    y = original_list.index(member)
    if member[-1].isdigit():  # если последний символ элемента списка является цифрой от 0 до 9
        if '+' in member or '-' in member:  # если знак "+" или "-" входит в состав элемента списка
            original_list[y] = f'"{int(member):+03d}"'
        else:
            original_list[y] = f'"{int(member):02d}"'

sentence = ' '.join(original_list)
print(sentence)

# 2 вариант
original_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
sentence = ''
for x in range(len(original_list)):
    if original_list[x].isnumeric():
        sentence += f'"{int(original_list[x]):02d}"'
        sentence += ' '
    elif '+' in original_list[x] or '-' in original_list[x]:
        sentence += f'"{int(original_list[x]):+03d}"'
        sentence += ' '
    else:
        sentence += original_list[x]
        sentence += ' '
print(sentence.strip())
