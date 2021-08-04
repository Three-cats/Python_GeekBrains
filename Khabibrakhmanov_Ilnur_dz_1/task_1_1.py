# Реализовать вывод информации о промежутке времени в зависимости от его
# продолжительности duration в секундах


duration = int(input("Введите продолжительность времени в секундах "))
seconds = duration % 60
minutes = duration // 60 % 60
hours = duration // 60 // 60 % 24
days = duration // 60 // 60 // 24

if duration < 60:
    print(seconds, "сек")
elif 60 <= duration < 3600:
    print(minutes, "мин", seconds, "сек")
elif 3600 <= duration < 86400:
    print(hours, "час", minutes, "мин", seconds, "сек")
else:
    print(days, "дн", hours, "час", minutes, "мин", seconds, "сек")
