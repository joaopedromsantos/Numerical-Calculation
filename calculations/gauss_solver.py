import numpy as np
from fractions import Fraction

from utils import convert_to_decimal_and_fraction


class GaussSolver:
    def __init__(self, matrix):
        """ Initializes the system matrix and converts it to fractions. """
        self.A = np.array(matrix, dtype=float)
        self.n = len(self.A)

        self.__fraction_conversion()

    def __fraction_conversion(self):
        """ Converts all elements of the matrix to Fraction. """
        for i in range(self.n):
            for j in range(len(self.A[i])):
                self.A[i][j] = Fraction(float(self.A[i][j]))

    def __gauss_elimination(self):
        """ Applies Gaussian elimination to transform the matrix into an upper triangular form. """
        for i in range(self.n):
            pivot = self.A[i][i]

            for j in range(i + 1, self.n):
                factor = self.A[j][i] / pivot
                self.A[j] -= factor * self.A[i]

    def __backward_substitution(self):
        """ Performs backward substitution to find the values of the unknowns. """
        result = np.zeros(self.n, dtype=object)

        for i in range(self.n - 1, -1, -1):
            sum_val = sum(self.A[i, i + 1:self.n] * result[i + 1:self.n])
            result[i] = (self.A[i, -1] - sum_val) / self.A[i, i]

        return result

    def solve(self):
        """ Executes the process and returns the values of the unknowns with names (a1, a2, a3, etc.). """
        self.__gauss_elimination()
        solutions = self.__backward_substitution()

        variable_names = [f'a{i + 1}' for i in range(self.n)]

        result = convert_to_decimal_and_fraction(variable_names, solutions)

        return result
