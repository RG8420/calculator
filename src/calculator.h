#ifndef CALCULATOR_H
#define CALCULATOR_H

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

#define MAX_DISPLAY_LEN 64
#define MAX_INPUT_LEN 256

typedef struct {
    char display[MAX_DISPLAY_LEN];
    double first_operand;
    char operator[8];
    int waiting_for_second;
    char error_message[MAX_INPUT_LEN];
} Calculator;

void calc_init(Calculator *calc);
void calc_clear(Calculator *calc);
void calc_input_digit(Calculator *calc, char digit);
void calc_input_decimal(Calculator *calc);
void calc_set_operator(Calculator *calc, const char *op);
void calc_calculate(Calculator *calc);
void calc_apply_unary(Calculator *calc, const char *op);
const char *calc_get_display(Calculator *calc);
const char *calc_get_error(Calculator *calc);

double add(double a, double b);
double subtract(double a, double b);
double multiply(double a, double b);
double divide(double a, double b);
double power(double a, double b);
double modulo(double a, double b);
double floor_divide(double a, double b);
double maximum(double a, double b);
double minimum(double a, double b);

double square(double a);
double cube(double a);
double negate(double a);
double absolute(double a);
double square_root(double a);
double logarithm(double a);
double exponential(double a);
double sine(double a);
double cosine(double a);
double tangent(double a);
double hyperbolic_tangent(double a);
double relu(double a);
double sigmoid(double a);

int is_integer(double value);
char *format_result(double value, char *buffer, size_t size);

#endif