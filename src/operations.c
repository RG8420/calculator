#include "calculator.h"

double add(double a, double b) {
    return a + b;
}

double subtract(double a, double b) {
    return a - b;
}

double multiply(double a, double b) {
    return a * b;
}

double divide(double a, double b) {
    if (b == 0) {
        fprintf(stderr, "Error: Division by zero\n");
        return 0;
    }
    return a / b;
}

double power(double a, double b) {
    return pow(a, b);
}

double modulo(double a, double b) {
    if (b == 0) {
        fprintf(stderr, "Error: Modulo by zero\n");
        return 0;
    }
    return fmod(a, b);
}

double floor_divide(double a, double b) {
    if (b == 0) {
        fprintf(stderr, "Error: Floor division by zero\n");
        return 0;
    }
    return floor(a / b);
}

double maximum(double a, double b) {
    return (a > b) ? a : b;
}

double minimum(double a, double b) {
    return (a < b) ? a : b;
}

double square(double a) {
    return a * a;
}

double cube(double a) {
    return a * a * a;
}

double negate(double a) {
    return -a;
}

double absolute(double a) {
    return fabs(a);
}

double square_root(double a) {
    if (a < 0) {
        fprintf(stderr, "Error: Cannot take square root of negative number\n");
        return 0;
    }
    return sqrt(a);
}

double logarithm(double a) {
    if (a <= 0) {
        fprintf(stderr, "Error: Cannot take logarithm of non-positive number\n");
        return 0;
    }
    return log(a);
}

double exponential(double a) {
    return exp(a);
}

double sine(double a) {
    return sin(a);
}

double cosine(double a) {
    return cos(a);
}

double tangent(double a) {
    double c = cos(a);
    if (c == 0) {
        fprintf(stderr, "Error: Tangent undefined at this angle\n");
        return 0;
    }
    return tan(a);
}

double hyperbolic_tangent(double a) {
    return tanh(a);
}

double relu(double a) {
    return (a > 0) ? a : 0;
}

double sigmoid(double a) {
    return 1.0 / (1.0 + exp(-a));
}

int is_integer(double value) {
    return value == floor(value);
}

char *format_result(double value, char *buffer, size_t size) {
    if (is_integer(value) && fabs(value) < 1e15) {
        snprintf(buffer, size, "%.0f", value);
    } else {
        snprintf(buffer, size, "%.10g", value);
    }
    return buffer;
}