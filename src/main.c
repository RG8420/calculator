#define _POSIX_C_SOURCE 200809L

#include "calculator.h"
#include <ctype.h>
#include <time.h>
#include <unistd.h>

#define HELP_TEXT \
"╔══════════════════════════════════════╗\n" \
"║         CALCULATOR HELP              ║\n" \
"╠══════════════════════════════════════╣\n" \
"║  Binary Operations:                  ║\n" \
"║    +        Add                     ║\n" \
"║    -        Subtract                 ║\n" \
"║    *        Multiply                 ║\n" \
"║    /        Divide                   ║\n" \
"║    %        Modulo                   ║\n" \
"║    ^        Power                    ║\n" \
"║    //       Floor divide             ║\n" \
"║    max      Maximum                  ║\n" \
"║    min      Minimum                  ║\n" \
"║                                      ║\n" \
"║  Unary Operations:                   ║\n" \
"║    square   Square                  ║\n" \
"║    cube     Cube                    ║\n" \
"║    sqrt     Square root             ║\n" \
"║    neg      Negate                   ║\n" \
"║    abs      Absolute                 ║\n" \
"║    log      Natural log              ║\n" \
"║    exp      Exponential             ║\n" \
"║    sin      Sine (radians)           ║\n" \
"║    cos      Cosine                   ║\n" \
"║    tan      Tangent                  ║\n" \
"║    tanh     Hyperbolic tan           ║\n" \
"║    relu     ReLU activation          ║\n" \
"║    sigmoid  Sigmoid activation       ║\n" \
"║                                      ║\n" \
"║  Commands:                           ║\n" \
"║    help     Show this message        ║\n" \
"║    quit     Exit calculator         ║\n" \
"║    clear   Clear display             ║\n" \
"╚══════════════════════════════════════╝\n"

void print_help() {
    printf("%s", HELP_TEXT);
}

int is_unary_op(const char *op) {
    return strcmp(op, "square") == 0 || strcmp(op, "sqrt") == 0 ||
           strcmp(op, "cube") == 0 || strcmp(op, "neg") == 0 ||
           strcmp(op, "abs") == 0 || strcmp(op, "log") == 0 ||
           strcmp(op, "exp") == 0 || strcmp(op, "sin") == 0 ||
           strcmp(op, "cos") == 0 || strcmp(op, "tan") == 0 ||
           strcmp(op, "tanh") == 0 || strcmp(op, "relu") == 0 ||
           strcmp(op, "sigmoid") == 0 || strcmp(op, "max") == 0 ||
           strcmp(op, "min") == 0;
}

int is_binary_op(const char *op) {
    return strcmp(op, "+") == 0 || strcmp(op, "-") == 0 ||
           strcmp(op, "*") == 0 || strcmp(op, "/") == 0 ||
           strcmp(op, "%") == 0 || strcmp(op, "^") == 0 ||
           strcmp(op, "//") == 0 || strcmp(op, "max") == 0 ||
           strcmp(op, "min") == 0;
}

void process_line(Calculator *calc, char *line) {
    char *line_copy = strdup(line);
    char *token;
    char *tokens[4];
    int token_count = 0;

    token = strtok(line_copy, " \t\n");
    while (token != NULL && token_count < 4) {
        tokens[token_count++] = token;
        token = strtok(NULL, " \t\n");
    }

    if (token_count == 0) {
        free(line_copy);
        return;
    }

    if (strcmp(tokens[0], "quit") == 0 || strcmp(tokens[0], "exit") == 0) {
        free(line_copy);
        printf("Goodbye!\n");
        exit(0);
    }

    if (strcmp(tokens[0], "help") == 0) {
        print_help();
        free(line_copy);
        return;
    }

    if (strcmp(tokens[0], "clear") == 0 || strcmp(tokens[0], "c") == 0) {
        calc_clear(calc);
        printf("  = %s\n", calc_get_display(calc));
        free(line_copy);
        return;
    }

    if (token_count == 1) {
        if (strlen(tokens[0]) == 1 && isdigit(tokens[0][0])) {
            calc_input_digit(calc, tokens[0][0]);
            printf("  = %s\n", calc_get_display(calc));
        } else if (strcmp(tokens[0], ".") == 0) {
            calc_input_decimal(calc);
            printf("  = %s\n", calc_get_display(calc));
        } else {
            printf("  Usage: <num> <op> <num>  or  <op> <num>\n");
        }
        free(line_copy);
        return;
    }

    if (token_count == 2) {
        if (is_unary_op(tokens[0])) {
            calc->display[0] = '0';
            calc->display[1] = '\0';
            strncpy(calc->display, tokens[1], MAX_DISPLAY_LEN - 1);
            calc->display[MAX_DISPLAY_LEN - 1] = '\0';
            calc_apply_unary(calc, tokens[0]);
            printf("  = %s\n", calc_get_display(calc));
        } else {
            printf("  Unknown operation '%s'. Type 'help' for options.\n", tokens[0]);
        }
        free(line_copy);
        return;
    }

    if (token_count == 3) {
        calc_clear(calc);
        strncpy(calc->display, tokens[0], MAX_DISPLAY_LEN - 1);
        calc->display[MAX_DISPLAY_LEN - 1] = '\0';
        calc_set_operator(calc, tokens[1]);
        strncpy(calc->display, tokens[2], MAX_DISPLAY_LEN - 1);
        calc->display[MAX_DISPLAY_LEN - 1] = '\0';
        calc_calculate(calc);
        printf("  = %s\n", calc_get_display(calc));
        free(line_copy);
        return;
    }

    printf("  Usage: <num> <op> <num>  or  <op> <num>\n");
    free(line_copy);
}

int main() {
    Calculator calc;
    calc_init(&calc);

    printf("=== Calculator (C) ===\n");
    printf("Type 'help' for operations, 'quit' to exit.\n\n");

    char *line = NULL;
    size_t len = 0;
    ssize_t read;

    while (1) {
        printf("> ");
        fflush(stdout);

        read = getline(&line, &len, stdin);
        if (read == -1) {
            printf("\nGoodbye!\n");
            break;
        }

        size_t line_len = strlen(line);
        while (line_len > 0 && (line[line_len - 1] == '\n' || line[line_len - 1] == '\r')) {
            line[--line_len] = '\0';
        }

        if (line_len == 0) continue;

        process_line(&calc, line);
    }

    free(line);
    return 0;
}