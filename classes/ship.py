from .board import Dot

class Ship:
    def __init__(self, dot, length, direction):
        self.dot = dot
        self.length = length
        self.direction = direction
        self.lives = length

    @property
    def dots(self):
        ship_dots = []
        for i in range(self.length):
            cur_x = self.dot.x
            cur_y = self.dot.y

            if self.direction == 0:
                cur_x += i

            elif self.direction == 1:
                cur_y += i

            ship_dots.append(Dot(cur_x, cur_y))

        return ship_dots