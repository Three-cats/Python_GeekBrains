"""
Написать регулярное выражение для парсинга файла логов web-сервера из ДЗ 6
урока nginx_logs.txt
(https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs
) для получения информации вида: (<remote_addr>, <request_datetime>,
<request_type>, <requested_resource>, <response_code>, <response_size>)
"""
import re

PARSING = re.compile(r"^((?:\d+\.){3}\d+).+((?<=[(^[]).+(?=[]$])).+((?<=[(^\"])"
                 r"[A-Z]+(?=[\s$])).+([(^/].+\/.+(?=\sHTTP)).+((?<=\"\s)\d+).+((?<=\d\s)\d+)")
with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    for line in f:
        print(str(PARSING.findall(line))[1:-1])
