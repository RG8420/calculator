# Calculator

A command-line calculator for Linux written in C. Simple, fast, and portable with no external dependencies beyond the standard C library.

## Features

- **22 Operations**: Basic arithmetic, trigonometry, hyperbolic functions, and ML activation functions
- **Portable**: Written in pure C, compiles with GCC
- **No Dependencies**: Only requires GCC and standard C library (libm)
- **Easy Install**: One-liner installation or manual build

## Quick Install

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
make
sudo make install
```

For user-level installation (no sudo):
```bash
make install PREFIX=$HOME/.local
```

## Usage

```bash
$ calculator
=== Calculator (C) ===
Type 'help' for operations, 'quit' to exit.

> 10 + 5
  = 15
> sqrt 16
  = 4
> sigmoid 0
  = 0.5
> quit
```

### Syntax

- **Binary**: `<num> <op> <num>` → `10 + 5`
- **Unary**: `<op> <num>` → `sqrt 16`
- **Commands**: `help`, `quit`, `clear`

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

| Operation | Name | Example |
|-----------|------|---------|
| `square` | Square | `square 5` → `25` |
| `cube` | Cube | `cube 3` → `27` |
| `sqrt` | Square root | `sqrt 16` → `4` |
| `neg` | Negate | `neg 5` → `-5` |
| `abs` | Absolute | `abs -5` → `5` |
| `log` | Natural log | `log 10` → `2.302585093` |
| `exp` | Exponential | `exp 1` → `2.718281828` |
| `sin` | Sine (radians) | `sin 0` → `0` |
| `cos` | Cosine | `cos 0` → `1` |
| `tan` | Tangent | `tan 0` → `0` |
| `tanh` | Hyperbolic tan | `tanh 1` → `0.7615941559557649` |
| `relu` | ReLU | `relu -3` → `0` |
| `sigmoid` | Sigmoid | `sigmoid 0` → `0.5` |

## Build Options

### Makefile Targets

```bash
make           # Build the calculator
make clean     # Remove build files
make install   # Install to /usr/local/bin (requires sudo)
make uninstall # Remove installed calculator
make test      # Run basic tests
make help      # Show help
```

### Custom Installation

```bash
# Install to custom location
make install PREFIX=/opt/calculator

# User-level installation
make install PREFIX=$HOME/.local
```

## Uninstall

```bash
bash install.sh --uninstall
```

Or manually:

```bash
sudo make uninstall
# or for user installation
make uninstall PREFIX=$HOME/.local
```

## Project Structure

```
calculator/
├── .github/workflows/   # GitHub Actions CI
├── src/                 # C source code
│   ├── main.c           # Entry point
│   ├── calculator.c     # Calculator logic
│   ├── calculator.h     # Header file
│   └── operations.c     # Math operations
├── Makefile             # Build system
├── install.sh           # Installation script
├── uninstall.sh         # Uninstallation script
├── LICENSE              # MIT License
└── README.md            # This file
```

## Requirements

- GCC (tested with GCC 11+)
- Linux/Unix system
- GNU Make

## License

MIT License - See [LICENSE](LICENSE) file.

## Author

Rahul Golder