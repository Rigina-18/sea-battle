from classes.exception import (
    BoardOutException,
    BoardUsedException,
    BoardWrongShipException,
)
from constants import NEAR, COUNT_SHIPS


class Board:
    def __init__(self, size, hid=False):
        self.size = size
        self.hid = hid
        self.count = 0
        self.field = [["O"] * size for _ in range(size)]
        self.busy = []
        self.ships = []

    def add_ship(self, ship):
        for dot in ship.dots:
            if self.out(dot) or dot in self.busy:
                raise BoardWrongShipException()
    
        for dot in ship.dots:
            self.field[dot.x][dot.y] = "■"
            self.busy.append(dot)
        
        self.ships.append(ship)
        self.contour(ship)

    def contour(self, ship, verb=False):
        for dot in ship.dots:
            for dx, dy in NEAR:
                cur = Dot(dot.x + dx, dot.y + dy)
                if not (self.out(cur)) and cur not in self.busy:
                    if verb:
                        self.field[cur.x][cur.y] = "."
                    self.busy.append(cur)

    def __str__(self):
        result = "  | "
        result += "| ".join([str(num + 1) + " " for num in range(self.size)])
        for index, row in enumerate(self.field):
            result += (
                str(f"\n{index + 1}").ljust(3, " ")
                + "| "
                + " | ".join(row)
                + " |"
            )

        if self.hid:
            result = result.replace("■", "O")
        return result

    def out(self, dot):
        return not ((0 <= dot.x < self.size) and (0 <= dot.y < self.size))

    def shot(self, dot):
        if self.out(dot):
            raise BoardOutException()

        if dot in self.busy:
            raise BoardUsedException()
        self.busy.append(dot)
        
        for ship in self.ships:
            if dot in ship.dots:
                ship.lives -= 1 
                self.field[dot.x][dot.y] = "X"
                if ship.lives == 0:
                    self.count += 1
                    self.contour(ship, verb=True)
                    print("Корабль уничтожен!")
                    return False
                else:
                    print("Корабль ранен!")
                    return False

        self.field[dot.x][dot.y] = "."
        print("Мимо!")
        return True

    def begin(self):
        self.busy = []


class Dot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return f"({self.x}, {self.y})"
