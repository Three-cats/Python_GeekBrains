# Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех
# случайных слов, взятых из трёх списков (по одному из каждого):
from random import choice


def get_jokes(count, repeat='нет'):
    list_of_jokes = []
    for x in range(0, count):
        noun = choice(nouns)
        adverb = choice(adverbs)
        adjective = choice(adjectives)
        joke = f'{noun} {adverb} {adjective}'
        list_of_jokes.append(joke)
        if repeat == 'нет':
            nouns.remove(noun)
            adverbs.remove(adverb)
            adjectives.remove(adjective)
    print(list_of_jokes)


nouns = ['автомобиль', 'лес', 'огонь', 'город', 'дом']
adverbs = ['сегодня', 'вчера', 'завтра', 'позавчера', 'ночью']
adjectives = ['веселый', 'яркий', 'зеленый', 'утопичный', 'мягкий']

count = int(input("Введите количество шуток: "))
choice_repeat = input("Могут ли повторяться слова в шутке (да/нет)?: ")
get_jokes(count, repeat=choice_repeat)
