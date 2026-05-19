CC = gcc
CFLAGS = -Wall -Wextra -O2 -std=c99
LDFLAGS = -lm

SRC_DIR = src
BUILD_DIR = build
BIN_DIR = build

SOURCES = $(SRC_DIR)/main.c $(SRC_DIR)/calculator.c $(SRC_DIR)/operations.c
OBJECTS = $(SOURCES:$(SRC_DIR)/%.c=$(BUILD_DIR)/%.o)
TARGET = $(BIN_DIR)/calculator

PREFIX ?= /usr/local
INSTALL_BIN = $(PREFIX)/bin

.PHONY: all clean install uninstall test

all: $(TARGET)

$(TARGET): $(OBJECTS)
	@mkdir -p $(BIN_DIR)
	$(CC) $(CFLAGS) -o $@ $^ $(LDFLAGS)
	@echo "Build complete: $(TARGET)"

$(BUILD_DIR)/%.o: $(SRC_DIR)/%.c
	@mkdir -p $(BUILD_DIR)
	$(CC) $(CFLAGS) -c -o $@ $<

clean:
	rm -rf $(BUILD_DIR)
	@echo "Clean complete"

install: $(TARGET)
	@mkdir -p $(INSTALL_BIN)
	cp $(TARGET) $(INSTALL_BIN)/calculator
	chmod 755 $(INSTALL_BIN)/calculator
	@echo "Installed to $(INSTALL_BIN)/calculator"

uninstall:
	rm -f $(INSTALL_BIN)/calculator
	@echo "Uninstalled"

test: $(TARGET)
	@echo "Running tests..."
	@echo "Test 1: 10 + 5"
	@echo "10 + 5" | $(TARGET)
	@echo ""
	@echo "Test 2: sqrt 16"
	@echo "sqrt 16" | $(TARGET)
	@echo ""
	@echo "Test 3: sigmoid 0"
	@echo "sigmoid 0" | $(TARGET)
	@echo ""
	@echo "All tests complete!"

help:
	@echo "Calculator Makefile"
	@echo ""
	@echo "Targets:"
	@echo "  all      - Build the calculator (default)"
	@echo "  clean    - Remove build files"
	@echo "  install  - Install to $(PREFIX)/bin (requires sudo)"
	@echo "  uninstall - Remove installed calculator"
	@echo "  test     - Run basic tests"
	@echo "  help     - Show this help"
	@echo ""
	@echo "Variables:"
	@echo "  PREFIX   - Installation prefix (default: /usr/local)"
	@echo "            Use PREFIX=~/.local for user installation"