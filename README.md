# Calculator

A feature-rich terminal calculator with TUI (Text User Interface) for Linux systems. Type `calculator` in your terminal to launch an interactive calculator with visual button layout.

## Features

- **TUI Mode**: Visual calculator interface with button grid (requires terminal with curses support)
- **Basic Mode**: Fallback command-line calculator (works in any terminal)
- **CLI Mode**: Python package interface for programmatic use
- **20+ Operations**: Basic arithmetic, trigonometry, hyperbolic functions, and ML activation functions
- **No Dependencies**: Uses only Python standard library (curses for TUI)

## Quick Install

One-liner installation (no git clone needed):

```bash
curl -sSL https://raw.githubusercontent.com/RG8420/calculator/main/install.sh | bash
```

Then open a new terminal and type:
```bash
calculator
```

## Manual Install

```bash
git clone https://github.com/RG8420/calculator.git
cd calculator
bash install.sh
```

## Usage

### TUI Mode (Recommended)

In a terminal with curses support, you'll see:

```
┌─────────────────────────┐
│              0.00      │
├─────────────────────────┤
│  7    8    9    /   *  │
│  4    5    6    -   +  │
│  1    2    3    =   %  │
│      0     .   C       │
└─────────────────────────┘
```

### Keyboard Shortcuts

| Key | Action |
|-----|--------|
| `0-9` | Input numbers |
| `.` | Decimal point |
| `+` | Addition |
| `-` | Subtraction |
| `*` | Multiplication |
| `/` | Division |
| `%` | Modulo |
| `^` | Power |
| `//` | Floor divide (press `/` twice) |
| `=` / `Enter` | Calculate |
| `C` / `Escape` | Clear |

#### Unary Operations (press after entering a number)

| Key | Operation | Example |
|-----|-----------|---------|
| `q` | Square | `5` then `q` → `25` |
| `r` | Square root | `16` then `r` → `4` |
| `c` | Cube | `3` then `c` → `27` |
| `n` | Negate | `5` then `n` → `-5` |
| `a` | Absolute | `-5` then `a` → `5` |
| `l` | Natural log (ln) | `10` then `l` → `2.30` |
| `x` | Exponential (e^x) | `1` then `x` → `2.72` |
| `s` | Sine (radians) | `0` then `s` → `0` |
| `k` | Cosine | `0` then `k` → `1` |
| `t` | Tangent | `0` then `t` → `0` |
| `y` | Hyperbolic tan (tanh) | `1` then `y` → `0.76` |
| `u` | ReLU | `-3` then `u` → `0` |
| `g` | Sigmoid | `0` then `g` → `0.5` |
| `M` | Maximum (vs 0) | `5` then `M` → `5` |
| `m` | Minimum (vs 0) | `5` then `m` → `0` |
| `h` | Show help |

### Basic Mode

If TUI isn't supported, it falls back to command-line mode:

```bash
$ calculator
=== Basic Calculator (No TUI) ===
Type expressions like: 10 + 5
Type 'help' for operations, 'quit' to exit.

> 10 + 5
  = 15
> sqrt 16
  = 4
> quit
```

#### Basic Mode Syntax

- Binary: `<num> <op> <num>` → `10 + 5`
- Unary: `<op> <num>` → `sqrt 16`

### Python Package Usage

```python
from calculator import add, subtract, multiply, divide
from calculator import square, sqrt, sin, cos, tan
from calculator import relu, sigmoid, tanh

# Basic operations
add(3, 4)           # 7
subtract(10, 3)     # 7
multiply(4, 5)     # 20
divide(10, 2)      # 5.0

# Unary operations
square(5)          # 25
sqrt(16)           # 4.0
sin(0)             # 0.0
cos(0)             # 1.0
tanh(1)            # 0.7615941559557649
relu(-5)           # 0
sigmoid(0)         # 0.5
```

## Operations Reference

### Binary Operations

| Symbol | Name | Example |
|--------|------|---------|
| `+` | Addition | `10 + 5` → `15` |
| `-` | Subtraction | `10 - 3` → `7` |
| `*` | Multiplication | `4 * 5` → `20` |
| `/` | Division | `10 / 2` → `5` |
| `%` | Modulo | `10 % 3` → `1` |
| `^` | Power | `2 ^ 8` → `256` |
| `//` | Floor divide | `7 // 2` → `3` |
| `max` | Maximum | `max 5 9` → `9` |
| `min` | Minimum | `min 5 9` → `5` |

### Unary Operations

| Key | Name | Example |
|-----|------|---------|
| `square` | Square | `square 5` → `25` |
| `cube` | Cube | `cube 3` → `27` |
| `sqrt` | Square root | `sqrt 16` → `4` |
| `neg` | Negate | `neg 5` → `-5` |
| `abs` | Absolute | `abs -5` → `5` |
| `log` | Natural log | `log 10` → `2.30` |
| `exp` | Exponential | `exp 1` → `2.72` |
| `sin` | Sine (radians) | `sin 0` → `0` |
| `cos` | Cosine | `cos 0` → `1` |
| `tan` | Tangent | `tan 0` → `0` |
| `tanh` | Hyperbolic tan | `tanh 1` → `0.76` |
| `relu` | ReLU | `relu -3` → `0` |
| `sigmoid` | Sigmoid | `sigmoid 0` → `0.5` |

## Uninstall

```bash
bash install.sh --uninstall
```

Or manually:

```bash
bash uninstall.sh
```

## Development

### Run Tests

```bash
pip install pytest pytest-cov
pytest tests/ -v
```

### Project Structure

```
calculator/
├── .github/workflows/   # GitHub Actions CI
├── calculator/          # Python package
│   ├── __init__.py      # Package exports
│   ├── cli.py           # CLI interface
│   ├── operations.py   # Math operations
│   └── repl.py          # TUI calculator
├── tests/               # Test suite
│   ├── test_operations.py
│   └── test_repl.py
├── install.sh           # Installation script
├── uninstall.sh         # Uninstallation script
├── pyproject.toml       # Package config
├── requirements.txt     # Dev dependencies
└── LICENSE              # MIT License
```

## License

MIT License - See [LICENSE](LICENSE) file.

## Author

Rahul Golder