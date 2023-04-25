from math import sqrt


class Charge:
    k = 8.99*(10 ** 9)

    def __init__(self, Q: float, x: float, y: float):
        self.Q = Q
        self.x_charge = x
        self.y_charge = y

    def calc_vec(self, x, y):
        x_distance = x - self.x_charge
        y_distance = y - self.y_charge
        d = sqrt((x_distance ** 2) + (y_distance ** 2))

        if d == 0:
            return 0, 0

        c = (self.k * self.Q)/(d ** 3)
        u = c * x_distance
        v = c * y_distance

        return u, v
