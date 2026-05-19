"""
Command-line interface for the calculator package.

Run with:
    python -m calculator.cli
"""

from typing import Callable, Dict

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

BINARY_OPS: Dict[str, Callable[[float, float], float]] = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
    "**": power,
    "%": modulo,
    "//": floor_divide,
    "max": maximum,
    "min": minimum,
}

UNARY_OPS: Dict[str, Callable[[float], float]] = {
    "square": square,
    "cube": cube,
    "neg": negate,
    "abs": absolute,
    "sqrt": square_root,
}


def get_number(prompt: str) -> float:
    """Prompt the user for a number, retrying on invalid input.

    Args:
        prompt: The message shown to the user.

    Returns:
        A valid float entered by the user.
    """
    while True:
        raw = input(prompt).strip()
        try:
            return float(raw)
        except ValueError:
            print(f"  Invalid input '{raw}'. Please enter a numeric value.")


def get_operation(prompt: str, ops_dict: Dict[str, Callable]) -> str:
    """Prompt the user for an operation, retrying on invalid input.

    Args:
        prompt: The message shown to the user.
        ops_dict: Dictionary of valid operations.

    Returns:
        A valid operation key from ops_dict.
    """
    valid_ops = ", ".join(ops_dict.keys())
    while True:
        op = input(prompt).strip()
        if op in ops_dict:
            return op
        print(f"  Unknown operation '{op}'. Choose from: {valid_ops}")


def get_mode() -> str:
    """Prompt the user to choose binary or unary mode.

    Returns:
        'b' for binary or 'u' for unary.
    """
    while True:
        mode = input("Binary or unary operation? (b/u): ").strip().lower()
        if mode in ("b", "u"):
            return mode
        print("  Invalid choice. Enter 'b' for binary or 'u' for unary.")


def main() -> None:
    """Run the interactive calculator session."""
    print("=== Extended Calculator ===")

    mode = get_mode()

    if mode == "b":
        a = get_number("Enter the first number : ")
        op = get_operation(
            "Enter an operation (+, -, *, /, **, %, //, max, min): ", BINARY_OPS
        )
        b = get_number("Enter the second number: ")

        try:
            result = BINARY_OPS[op](a, b)
            print(f"Result: {a} {op} {b} = {result}")
        except ZeroDivisionError as exc:
            print(f"Error: {exc}")

    else:
        op = get_operation(
            "Enter an operation (square, cube, neg, abs, sqrt): ", UNARY_OPS
        )
        a = get_number("Enter a number: ")

        try:
            result = UNARY_OPS[op](a)
            print(f"Result: {op}({a}) = {result}")
        except ValueError as exc:
            print(f"Error: {exc}")


if __name__ == "__main__":
    main()
