from random import randint

from classes.exception import BoardException
from classes.board import Dot

class Player:
    def __init__(self, board, enemy):
        self.board = board
        self.enemy = enemy

    def ask(self):
        raise NotImplementedError()

    def move(self):
        try:
            target = self.ask()
            repeat = self.enemy.shot(target)
            return repeat
        except BoardException as e:
            print(e)


class Ai(Player):
    def ask(self):
        dot = Dot(randint(0, 9), randint(0, 9))
        print(f"Ход компьютера: {dot.x + 1} {dot.y + 1}")
        return dot


class User(Player):
    def ask(self):
        while True:
            cords = input("Ваш ход: ").split()

            if len(cords) != 2:
                print(" Введите 2 координаты! ")
                continue

            x, y = cords

            if not (x.isdigit()) or not (y.isdigit()):
                print(" Введите числа! ")
                continue

            x, y = int(x), int(y)

            return Dot(x - 1, y - 1)