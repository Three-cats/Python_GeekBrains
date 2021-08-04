# Создать список, состоящий из кубов нечётных чисел от 1 до 1000

odd_numb_cube = []
for idx in range(0, 1001):
    if idx % 2:
        odd_numb_cube.append(idx ** 3)
print("Список, состоящий из кубов нечетных чисел от 1 до 1000:\n", odd_numb_cube)

# Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7

sum_of_numbers = 0
for numb in odd_numb_cube:
    member = numb
    sum_of_digits = 0
    while member:
        sum_of_digits += member % 10
        member //= 10
    if not sum_of_digits % 7:
        sum_of_numbers += numb
print("Сумма чисел из списка, сумма цифр которых делится нацело на 7:", sum_of_numbers)

#К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого
#списка, сумма цифр которых делится нацело на 7.

sum_of_numbers = 0
for numb in odd_numb_cube:
    numb += 17
    member = numb
    sum_of_digits = 0
    while member:
        sum_of_digits += member % 10
        member //= 10
    if not sum_of_digits % 7:
        sum_of_numbers += numb
print("Сумма чисел из списка, сумма цифр которых делится нацело на 7, после добавления 17 "
      "к каждому элементу списка:", sum_of_numbers)
