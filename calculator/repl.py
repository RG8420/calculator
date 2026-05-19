"""
TUI (Text User Interface) Calculator for the terminal.

Run with:
    python -m calculator.repl

Or, after installing:
    calculator

Keyboard shortcuts:
    0-9, .         - Input numbers
    +, -, *, /     - Basic operations
    %              - Modulo
    ^              - Power
    //             - Floor divide (press / twice quickly)
    =, Enter       - Calculate
    C, Escape      - Clear
    q              - Square
    r              - Square root
    c              - Cube (when operand pending)
    n              - Negate
    a              - Absolute
    M              - Maximum
    m              - Minimum
    l              - Natural log (ln)
    x              - Exponential (e^x)
    s              - Sine (sin)
    k              - Cosine (cos)
    t              - Tangent (tan)
    y              - Hyperbolic tan (tanh)
    u              - ReLU
    g              - Sigmoid
    h              - Show help
"""

import curses
import sys
import time
from calculator import (
    absolute,
    add,
    cube,
    divide,
    exponential,
    floor_divide,
    hyperbolic_tangent,
    logarithm,
    maximum,
    minimum,
    modulo,
    multiply,
    negate,
    power,
    relu,
    sigmoid,
    sine,
    cosine,
    tangent,
    square,
    square_root,
    subtract,
)


class Calculator:
    def __init__(self):
        self.display = "0"
        self.first_operand = None
        self.operator = None
        self.waiting_for_second = False
        self.last_slash_time = 0
        self.show_help = False
        self.error_message = None

    def clear(self):
        self.display = "0"
        self.first_operand = None
        self.operator = None
        self.waiting_for_second = False
        self.error_message = None

    def input_digit(self, digit: str):
        if self.error_message:
            self.clear()
        
        if self.waiting_for_second:
            self.display = digit
            self.waiting_for_second = False
        else:
            if self.display == "0":
                self.display = digit
            else:
                self.display += digit
        self._truncate_display()

    def input_decimal(self):
        if self.error_message:
            self.clear()
        
        if self.waiting_for_second:
            self.display = "0."
            self.waiting_for_second = False
        elif "." not in self.display:
            self.display += "."

    def set_operator(self, op: str):
        if self.error_message:
            self.clear()

        if self.first_operand is None:
            self.first_operand = float(self.display)
        elif self.waiting_for_second:
            self.operator = op
        else:
            self._calculate()
            self.first_operand = float(self.display)
        
        self.operator = op
        self.waiting_for_second = True

    def _calculate(self):
        if self.first_operand is None or self.operator is None:
            return

        try:
            second = float(self.display)
            result = self._apply_operator(self.first_operand, self.operator, second)
            self.display = self._format_result(result)
            self.first_operand = result
            self.operator = None
            self.waiting_for_second = True
        except ZeroDivisionError:
            self.error_message = "Error: Division by zero"
            self.display = "0"
            self.first_operand = None
            self.operator = None
        except Exception as e:
            self.error_message = f"Error: {str(e)}"
            self.display = "0"
            self.first_operand = None
            self.operator = None

    def _apply_operator(self, a: float, op: str, b: float) -> float:
        if op == "+":
            return add(a, b)
        elif op == "-":
            return subtract(a, b)
        elif op == "*":
            return multiply(a, b)
        elif op == "/":
            return divide(a, b)
        elif op == "%":
            return modulo(a, b)
        elif op == "^":
            return power(a, b)
        elif op == "//":
            return floor_divide(a, b)
        elif op == "max":
            return maximum(a, b)
        elif op == "min":
            return minimum(a, b)
        return b

    def _format_result(self, value: float):
        if value == int(value):
            return str(int(value))
        return str(value)[:15]

    def _truncate_display(self):
        if len(self.display) > 15:
            self.display = self.display[:15]

    def calculate(self):
        if self.operator is not None:
            self._calculate()

    def apply_unary(self, op: str):
        if self.error_message:
            self.clear()

        try:
            value = float(self.display)
            if op == "square":
                result = square(value)
            elif op == "sqrt":
                result = square_root(value)
            elif op == "cube":
                result = cube(value)
            elif op == "neg":
                result = negate(value)
            elif op == "abs":
                result = absolute(value)
            elif op == "max":
                result = maximum(value, 0)
            elif op == "min":
                result = minimum(value, 0)
            elif op == "log":
                result = logarithm(value)
            elif op == "exp":
                result = exponential(value)
            elif op == "sin":
                result = sine(value)
            elif op == "cos":
                result = cosine(value)
            elif op == "tan":
                result = tangent(value)
            elif op == "tanh":
                result = hyperbolic_tangent(value)
            elif op == "relu":
                result = relu(value)
            elif op == "sigmoid":
                result = sigmoid(value)
            else:
                return
            
            self.display = self._format_result(result)
            if self.first_operand is not None and not self.waiting_for_second:
                self.first_operand = result
        except Exception as e:
            self.error_message = f"Error: {str(e)}"
            self.display = "0"

    def get_display_text(self) -> str:
        if self.error_message:
            return self.error_message
        
        text = self.display
        if self.operator and self.waiting_for_second:
            text += f" {self.operator}"
        return text


