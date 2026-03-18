# calculator/pkg/calculator.py

import math

class Calculator:
    def __init__(self):
        self.operators = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: a / b,
            "^": lambda a, b: a ** b,
        }
        self.precedence = {
            "+": 1,
            "-": 1,
            "*": 2,
            "/": 2,
            "^": 3,  # Higher precedence for exponentiation
        }
        self.right_associative = {
            "^": True
        }

    def evaluate(self, expression):
        if not expression or expression.isspace():
            return None
        tokens = expression.strip().split()
        return self._evaluate_infix(tokens)

    def _evaluate_infix(self, tokens):
        values = []
        operators = []

        i = 0
        while i < len(tokens):
            token = tokens[i]
            if token == "(":
                operators.append(token)
            elif token == ")":
                while operators and operators[-1] != "(":
                    self._apply_operator(operators, values)
                if operators and operators[-1] == "(":
                    operators.pop() # Pop the "("
                else:
                    raise ValueError("Mismatched parentheses")
            elif token == "sqrt":
                # Handle sqrt function
                if i + 1 < len(tokens) and tokens[i+1] == "(":
                    # Find the matching closing parenthesis
                    paren_count = 1
                    j = i + 2
                    start_expr_idx = j
                    while j < len(tokens) and paren_count != 0:
                        if tokens[j] == "(":
                            paren_count += 1
                        elif tokens[j] == ")":
                            paren_count -= 1
                        j += 1
                    if paren_count != 0:
                        raise ValueError("Mismatched parentheses in sqrt function")

                    sub_expression_tokens = tokens[start_expr_idx : j-1]
                    sub_expression_result = self._evaluate_infix(sub_expression_tokens)
                    values.append(math.sqrt(sub_expression_result))
                    i = j - 1 # Move cursor past the sqrt expression
                else:
                    raise ValueError("sqrt function requires an argument in parentheses")

            elif token in self.operators:
                while (
                    operators
                    and operators[-1] != "("
                    and (
                        self.precedence.get(operators[-1], 0) > self.precedence[token]
                        or (self.precedence.get(operators[-1], 0) == self.precedence[token] and not self.right_associative.get(token, False))
                    )
                ):
                    self._apply_operator(operators, values)
                operators.append(token)
            else:
                try:
                    values.append(float(token))
                except ValueError:
                    raise ValueError(f"invalid token: {token}")
            i += 1

        while operators:
            if operators[-1] == "(":
                raise ValueError("Mismatched parentheses")
            self._apply_operator(operators, values)

        if len(values) != 1:
            raise ValueError("invalid expression")

        return values[0]

    def _apply_operator(self, operators, values):
        if not operators:
            return

        operator = operators.pop()
        if len(values) < 2:
            raise ValueError(f"not enough operands for operator {operator}")

        b = values.pop()
        a = values.pop()
        values.append(self.operators[operator](a, b))
