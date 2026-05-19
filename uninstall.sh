#!/usr/bin/env bash
# uninstall.sh
# Removes the 'calculator' command from your system.
#
# Usage:
#   bash uninstall.sh

set -euo pipefail

INSTALL_DIR="$HOME/.local/bin"
SYSTEM_INSTALL_DIR="/usr/local/bin"
VENV_DIR="$HOME/.calculator-venv"

echo "=== Calculator Uninstaller ==="

targets=("$SYSTEM_INSTALL_DIR/calculator" "$INSTALL_DIR/calculator")
removed=0

for target in "${targets[@]}"; do
    if [ -f "$target" ]; then
        rm "$target"
        echo "  Removed $target"
        removed=1
    fi
done

if [ -d "$VENV_DIR" ]; then
    rm -rf "$VENV_DIR"
    echo "  Removed virtual environment"
    removed=1
fi

if [ $removed -eq 1 ]; then
    echo ""
    echo "  Uninstall complete."
else
    echo "  Calculator not found - nothing to remove."
fi