HELP_TEXT = """
╔══════════════════════════════════════╗
║         CALCULATOR HELP              ║
╠══════════════════════════════════════╣
║  Input:                              ║
║    0-9     Enter digits              ║
║    .        Decimal point            ║
║                                      ║
║  Basic Operations:                   ║
║    +        Add                     ║
║    -        Subtract                 ║
║    *        Multiply                 ║
║    /        Divide                   ║
║    %        Modulo                   ║
║    ^        Power                    ║
║    //       Floor divide             ║
║           (press / twice)            ║
║                                      ║
║  Unary Operations:                   ║
║    q        Square (x²)              ║
║    r        Square root (√)          ║
║    c        Cube (x³)                ║
║    n        Negate                   ║
║    a        Absolute value           ║
║    M        Maximum                  ║
║    m        Minimum                  ║
║    l        Natural log (ln)         ║
║    e        Exponential (e^x)        ║
║    s        Sine (sin)               ║
║    o        Cosine (cos)             ║
║    t        Tangent (tan)            ║
║    y        Hyperbolic tan (tanh)    ║
║    u        ReLU activation          ║
║    g        Sigmoid activation       ║
║                                      ║
║  Other:                              ║
║    =, Enter  Calculate               ║
║    C, Esc    Clear                   ║
║    h        Toggle this help         ║
║    q        Quit (from help)         ║
╚══════════════════════════════════════╝
"""


