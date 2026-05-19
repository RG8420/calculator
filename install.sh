#!/bin/bash
# install.sh
# Installs the 'calculator' command on Linux.
#
# Usage:
#   # Quick one-liner:
#   curl -sSL https://raw.githubusercontent.com/RG8420/calculator/main/install.sh | bash
#
#   # Or clone and run locally:
#   git clone https://github.com/RG8420/calculator.git
#   cd calculator
#   bash install.sh
#
# Options:
#   --uninstall  Remove the calculator command

set -eo pipefail

REPO_URL="https://github.com/RG8420/calculator.git"
INSTALL_DIR="$HOME/.local/bin"
SYSTEM_INSTALL_DIR="/usr/local/bin"
BUILD_DIR="$HOME/.calculator-build"

usage() {
    echo "Usage: install.sh [--uninstall]"
    echo "  --uninstall  Remove calculator from system"
    exit 1
}

uninstall_calculator() {
    echo "=== Calculator Uninstaller ==="

    local targets=("$SYSTEM_INSTALL_DIR/calculator" "$INSTALL_DIR/calculator")
    local removed=0

    for target in "${targets[@]}"; do
        if [ -f "$target" ]; then
            rm "$target"
            echo "  Removed $target"
            removed=1
        fi
    done

    if [ -d "$BUILD_DIR" ]; then
        rm -rf "$BUILD_DIR"
        echo "  Removed build directory"
        removed=1
    fi

    if [ $removed -eq 1 ]; then
        echo ""
        echo "  Uninstall complete."
    else
        echo "  Calculator not found - nothing to remove."
    fi
    exit 0
}

if [[ "${1:-}" == "--uninstall" ]]; then
    uninstall_calculator
fi

if [[ "${1:-}" == "-h" ]] || [[ "${1:-}" == "--help" ]]; then
    usage
fi

echo "=== Calculator Installer (C Version) ==="

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

if [[ "$SCRIPT_DIR" == *"/tmp"* ]] || [[ ! -f "$SCRIPT_DIR/Makefile" ]]; then
    echo "[*] Detected run from curl/download - cloning repository..."
    TEMP_DIR=$(mktemp -d)
    git clone --depth 1 "$REPO_URL" "$TEMP_DIR"
    cd "$TEMP_DIR"
    SCRIPT_DIR="$TEMP_DIR"
    CLEANUP_TEMP=1
else
    CLEANUP_TEMP=0
fi

echo "[1/3] Building calculator..."
cd "$SCRIPT_DIR"

if ! command -v gcc &> /dev/null; then
    echo "  Error: GCC not found. Please install GCC."
    exit 1
fi

make clean 2>/dev/null || true
make

echo "[2/3] Installing calculator..."

CALCULATOR_BIN="$SCRIPT_DIR/calculator"

if [ -w "$SYSTEM_INSTALL_DIR" ]; then
    cp "$CALCULATOR_BIN" "$SYSTEM_INSTALL_DIR/calculator"
    chmod +x "$SYSTEM_INSTALL_DIR/calculator"
    echo "  Installed to $SYSTEM_INSTALL_DIR (system-wide)"
    INSTALL_TARGET="$SYSTEM_INSTALL_DIR/calculator"
else
    if [ ! -d "$INSTALL_DIR" ]; then
        mkdir -p "$INSTALL_DIR"
    fi
    cp "$CALCULATOR_BIN" "$INSTALL_DIR/calculator"
    chmod +x "$INSTALL_DIR/calculator"
    echo "  Installed to $INSTALL_DIR (user-level)"
    INSTALL_TARGET="$INSTALL_DIR/calculator"
fi

echo "[3/3] Configuring PATH..."

SHELL_RC="$HOME/.bashrc"
if [ -n "${ZSH_VERSION:-}" ]; then
    SHELL_RC="$HOME/.zshrc"
fi

if [[ "$INSTALL_TARGET" == *"$INSTALL_DIR"* ]]; then
    if ! grep -q "$INSTALL_DIR" "$SHELL_RC" 2>/dev/null; then
        echo "" >> "$SHELL_RC"
        echo "# Calculator command" >> "$SHELL_RC"
        echo "export PATH=\"$INSTALL_DIR:\$PATH\"" >> "$SHELL_RC"
        echo "  Added $INSTALL_DIR to PATH in $SHELL_RC"
        echo "  Please restart your terminal or run: source $SHELL_RC"
    fi
fi

echo ""
echo "  Installation successful!"
echo ""
echo "  Run 'calculator' to start!"
echo ""
echo "  To uninstall, run:  bash install.sh --uninstall"

if [ "$CLEANUP_TEMP" -eq 1 ]; then
    rm -rf "$TEMP_DIR"
fi