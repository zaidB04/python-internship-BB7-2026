
class RationalNumber:
    def __init__(self, num, den):
        if den == 0:
            raise ValueError("Denominator must not be zero.")

        self.num = num
        self.den = den

    def __add__(self, other):
        numerator = (self.num * other.den) + \
                    (other.num * self.den)

        denominator = self.den * other.den

        return RationalNumber(numerator, denominator)


num1 = RationalNumber(2, 5)
num2 = RationalNumber(1, 5)

sum_result = num1 + num2

print("Sum of fractions:", sum_result.num, "/", sum_result.den)
