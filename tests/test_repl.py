"""
Unit tests for the REPL parser (calculator.repl.parse_and_evaluate).
"""

import pytest

from calculator.repl import parse_and_evaluate


class TestBinaryInfix:
    def test_addition(self):
        assert parse_and_evaluate("3 + 4") == "  = 7.0"

    def test_subtraction(self):
        assert parse_and_evaluate("10 - 3") == "  = 7.0"

    def test_multiplication(self):
        assert parse_and_evaluate("3 * 4") == "  = 12.0"

    def test_division(self):
        assert parse_and_evaluate("10 / 2") == "  = 5.0"

    def test_power(self):
        assert parse_and_evaluate("2 ** 8") == "  = 256.0"

    def test_modulo(self):
        assert parse_and_evaluate("10 % 3") == "  = 1.0"

    def test_floor_divide(self):
        assert parse_and_evaluate("7 // 2") == "  = 3.0"


class TestBinaryPrefix:
    def test_maximum(self):
        assert parse_and_evaluate("max 3 7") == "  = 7.0"

    def test_minimum(self):
        assert parse_and_evaluate("min 3 7") == "  = 3.0"


class TestUnary:
    def test_square(self):
        assert parse_and_evaluate("square 5") == "  = 25.0"

    def test_cube(self):
        assert parse_and_evaluate("cube 3") == "  = 27.0"

    def test_negate(self):
        assert parse_and_evaluate("neg 7") == "  = -7.0"

    def test_absolute(self):
        assert parse_and_evaluate("abs -4") == "  = 4.0"

    def test_sqrt(self):
        assert parse_and_evaluate("sqrt 9") == "  = 3.0"


class TestErrorCases:
    def test_divide_by_zero(self):
        result = parse_and_evaluate("5 / 0")
        assert "Error" in result and "divide" in result.lower()

    def test_modulo_by_zero(self):
        result = parse_and_evaluate("5 % 0")
        assert "Error" in result and "modulo" in result.lower()

    def test_floor_divide_by_zero(self):
        result = parse_and_evaluate("5 // 0")
        assert "Error" in result and "floor divide" in result.lower()

    def test_sqrt_negative(self):
        result = parse_and_evaluate("sqrt -4")
        assert "Error" in result and "negative" in result.lower()

    def test_unknown_binary_op(self):
        result = parse_and_evaluate("5 @ 3")
        assert "Unknown" in result or "parse" in result.lower()

    def test_unknown_unary_op(self):
        result = parse_and_evaluate("foo 5")
        assert "Unknown" in result

    def test_invalid_number_binary(self):
        result = parse_and_evaluate("abc + 3")
        assert "Invalid" in result

    def test_invalid_number_unary(self):
        result = parse_and_evaluate("sqrt abc")
        assert "Invalid" in result

    def test_empty_tokens(self):
        result = parse_and_evaluate("just_one_token")
        assert "parse" in result.lower() or "unknown" in result.lower()

    def test_too_many_tokens(self):
        result = parse_and_evaluate("1 + 2 + 3")
        assert "parse" in result.lower() or "unknown" in result.lower()
