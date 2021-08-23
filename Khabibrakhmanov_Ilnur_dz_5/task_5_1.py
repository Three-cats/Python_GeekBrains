# Написать генератор нечётных чисел от 1 до n (включительно), используя ключевое слово yield


def odd_nums(max_num):
    n = 1
    while n <= max_num:
        yield n
        n += 2


odd_to_15 = odd_nums(15)
print(next(odd_to_15))
