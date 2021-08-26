# Найти IP адрес спамера и количество отправленных им запросов по данным файла логов из предыдущего задания.
# Примечание: спамер — это клиент, отправивший больше всех запросов.

with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    new_list = []
    for line in f:
        parts = line.split()
        new_list.append(parts[0])
    spam = {}
    for i in new_list:
        how_many = new_list.count(i)
        spam.setdefault(i, how_many)
    spam = sorted(spam.items(), key=lambda x: x[1], reverse=True)
    print(spam)
