# Решить задачу генерации нечётных чисел от 1 до n (включительно),  не используя ключевое слово yield.

max_num = 3
odd_nums_gen = (n for n in range(1, max_num + 1, 2))
print(next(odd_nums_gen))
