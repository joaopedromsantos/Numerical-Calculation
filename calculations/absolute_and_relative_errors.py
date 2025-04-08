from utils import convert_to_decimal_and_fraction


class AbsoluteAndRelativeError:
    def __init__(self, x: float, y: float):
        """
        Initializes the AbsoluteAndRelativeError object with two float values.
        :param x: The true value.
        :param y: The approximated value.
        """
        self.x = x
        self.y = y
        self.absolute_error = None
        self.relative_error = None
        self.top_quota_absolute_error = None

    def __absolute(self):
        """
        Calculates the absolute error between x and y.
        """
        self.absolute_error = abs(self.x - self.y)

    def __relative(self):
        """
        Calculates the relative error as a ratio of the absolute error to the true value.
        """
        if self.y != 0:
            self.relative_error = self.absolute_error / abs(self.y)

    def __top_quota_absolute_error(self):
        """
        Estimates the upper bound (top quota) of the absolute error based on the number of
        matching decimal digits between x and y. Assumes both values are precise up to 15 decimals.
        Formula: 0.5 * 10^(-d), where d is the number of matching decimal digits.
        """
        str_x = f"{self.x:.15f}"
        str_y = f"{self.y:.15f}"

        decimal_x = str_x.split(".")[1]
        decimal_y = str_y.split(".")[1]

        correct_digits = 0
        for dx, dy in zip(decimal_x, decimal_y):
            if dx == dy:
                correct_digits += 1
            else:
                break

        self.top_quota_absolute_error = 0.5 * 10 ** (-correct_digits)

    def solve(self):
        """
        Performs the calculations and returns a dictionary with the results.
        :return: Dictionary containing the original values, absolute error,
                 relative error, and the upper bound of the absolute error.
        """
        self.__absolute()
        self.__relative()
        self.__top_quota_absolute_error()

        result = convert_to_decimal_and_fraction(
            ['absolute', 'relative', 'top_quota_absolute_error'],
            [self.absolute_error, self.relative_error, self.top_quota_absolute_error]
        )
        result['relative_percentage'] = round(self.relative_error * 100, 10) if self.relative_error is not None \
            else None

        result['x'] = self.x
        result['y'] = self.y

        return result


teste = AbsoluteAndRelativeError(1/9, 0.11)

print(teste.solve())
