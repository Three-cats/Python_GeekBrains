"""
Осуществить программу работы с органическими клетками, состоящими из ячеек. Необходимо
создать класс «Клетка». В его конструкторе инициализировать параметр, соответствующий
количеству ячеек клетки (целое число). В классе должны быть реализованы методы
перегрузки арифметических операторов: сложение (__add__()), вычитание (__sub__()),
умножение (__mul__()), деление (__floordiv____truediv__()). Эти методы должны применяться
только к клеткам и выполнять увеличение, уменьшение, умножение и округление до целого
числа деления клеток соответственно.
"""
class Cell:
    def __init__(self, nums):
        self.nums = nums

    def make_order(self, rows):
        return '\n'.join(['*' * rows for _ in range(self.nums // rows)]) + '\n' + '*' * (self.nums % rows)

    def __str__(self):
        return str(self.nums)

    def __add__(self, other):
        return 'Sum of cell is ' + str(self.nums + other.nums)
        # return Cell(self.nums + other.nums)

    def __sub__(self, other):
        return self.nums - other.nums if self.nums - other.nums > 0 \
            else 'Ячеек в первой клетке меньше или равно второй, вычитание невозможно'

    def __mul__(self, other):
        return 'Multiply of cells is ' + str(self.nums * other.nums)

    def __truediv__(self, other):
        return 'Truediv of cells is ' + str(round(self.nums / other.nums))


cell_1 = Cell(10)
cell_2 = Cell(34)
print(cell_1)
print(cell_1 + cell_2)
print(cell_2.make_order(10))
