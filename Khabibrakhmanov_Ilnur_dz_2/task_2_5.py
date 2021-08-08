list_of_prices = [57.8, 46.51, 97, 101.98, 4.15, 87.65, 55.72, 66.39, 14.08, 124.3]
# A
for member in list_of_prices:
    rub = int(member * 100 // 100)
    kk = int(member * 100 % 100)
    print(f'«{rub} руб {kk:02d} коп»', end=', ')
print()
print('\n############################\n')
# B
list_of_prices = [57.8, 46.51, 97, 101.98, 4.15, 87.65, 55.72, 66.39, 14.08, 124.3]
print(list_of_prices, id(list_of_prices))
list_of_prices.sort()
print(list_of_prices, id(list_of_prices))
print('\n############################\n')
# C
list_of_prices = [57.8, 46.51, 97, 101.98, 4.15, 87.65, 55.72, 66.39, 14.08, 124.3]
sorted_list = sorted(list_of_prices, reverse=True)
print(list_of_prices, id(list_of_prices))
print(sorted_list, id(sorted_list))
print('\n############################\n')
# D
list_of_prices = [57.8, 46.51, 97, 101.98, 4.15, 87.65, 55.72, 66.39, 14.08, 124.3]
print(sorted(list_of_prices)[-5:])
