
import pytest
from fraction import Fraction

def test_init():
    f = Fraction(1, 2)
    assert f.numerator == 1 and f.denominator == 2

def test_str():
    f = Fraction(3, 4)
    assert str(f) == "3/4"

def test_repr():
    f = Fraction(3, 4)
    assert repr(f) == "Fraction(3, 4)"

def test_addition():
    f1 = Fraction(1, 2)
    f2 = Fraction(1, 3)
    result = f1 + f2
    assert result.numerator == 5 and result.denominator == 6

def test_subtraction():
    f1 = Fraction(3, 4)
    f2 = Fraction(1, 4)
    result = f1 - f2
    assert result.numerator == 1 and result.denominator == 2

def test_multiplication():
    f1 = Fraction(2, 3)
    f2 = Fraction(3, 4)
    result = f1 * f2
    assert result.numerator == 1 and result.denominator == 2

def test_division():
    f1 = Fraction(3, 5)
    f2 = Fraction(2, 7)
    result = f1 / f2
    assert result.numerator == 21 and result.denominator == 10

def test_equality():
    f1 = Fraction(1, 2)
    f2 = Fraction(1, 2)
    assert f1 == f2

def test_inequality():
    f1 = Fraction(1, 2)
    f2 = Fraction(2, 3)
    assert f1 != f2

def test_less_than():
    f1 = Fraction(1, 2)
    f2 = Fraction(2, 3)
    assert f1 < f2

def test_greater_than():
    f1 = Fraction(2, 3)
    f2 = Fraction(1, 2)
    assert f1 > f2

def test_less_than_or_equal():
    f1 = Fraction(1, 2)
    f2 = Fraction(1, 2)
    assert f1 <= f2

def test_greater_than_or_equal():
    f1 = Fraction(1, 2)
    f2 = Fraction(1, 2)
    assert f1 >= f2

