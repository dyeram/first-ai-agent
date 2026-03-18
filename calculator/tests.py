# calculator/tests.py

import unittest
from pkg.calculator import Calculator


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_addition(self):
        result = self.calculator.evaluate("3 + 5")
        self.assertEqual(result, 8)

    def test_subtraction(self):
        result = self.calculator.evaluate("10 - 4")
        self.assertEqual(result, 6)

    def test_multiplication(self):
        result = self.calculator.evaluate("3 * 4")
        self.assertEqual(result, 12)

    def test_division(self):
        result = self.calculator.evaluate("10 / 2")
        self.assertEqual(result, 5)

    def test_nested_expression(self):
        result = self.calculator.evaluate("3 * 4 + 5")
        self.assertEqual(result, 17)

    def test_complex_expression(self):
        result = self.calculator.evaluate("2 * 3 - 8 / 2 + 5")
        self.assertEqual(result, 7)

    def test_empty_expression(self):
        result = self.calculator.evaluate("")
        self.assertIsNone(result)

    def test_invalid_operator(self):
        with self.assertRaises(ValueError):
            self.calculator.evaluate("$ 3 5")

    def test_not_enough_operands(self):
        with self.assertRaises(ValueError):
            self.calculator.evaluate("+ 3")

    def test_exponentiation_basic(self):
        result = self.calculator.evaluate("2 ^ 3")
        self.assertEqual(result, 8)

    def test_exponentiation_precedence(self):
        result = self.calculator.evaluate("2 * 3 ^ 2")
        self.assertEqual(result, 18)

    def test_sqrt_basic(self):
        result = self.calculator.evaluate("sqrt(9)")
        self.assertEqual(result, 3)

    def test_sqrt_expression(self):
        result = self.calculator.evaluate("sqrt(4 + 5)")
        self.assertEqual(result, 3)

    def test_mixed_expression_with_power_and_sqrt(self):
        result = self.calculator.evaluate("2 * sqrt(9) + 3 ^ 2")
        self.assertEqual(result, 15) # 2 * 3 + 9 = 6 + 9 = 15

    def test_exponentiation_associativity(self):
        # (2 ^ 3) ^ 2 = 8 ^ 2 = 64
        # 2 ^ (3 ^ 2) = 2 ^ 9 = 512
        # Exponentiation is right-associative, so 2 ^ 3 ^ 2 should be 2 ^ (3 ^ 2)
        result = self.calculator.evaluate("2 ^ 3 ^ 2")
        self.assertEqual(result, 512)

    def test_parentheses_with_exponent(self):
        result = self.calculator.evaluate("(2 + 3) ^ 2")
        self.assertEqual(result, 25)

    def test_sqrt_with_nested_expressions(self):
        result = self.calculator.evaluate("sqrt(4 * (2 + 1) + 1)")
        self.assertAlmostEqual(result, 3.605551275463989)

    def test_invalid_sqrt_input_empty(self):
        with self.assertRaises(ValueError):
            self.calculator.evaluate("sqrt()")

    def test_invalid_sqrt_input_missing_parenthesis(self):
        with self.assertRaises(ValueError):
            self.calculator.evaluate("sqrt(9")

    def test_mismatched_parentheses_missing_open(self):
        with self.assertRaises(ValueError):
            self.calculator.evaluate("2 + 3)")

    def test_mismatched_parentheses_missing_close(self):
        with self.assertRaises(ValueError):
            self.calculator.evaluate("(2 + 3")

    def test_invalid_input_empty_parentheses(self):
        with self.assertRaises(ValueError):
            self.calculator.evaluate("()")

    def test_invalid_input_unsupported_character(self):
        with self.assertRaises(ValueError):
            self.calculator.evaluate("2 + @")


if __name__ == "__main__":
    unittest.main()
