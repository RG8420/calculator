"""
Unit tests for calculator.operations.
"""

import pytest

from calculator import (
    absolute,
    add,
    cube,
    divide,
    floor_divide,
    maximum,
    minimum,
    modulo,
    multiply,
    negate,
    power,
    square,
    square_root,
    subtract,
)


class TestAdd:
    def test_two_positive_numbers(self):
        assert add(3, 4) == 7

    def test_positive_and_negative(self):
        assert add(10, -3) == 7

    def test_two_negatives(self):
        assert add(-2, -5) == -7

    def test_floats(self):
        assert add(1.5, 2.5) == pytest.approx(4.0)

    def test_zero_identity(self):
        assert add(0, 99) == 99


class TestSubtract:
    def test_positive_result(self):
        assert subtract(10, 4) == 6

    def test_negative_result(self):
        assert subtract(3, 8) == -5

    def test_same_numbers(self):
        assert subtract(7, 7) == 0

    def test_floats(self):
        assert subtract(5.5, 2.2) == pytest.approx(3.3)


class TestMultiply:
    def test_two_positives(self):
        assert multiply(3, 4) == 12

    def test_multiply_by_zero(self):
        assert multiply(999, 0) == 0

    def test_negative_times_positive(self):
        assert multiply(-3, 4) == -12

    def test_two_negatives(self):
        assert multiply(-3, -4) == 12

    def test_floats(self):
        assert multiply(2.5, 4.0) == pytest.approx(10.0)


class TestDivide:
    def test_exact_division(self):
        assert divide(10, 2) == 5.0

    def test_float_result(self):
        assert divide(7, 2) == pytest.approx(3.5)

    def test_negative_dividend(self):
        assert divide(-9, 3) == pytest.approx(-3.0)

    def test_two_negatives(self):
        assert divide(-8, -4) == pytest.approx(2.0)

    def test_divide_by_zero_raises(self):
        with pytest.raises(ZeroDivisionError, match="Cannot divide by zero"):
            divide(5, 0)

    def test_divide_zero_by_nonzero(self):
        assert divide(0, 5) == 0.0


class TestPower:
    def test_positive_exponent(self):
        assert power(2, 3) == pytest.approx(8.0)

    def test_negative_exponent(self):
        assert power(2, -2) == pytest.approx(0.25)

    def test_zero_exponent(self):
        assert power(5, 0) == pytest.approx(1.0)

    def test_fractional_exponent(self):
        assert power(4, 0.5) == pytest.approx(2.0)

    def test_negative_base(self):
        assert power(-2, 3) == pytest.approx(-8.0)


class TestModulo:
    def test_positive_numbers(self):
        assert modulo(10, 3) == pytest.approx(1.0)

    def test_negative_dividend(self):
        assert modulo(-10, 3) == pytest.approx(2.0)

    def test_zero_dividend(self):
        assert modulo(0, 5) == pytest.approx(0.0)

    def test_modulo_by_zero_raises(self):
        with pytest.raises(ZeroDivisionError, match="Cannot modulo by zero"):
            modulo(5, 0)


class TestFloorDivide:
    def test_exact_division(self):
        assert floor_divide(10, 2) == pytest.approx(5.0)

    def test_truncates_toward_negative_infinity(self):
        assert floor_divide(7, 2) == pytest.approx(3.0)

    def test_negative_dividend(self):
        assert floor_divide(-7, 2) == pytest.approx(-4.0)

    def test_floor_divide_by_zero_raises(self):
        with pytest.raises(ZeroDivisionError, match="Cannot floor divide by zero"):
            floor_divide(5, 0)


class TestMaximum:
    def test_two_positives(self):
        assert maximum(3, 7) == pytest.approx(7.0)

    def test_positive_and_negative(self):
        assert maximum(-5, 3) == pytest.approx(3.0)

    def test_two_negatives(self):
        assert maximum(-10, -3) == pytest.approx(-3.0)

    def test_equal_values(self):
        assert maximum(5, 5) == pytest.approx(5.0)


class TestMinimum:
    def test_two_positives(self):
        assert minimum(3, 7) == pytest.approx(3.0)

    def test_positive_and_negative(self):
        assert minimum(-5, 3) == pytest.approx(-5.0)

    def test_two_negatives(self):
        assert minimum(-10, -3) == pytest.approx(-10.0)

    def test_equal_values(self):
        assert minimum(5, 5) == pytest.approx(5.0)


class TestSquare:
    def test_positive_number(self):
        assert square(5) == pytest.approx(25.0)

    def test_negative_number(self):
        assert square(-4) == pytest.approx(16.0)

    def test_zero(self):
        assert square(0) == pytest.approx(0.0)

    def test_float(self):
        assert square(2.5) == pytest.approx(6.25)


class TestCube:
    def test_positive_number(self):
        assert cube(3) == pytest.approx(27.0)

    def test_negative_number(self):
        assert cube(-2) == pytest.approx(-8.0)

    def test_zero(self):
        assert cube(0) == pytest.approx(0.0)

    def test_float(self):
        assert cube(2.0) == pytest.approx(8.0)


class TestNegate:
    def test_positive_number(self):
        assert negate(5) == pytest.approx(-5.0)

    def test_negative_number(self):
        assert negate(-3) == pytest.approx(3.0)

    def test_zero(self):
        assert negate(0) == pytest.approx(0.0)


class TestAbsolute:
    def test_positive_number(self):
        assert absolute(5) == pytest.approx(5.0)

    def test_negative_number(self):
        assert absolute(-7) == pytest.approx(7.0)

    def test_zero(self):
        assert absolute(0) == pytest.approx(0.0)


class TestSquareRoot:
    def test_perfect_square(self):
        assert square_root(9) == pytest.approx(3.0)

    def test_non_perfect_square(self):
        assert square_root(2) == pytest.approx(1.414213, rel=1e-5)

    def test_zero(self):
        assert square_root(0) == pytest.approx(0.0)

    def test_large_number(self):
        assert square_root(100) == pytest.approx(10.0)

    def test_negative_raises(self):
        with pytest.raises(
            ValueError, match="Cannot take square root of a negative number"
        ):
            square_root(-4)
