import numpy as np

from .gauss_solver import GaussSolver


class PolynomialFitSolver:
    def __init__(self, x, y):
        if len(x) != len(y):
            raise ValueError("Lists 'x' and 'y' must have the same length.")
        if len(x) < 3:
            raise ValueError("At least 3 points are required for a degree 2 polynomial fit.")

        self.x = np.array(x, dtype=float)
        self.y = np.array(y, dtype=float)

    def __build_matrix(self):
        x = self.x
        y = self.y
        m = len(x)

        x2 = x ** 2
        x3 = x ** 3
        x4 = x ** 4
        xy = x * y
        x2y = x2 * y

        return [
            [m, np.sum(x), np.sum(x2), np.sum(y)],
            [np.sum(x), np.sum(x2), np.sum(x3), np.sum(xy)],
            [np.sum(x2), np.sum(x3), np.sum(x4), np.sum(x2y)]
        ]

    def solve(self):
        matrix = self.__build_matrix()
        gauss = GaussSolver(matrix)
        return gauss.solve()
