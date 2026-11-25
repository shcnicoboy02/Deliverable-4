"""A module to define a Fraction class and its operations."""

from __future__ import annotations
import math


class Fraction:
    """A class to represent a fraction with a numerator and denominator.
    The fraction is always stored in its simplest form, and the denominator is always positive.
    """
    def __init__(self, numerator: int, denominator: int) -> None:
        """Initialize a Fraction with a numerator and denominator."""
        if not isinstance(numerator, int) or not isinstance(denominator, int):
            raise TypeError("Numerator and denominator must be integers")
        if denominator <= 0:
            raise ValueError("Denominator must be a positive integer")
        # Simplify the fraction using the greatest common divisor (gcd)
        gcd = math.gcd(numerator, denominator)
        self.numerator = numerator // gcd
        self.denominator = denominator // gcd  

    def __repr__(self) -> str:
        """Return the official string representation of the fraction."""
        return f"Fraction({self.numerator}, {self.denominator})"
        
    def __str__(self) -> str:
        """Return the string representation of the fraction in the form "numerator/denominator"."""
        return f"{self.numerator}/{self.denominator}"

    def __add__(self, other: Fraction) -> Fraction:
        """Add two fractions: a/b + c/d = (a*d + b*c) / (b*d)"""
        if not isinstance(other, Fraction):
            raise TypeError("Can only add Fraction to Fraction")
        new_numerator = (self.numerator * other.denominator) + (other.numerator * self.denominator)
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __sub__(self, other: Fraction) -> Fraction:
        """Subtract two fractions: a/b - c/d = (a*d - b*c) / (b*d)"""
        if not isinstance(other, Fraction):
            raise TypeError("Can only subtract Fraction from Fraction")
        new_numerator = (self.numerator * other.denominator) - (other.numerator * self.denominator)
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __mul__(self, other: Fraction) -> Fraction:
        """Multiply two fractions: a/b * c/d = (a*c) / (b*d)"""
        if not isinstance(other, Fraction):
            raise TypeError("Can only multiply Fraction by Fraction")
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __truediv__(self, other: Fraction) -> Fraction:
        """Divide two fractions: a/b / c/d = (a*d) / (b*c)"""
        if not isinstance(other, Fraction):
            raise TypeError("Can only divide Fraction by Fraction")
        new_numerator = self.numerator * other.denominator
        new_denominator = self.denominator * other.numerator
        return Fraction(new_numerator, new_denominator)

    def __eq__(self, other: object) -> bool:
        """Check equality of two fractions: a/b == c/d if and only if a*d == b*c"""
        if not isinstance(other, Fraction):
            return False
        return (self.numerator * other.denominator) == (other.numerator * self.denominator)

    def __ne__(self, other: object) -> bool:
        """Check inequality of two fractions: a/b != c/d if and only if a*d != b*c"""
        if not isinstance(other, Fraction):
            return True
        return (self.numerator * other.denominator) != (other.numerator * self.denominator)

    def __lt__(self, other: Fraction) -> bool:
        """Less than comparison"""
        if not isinstance(other, Fraction):
            raise TypeError("Can only compare Fraction with Fraction")
        return (self.numerator * other.denominator) < (other.numerator * self.denominator)

    def __gt__(self, other: Fraction) -> bool:
        """Greater than comparison"""
        if not isinstance(other, Fraction):
            raise TypeError("Can only compare Fraction with Fraction")
        return (self.numerator * other.denominator) > (other.numerator * self.denominator)

    def __le__(self, other: Fraction) -> bool:
        """Less than or equal comparison"""
        if not isinstance(other, Fraction):
            raise TypeError("Can only compare Fraction with Fraction")
        return (self.numerator * other.denominator) <= (other.numerator * self.denominator)

    def __ge__(self, other: Fraction) -> bool:
        """Greater than or equal comparison"""
        if not isinstance(other, Fraction):
            raise TypeError("Can only compare Fraction with Fraction")
        return (self.numerator * other.denominator) >= (other.numerator * self.denominator)
    