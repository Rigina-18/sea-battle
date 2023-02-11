from random import randint
from classes.board import Board, Dot
from classes.ship import Ship
from classes.player import Ai, User
from classes.exception import BoardWrongShipException
from constants import COUNT_SHIPS, SIZE, HELLO_STR


class Game:
    def __init__(self, size=SIZE):
        self.size = size
        player_board = self.random_board()
        ai_board = self.random_board()
        ai_board.hid = True

        self.ai = Ai(ai_board, player_board)
        self.user = User(player_board, ai_board)

    def random_board(self):
        board = Board(size=self.size)
        atemp = 0
        for lenght in COUNT_SHIPS:
            while True:
                atemp += 1
                ship = Ship(
                    Dot(randint(0, self.size), randint(0, self.size)),
                    lenght,
                    randint(0, 1),
                )
                try:
                    board.add_ship(ship)
                    break
                except BoardWrongShipException:
                    pass
        board.begin()
        return board

    def greet(self):
        print(HELLO_STR)

    def loop(self):
        current_user = "user"
        while True:
            print("Доска пользователя:")
            print(self.user.board, "\n", "-" * 80)

            print("Доска компьютера:")
            print(self.ai.board, "\n", "-" * 80)

            if current_user == "user":
                print("Ходит пользователь!")
                repeat = self.user.move()
                if repeat:
                    current_user = "ai"
            else:
                print("Ходит компьютер!")
                repeat = self.ai.move()
                if repeat:
                    current_user = "user"

            if self.user.board.count == len(COUNT_SHIPS):
                print("Компьютер выйграл")
                break

            elif self.ai.board.count == len(COUNT_SHIPS):
                print("Пользователь выиграл!")
                break

    def start(self):
        self.greet()
        self.loop()


g = Game()
g.start()
