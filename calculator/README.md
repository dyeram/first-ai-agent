# Calculator

A simple Python command-line calculator that evaluates arithmetic expressions.

## Features

- Basic arithmetic: `+`, `-`, `*`, `/`
- Exponentiation using `^`
- Square root using `sqrt(...)`
- Supports parentheses and operator precedence
- Expressions can be written with or without spaces

## Run

```bash
uv run main.py "<expression>"
```

Example:

```bash
uv run main.py "2*sqrt(9)+3^2"
```

The expression must be provided as a quoted string so it is passed as a single argument to the program.
