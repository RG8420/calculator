"""
Core arithmetic operations for the calculator package.
"""


def add(a: float, b: float) -> float:
    """Return the sum of a and b.

    Args:
        a: The first number.
        b: The second number.

    Returns:
        The result of a + b.
    """
    return a + b


def subtract(a: float, b: float) -> float:
    """Return the difference of a and b.

    Args:
        a: The first number.
        b: The second number.

    Returns:
        The result of a - b.
    """
    return a - b


def multiply(a: float, b: float) -> float:
    """Return the product of a and b.

    Args:
        a: The first number.
        b: The second number.

    Returns:
        The result of a * b.
    """
    return a * b


def divide(a: float, b: float) -> float:
    """Return the quotient of a and b.

    Args:
        a: The dividend.
        b: The divisor.

    Returns:
        The result of a / b.

    Raises:
        ZeroDivisionError: If b is zero.
    """
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b


def power(a: float, b: float) -> float:
    """Return a raised to the power b.

    Args:
        a: The base.
        b: The exponent.

    Returns:
        The result of a ** b.
    """
    return a ** b


def modulo(a: float, b: float) -> float:
    """Return the remainder of a divided by b.

    Args:
        a: The dividend.
        b: The divisor.

    Returns:
        The result of a % b.

    Raises:
        ZeroDivisionError: If b is zero.
    """
    if b == 0:
        raise ZeroDivisionError("Cannot modulo by zero.")
    return a % b


def floor_divide(a: float, b: float) -> float:
    """Return the floor division of a by b.

    Args:
        a: The dividend.
        b: The divisor.

    Returns:
        The result of a // b.

    Raises:
        ZeroDivisionError: If b is zero.
    """
    if b == 0:
        raise ZeroDivisionError("Cannot floor divide by zero.")
    return a // b


def maximum(a: float, b: float) -> float:
    """Return the larger of a and b.

    Args:
        a: The first number.
        b: The second number.

    Returns:
        The maximum of a and b.
    """
    return max(a, b)


def minimum(a: float, b: float) -> float:
    """Return the smaller of a and b.

    Args:
        a: The first number.
        b: The second number.

    Returns:
        The minimum of a and b.
    """
    return min(a, b)


def square(a: float) -> float:
    """Return the square of a.

    Args:
        a: The number to square.

    Returns:
        The result of a².
    """
    return a ** 2


def cube(a: float) -> float:
    """Return the cube of a.

    Args:
        a: The number to cube.

    Returns:
        The result of a³.
    """
    return a ** 3


def negate(a: float) -> float:
    """Return the negation of a.

    Args:
        a: The number to negate.

    Returns:
        The result of -a.
    """
    return -a


def absolute(a: float) -> float:
    """Return the absolute value of a.

    Args:
        a: The number.

    Returns:
        The absolute value of a.
    """
    return abs(a)


def square_root(a: float) -> float:
    """Return the square root of a.

    Args:
        a: The number.

    Returns:
        The square root of a.

    Raises:
        ValueError: If a is negative.
    """
    if a < 0:
        raise ValueError("Cannot take square root of a negative number.")
    return a ** 0.5


def logarithm(a: float) -> float:
    """Return the natural logarithm of a.

    Args:
        a: The number.

    Returns:
        The natural log (ln) of a.

    Raises:
        ValueError: If a is negative or zero.
    """
    if a <= 0:
        raise ValueError("Cannot take logarithm of non-positive number.")
    import math
    return math.log(a)


def exponential(a: float) -> float:
    """Return e raised to the power of a.

    Args:
        a: The exponent.

    Returns:
        The result of e^a.
    """
    import math
    return math.exp(a)


def sine(a: float) -> float:
    """Return the sine of a (in radians).

    Args:
        a: The angle in radians.

    Returns:
        The sine of a.
    """
    import math
    return math.sin(a)


def cosine(a: float) -> float:
    """Return the cosine of a (in radians).

    Args:
        a: The angle in radians.

    Returns:
        The cosine of a.
    """
    import math
    return math.cos(a)


def tangent(a: float) -> float:
    """Return the tangent of a (in radians).

    Args:
        a: The angle in radians.

    Returns:
        The tangent of a.

    Raises:
        ValueError: If cosine is zero.
    """
    import math
    return math.tan(a)


def hyperbolic_tangent(a: float) -> float:
    """Return the hyperbolic tangent of a.

    Args:
        a: The number.

    Returns:
        The hyperbolic tangent of a.
    """
    import math
    return math.tanh(a)


def relu(a: float) -> float:
    """Return the Rectified Linear Unit of a.

    Args:
        a: The number.

    Returns:
        max(0, a)
    """
    return max(0, a)


def sigmoid(a: float) -> float:
    """Return the sigmoid function of a.

    Args:
        a: The number.

    Returns:
        1 / (1 + e^(-a))
    """
    import math
    return 1 / (1 + math.exp(-a))
