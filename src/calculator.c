#include "calculator.h"

void calc_init(Calculator *calc) {
    calc->display[0] = '0';
    calc->display[1] = '\0';
    calc->first_operand = 0;
    calc->operator[0] = '\0';
    calc->waiting_for_second = 0;
    calc->error_message[0] = '\0';
}

void calc_clear(Calculator *calc) {
    calc->display[0] = '0';
    calc->display[1] = '\0';
    calc->first_operand = 0;
    calc->operator[0] = '\0';
    calc->waiting_for_second = 0;
    calc->error_message[0] = '\0';
}

void calc_input_digit(Calculator *calc, char digit) {
    if (calc->error_message[0] != '\0') {
        calc_clear(calc);
    }

    if (calc->waiting_for_second) {
        calc->display[0] = digit;
        calc->display[1] = '\0';
        calc->waiting_for_second = 0;
    } else {
        if (calc->display[0] == '0' && calc->display[1] == '\0') {
            calc->display[0] = digit;
        } else if (strlen(calc->display) < MAX_DISPLAY_LEN - 1) {
            size_t len = strlen(calc->display);
            calc->display[len] = digit;
            calc->display[len + 1] = '\0';
        }
    }
}

void calc_input_decimal(Calculator *calc) {
    if (calc->error_message[0] != '\0') {
        calc_clear(calc);
        calc->display[0] = '0';
        calc->display[1] = '.';
        calc->display[2] = '\0';
        return;
    }

    if (calc->waiting_for_second) {
        calc->display[0] = '0';
        calc->display[1] = '.';
        calc->display[2] = '\0';
        calc->waiting_for_second = 0;
        return;
    }

    if (strchr(calc->display, '.') == NULL) {
        size_t len = strlen(calc->display);
        calc->display[len] = '.';
        calc->display[len + 1] = '\0';
    }
}

void calc_set_operator(Calculator *calc, const char *op) {
    if (calc->error_message[0] != '\0') {
        calc_clear(calc);
    }

    double current = atof(calc->display);

    if (calc->first_operand == 0 && calc->operator[0] == '\0') {
        calc->first_operand = current;
    } else if (!calc->waiting_for_second && calc->operator[0] != '\0') {
        calc_calculate(calc);
        calc->first_operand = atof(calc->display);
    }

    strncpy(calc->operator, op, 7);
    calc->operator[7] = '\0';
    calc->waiting_for_second = 1;
}

static double apply_binary_op(double a, const char *op, double b) {
    if (strcmp(op, "+") == 0) return add(a, b);
    if (strcmp(op, "-") == 0) return subtract(a, b);
    if (strcmp(op, "*") == 0) return multiply(a, b);
    if (strcmp(op, "/") == 0) return divide(a, b);
    if (strcmp(op, "%") == 0) return modulo(a, b);
    if (strcmp(op, "^") == 0) return power(a, b);
    if (strcmp(op, "//") == 0) return floor_divide(a, b);
    if (strcmp(op, "max") == 0) return maximum(a, b);
    if (strcmp(op, "min") == 0) return minimum(a, b);
    return b;
}

void calc_calculate(Calculator *calc) {
    if (calc->operator[0] == '\0') return;

    double second = atof(calc->display);
    double result = apply_binary_op(calc->first_operand, calc->operator, second);

    char buf[MAX_DISPLAY_LEN];
    format_result(result, buf, MAX_DISPLAY_LEN);
    strncpy(calc->display, buf, MAX_DISPLAY_LEN - 1);
    calc->display[MAX_DISPLAY_LEN - 1] = '\0';

    calc->first_operand = result;
    calc->operator[0] = '\0';
    calc->waiting_for_second = 1;
}

void calc_apply_unary(Calculator *calc, const char *op) {
    if (calc->error_message[0] != '\0') {
        calc_clear(calc);
    }

    double value = atof(calc->display);
    double result = 0;

    if (strcmp(op, "square") == 0) result = square(value);
    else if (strcmp(op, "sqrt") == 0) result = square_root(value);
    else if (strcmp(op, "cube") == 0) result = cube(value);
    else if (strcmp(op, "neg") == 0) result = negate(value);
    else if (strcmp(op, "abs") == 0) result = absolute(value);
    else if (strcmp(op, "log") == 0) result = logarithm(value);
    else if (strcmp(op, "exp") == 0) result = exponential(value);
    else if (strcmp(op, "sin") == 0) result = sine(value);
    else if (strcmp(op, "cos") == 0) result = cosine(value);
    else if (strcmp(op, "tan") == 0) result = tangent(value);
    else if (strcmp(op, "tanh") == 0) result = hyperbolic_tangent(value);
    else if (strcmp(op, "relu") == 0) result = relu(value);
    else if (strcmp(op, "sigmoid") == 0) result = sigmoid(value);
    else if (strcmp(op, "max") == 0) result = maximum(value, 0);
    else if (strcmp(op, "min") == 0) result = minimum(value, 0);
    else return;

    char buf[MAX_DISPLAY_LEN];
    format_result(result, buf, MAX_DISPLAY_LEN);
    strncpy(calc->display, buf, MAX_DISPLAY_LEN - 1);
    calc->display[MAX_DISPLAY_LEN - 1] = '\0';

    if (calc->first_operand != 0 && !calc->waiting_for_second) {
        calc->first_operand = result;
    }
}

const char *calc_get_display(Calculator *calc) {
    if (calc->error_message[0] != '\0') {
        return calc->error_message;
    }
    return calc->display;
}

const char *calc_get_error(Calculator *calc) {
    return calc->error_message;
}