def run_calculator(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(True)
    stdscr.keypad(True)

    calc = Calculator()
    height, width = stdscr.getmaxyx()

    while True:
        stdscr.clear()

        h, w = stdscr.getmaxyx()
        
        display_text = calc.get_display_text()
        display_width = max(len(display_text), 15)
        
        box_width = display_width + 4
        box_start_x = (w - box_width) // 2
        
        stdscr.addstr(2, box_start_x, "┌" + "─" * box_width + "┐")
        stdscr.addstr(3, box_start_x, "│ " + display_text.rjust(display_width) + " │")
        stdscr.addstr(4, box_start_x, "└" + "─" * box_width + "┘")

        if calc.show_help:
            help_lines = HELP_TEXT.split("\n")
            start_y = (h - len(help_lines)) // 2
            start_x = (w - 34) // 2
            for i, line in enumerate(help_lines):
                if start_y + i < h - 1:
                    stdscr.addstr(start_y + i, start_x, line)
            stdscr.addstr(h - 3, 2, "Press 'q' to close help")
        else:
            stdscr.addstr(h - 6, 2, "┌─────┬─────┬─────┬─────┬─────┐")
            stdscr.addstr(h - 5, 2, "│  7  │  8  │  9  │  /  │  *  │")
            stdscr.addstr(h - 4, 2, "├─────┼─────┼─────┼─────┼─────┤")
            stdscr.addstr(h - 3, 2, "│  4  │  5  │  6  │  -  │  +  │")
            stdscr.addstr(h - 2, 2, "├─────┼─────┼─────┼─────┼─────┤")
            stdscr.addstr(h - 1, 2, "│  1  │  2  │  3  │  =  │  %  │")
            stdscr.addstr(h, 2,   "└─────┴─────┴─────┴─────┴─────┘")
            
            stdscr.addstr(h + 1, 2, "Press h for help | C=Clear | //=Floor divide")

        stdscr.refresh()

        try:
            key = stdscr.getch()
        except:
            key = -1

        if key == -1:
            curses.napms(50)
            continue

        if calc.show_help:
            if key in (ord('q'), ord('Q'), 27):
                calc.show_help = False
            continue

        current_time = time.time()

        if ord('0') <= key <= ord('9'):
            calc.input_digit(chr(key))
        elif key == ord('.'):
            calc.input_decimal()
        elif key == ord('+'):
            calc.set_operator('+')
        elif key == ord('-'):
            calc.set_operator('-')
        elif key == ord('*'):
            calc.set_operator('*')
        elif key == ord('%'):
            calc.set_operator('%')
        elif key == ord('^'):
            calc.set_operator('^')
        elif key == ord('/'):
            if current_time - calc.last_slash_time < 1.0:
                calc.set_operator('//')
                calc.last_slash_time = 0
            else:
                calc.set_operator('/')
                calc.last_slash_time = current_time
        elif key in (ord('='), 10, 13):
            calc.calculate()
        elif key in (ord('C'), ord('c'), 27):
            calc.clear()
        elif key in (ord('Q'), ord('q')) and not calc.waiting_for_second:
            calc.apply_unary('square')
        elif key in (ord('R'), ord('r')):
            calc.apply_unary('sqrt')
        elif key in (ord('C'), ord('c')) and calc.waiting_for_second:
            calc.apply_unary('cube')
        elif key in (ord('N'), ord('n')):
            calc.apply_unary('neg')
        elif key in (ord('A'), ord('a')):
            calc.apply_unary('abs')
        elif key == ord('M'):
            calc.apply_unary('max')
        elif key == ord('m'):
            calc.apply_unary('min')
        elif key in (ord('L'), ord('l')):
            calc.apply_unary('log')
        elif key in (ord('X'), ord('x')):
            calc.apply_unary('exp')
        elif key in (ord('S'), ord('s')):
            calc.apply_unary('sin')
        elif key in (ord('K'), ord('k')):
            calc.apply_unary('cos')
        elif key in (ord('T'), ord('t')):
            calc.apply_unary('tan')
        elif key in (ord('Y'), ord('y')):
            calc.apply_unary('tanh')
        elif key in (ord('U'), ord('u')):
            calc.apply_unary('relu')
        elif key in (ord('G'), ord('g')):
            calc.apply_unary('sigmoid')
        elif key in (ord('H'), ord('h')):
            calc.show_help = True
        elif key in (ord('Q'), ord('q')) and calc.waiting_for_second:
            break


def main():
    try:
        curses.wrapper(run_calculator)
    except curses.error:
        print("Error: Terminal doesn't support curses. Please use a proper terminal.")
        print("Running in basic mode...")
        basic_mode()


def basic_mode():
    print("=== Basic Calculator (No TUI) ===")
    print("Type expressions like: 10 + 5")
    print("Type 'help' for operations, 'quit' to exit.\n")
    
    calc = Calculator()
    while True:
        try:
            line = input("> ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!")
            break

        if not line:
            continue

        if line.lower() in ("quit", "exit"):
            break

        if line.lower() == "help":
            print(HELP_TEXT)
            continue

        tokens = line.split()
        
        if len(tokens) == 1 and tokens[0].lower() == 'c':
            calc.clear()
            print(f"  = {calc.display}")
            continue
        
        if len(tokens) == 2:
            op_token, num_token = tokens
            calc.clear()
            calc.display = num_token
            calc.apply_unary(op_token)
        elif len(tokens) == 3:
            calc.clear()
            first, op, third = tokens
            calc.display = first
            calc.set_operator(op)
            calc.display = third
            calc.calculate()
        else:
            print("  Usage: <num> <op> <num>  or  <op> <num>")
            continue

        print(f"  = {calc.display}")


if __name__ == "__main__":
    main()