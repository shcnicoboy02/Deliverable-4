

class Fraction:
    def __init__(self, numerator: int, denominator: int) -> None:
        if not isinstance(numerator, int) or not isinstance(denominator, int):
            raise TypeError("Numerator and denominator must be integers")
        if denominator <= 0:
            raise ValueError("Denominator must be a positive integer")
        self.numerator = numerator
        self.denominator = denominator

    def __repr__(self):
        return f"Fraction({self.numerator}, {self.denominator})"
        
    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def __add__(self, other):
        if not isinstance(other, Fraction):
            raise TypeError("Can only add Fraction to Fraction")
        new_numerator = (self.numerator * other.denominator) + (other.numerator * self.denominator)
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __sub__(self, other):
        if not isinstance(other, Fraction):
            raise TypeError("Can only subtract Fraction from Fraction")
        new_numerator = (self.numerator * other.denominator) - (other.numerator * self.denominator)
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __mul__(self, other):
        if not isinstance(other, Fraction):
            raise TypeError("Can only multiply Fraction by Fraction")
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __truediv__(self, other):
        if not isinstance(other, Fraction):
            raise TypeError("Can only divide Fraction by Fraction")
        new_numerator = self.numerator * other.denominator
        new_denominator = self.denominator * other.numerator
        return Fraction(new_numerator, new_denominator)

    def __eq__(self, other):
        # Equality check: a/b == c/d if and only if a*d == b*c
        if not isinstance(other, Fraction):
            return False
        return (self.numerator * other.denominator) == (other.numerator * self.denominator)

    def __ne__(self, other):
        # Not equal comparison
        if not isinstance(other, Fraction):
            return True
        return (self.numerator * other.denominator) != (other.numerator * self.denominator)

    def __lt__(self, other):
        # Less than comparison
        if not isinstance(other, Fraction):
            raise TypeError("Can only compare Fraction with Fraction")
        return (self.numerator * other.denominator) < (other.numerator * self.denominator)

    def __gt__(self, other):
        # Greater than comparison
        if not isinstance(other, Fraction):
            raise TypeError("Can only compare Fraction with Fraction")
        return (self.numerator * other.denominator) > (other.numerator * self.denominator)

    def __le__(self, other):
        # Less than or equal comparison
        if not isinstance(other, Fraction):
            raise TypeError("Can only compare Fraction with Fraction")
        return (self.numerator * other.denominator) <= (other.numerator * self.denominator)

    def __ge__(self, other):
        # Greater than or equal comparison
        if not isinstance(other, Fraction):
            raise TypeError("Can only compare Fraction with Fraction")
        return (self.numerator * other.denominator) >= (other.numerator * self.denominator)
    


    

    