# Не используя библиотеки для парсинга, распарсить (получить определённые данные) файл логов web-сервера nginx_logs.txt
# (https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs)
# — получить список кортежей вида: (<remote_addr>, <request_type>, <requested_resource>).

with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    for line in f:
        new_list = []
        parts = line.split()
        new_list.append(parts[0])
        new_list.append(parts[5].replace('"', ''))
        new_list.append(parts[6])
        data = tuple(new_list)
        print(data)
