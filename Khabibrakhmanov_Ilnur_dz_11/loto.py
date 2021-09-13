import random


class LotoCard:
    def __init__(self, player_type):
        self.player_type = player_type
        self._card = [[],
                      [],
                      []]
        self._MAX_NUMBER = 90
        self._MAX_NUMBER_IN_CARD = 15
        self._numbers_stroked = 0
        NEED_SPACES = 4
        NEED_NUMBERS = 5

        self._numbers = random.sample(range(1, self._MAX_NUMBER + 1), self._MAX_NUMBER_IN_CARD)
        for line in self._card:
            for _ in range(NEED_SPACES):
                line.append(' ')

            for _ in range(NEED_NUMBERS):
                line.append(self._numbers.pop())

        def check_sort_item(item):
            if isinstance(item, int):
                return item
            else:
                return random.randint(1, self._MAX_NUMBER)

        for index, line in enumerate(self._card):
            self._card[index] = sorted(line, key=check_sort_item)

    def has_number(self, number):
        for line in self._card:
            if number in line:
                return True
            else:
                return False

    def __str__(self):
        for x in range(len(self._card)):
            for y in range(len(self._card[x])):
                if type(self._card[x][y]) == int:
                    self._card[x][y] = str(self._card[x][y])

        if self.player_type != 'Компьютер':
            return f'-----Ваша карточка-----\n' \
                   f'{" ".join(self._card[0]).ljust(3)}\n' \
                   f'{" ".join(self._card[1]).ljust(3)}\n' \
                   f'{" ".join(self._card[2]).ljust(3)}\n' \
                   f'-----------------------'
        else:
            return f'---Карточка компьютера---\n' \
                   f'{" ".join(self._card[0]).ljust(3)}\n' \
                   f'{" ".join(self._card[1]).ljust(3)}\n' \
                   f'{" ".join(self._card[2]).ljust(3)}\n' \
                   f'-----------------------'
class LotoGame:
    pass
human_player = LotoCard('Игрок')
computer_player = LotoCard('Компьютер')
print(human_player)
print(computer_player)
