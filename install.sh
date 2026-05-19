#!/usr/bin/env bash
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
VENV_DIR="$HOME/.calculator-venv"

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
    exit 0
}

if [[ "${1:-}" == "--uninstall" ]]; then
    uninstall_calculator
fi

if [[ "${1:-}" == "-h" ]] || [[ "${1:-}" == "--help" ]]; then
    usage
fi

echo "=== Calculator Installer ==="

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

if [[ "$SCRIPT_DIR" == *"/tmp"* ]] || [[ ! -d "$SCRIPT_DIR/calculator" ]]; then
    echo "[*] Detected run from curl/download - cloning repository..."
    TEMP_DIR=$(mktemp -d)
    git clone --depth 1 "$REPO_URL" "$TEMP_DIR"
    cd "$TEMP_DIR"
    SCRIPT_DIR="$TEMP_DIR"
    CLEANUP_TEMP=1
else
    CLEANUP_TEMP=0
fi

PYTHON="$VENV_DIR/bin/python"
if [ ! -f "$PYTHON" ]; then
    echo "[1/4] Creating virtual environment..."
    python3 -m venv "$VENV_DIR"
else
    echo "[1/4] Virtual environment already exists — skipping."
fi

echo "[2/4] Installing calculator package..."
"$VENV_DIR/bin/pip" install --upgrade pip setuptools wheel --quiet 2>/dev/null || true
"$VENV_DIR/bin/pip" install -e "$SCRIPT_DIR" --quiet 2>/dev/null || true

echo "[3/4] Creating launcher script..."

if [ -w "$SYSTEM_INSTALL_DIR" ]; then
    INSTALL_TARGET="$SYSTEM_INSTALL_DIR/calculator"
    echo "  Installing to $SYSTEM_INSTALL_DIR (system-wide)"
else
    INSTALL_TARGET="$INSTALL_DIR/calculator"
    echo "  Installing to $INSTALL_DIR (user-level)"

    if [ ! -d "$INSTALL_DIR" ]; then
        mkdir -p "$INSTALL_DIR"
    fi
fi

cat > "$INSTALL_TARGET" <<EOF
#!/usr/bin/env bash
cd /tmp
exec "$PYTHON" -m calculator.repl "\$@"
EOF
chmod +x "$INSTALL_TARGET"

echo "[4/4] Configuring PATH..."

SHELL_RC="$HOME/.bashrc"
if [ -n "${ZSH_VERSION:-}" ]; then
    SHELL_RC="$HOME/.zshrc"
fi

PATH_LINE="export PATH=\"$INSTALL_DIR:\$PATH\""
if [[ "$INSTALL_TARGET" == *"$INSTALL_DIR"* ]]; then
    if ! grep -q "$INSTALL_DIR" "$SHELL_RC" 2>/dev/null; then
        echo "" >> "$SHELL_RC"
        echo "# Calculator command" >> "$SHELL_RC"
        echo "$PATH_LINE" >> "$SHELL_RC"
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