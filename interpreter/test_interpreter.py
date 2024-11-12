import unittest
from interpreter import (
    Lexer, Parser, Interpreter, ParsingError, InterpreterError)


class TestInterpreter(unittest.TestCase):

    def test_addition(self):
        expr = "2 + 3"
        lexer = Lexer(expr)
        parser = Parser(lexer)
        interpreter = Interpreter(parser)
        self.assertEqual(interpreter.interpret(), 5)

    def test_subtraction(self):
        expr = "10 - 4"
        lexer = Lexer(expr)
        parser = Parser(lexer)
        interpreter = Interpreter(parser)
        self.assertEqual(interpreter.interpret(), 6)

    def test_multiplication(self):
        expr = "6 * 7"
        lexer = Lexer(expr)
        parser = Parser(lexer)
        interpreter = Interpreter(parser)
        self.assertEqual(interpreter.interpret(), 42)

    def test_division(self):
        expr = "20 / 4"
        lexer = Lexer(expr)
        parser = Parser(lexer)
        interpreter = Interpreter(parser)
        self.assertEqual(interpreter.interpret(), 5.0)

    def test_combined_operations(self):
        expr = "(2 + 3) * 4"
        lexer = Lexer(expr)
        parser = Parser(lexer)
        interpreter = Interpreter(parser)
        self.assertEqual(interpreter.interpret(), 20)

    def test_parentheses_precedence(self):
        expr = "2 + (3 * 4)"
        lexer = Lexer(expr)
        parser = Parser(lexer)
        interpreter = Interpreter(parser)
        self.assertEqual(interpreter.interpret(), 14)  # 2 + (3 * 4) = 14

    def test_nested_parentheses(self):
        expr = "(2 + 3) * (4 + 5)"
        lexer = Lexer(expr)
        parser = Parser(lexer)
        interpreter = Interpreter(parser)
        # (2 + 3) * (4 + 5) = 5 * 9 = 45
        self.assertEqual(interpreter.interpret(), 45)

    def test_complex_operations_with_parentheses(self):
        expr = "(6 + 2) * (5 - 3)"
        lexer = Lexer(expr)
        parser = Parser(lexer)
        interpreter = Interpreter(parser)
        # (6 + 2) * (5 - 3) = 8 * 2 = 16
        self.assertEqual(interpreter.interpret(), 16)

    def test_parentheses_with_subtraction_and_addition(self):
        expr = "(10 - 2) + (5 + 3)"
        lexer = Lexer(expr)
        parser = Parser(lexer)
        interpreter = Interpreter(parser)
        # (10 - 2) + (5 + 3) = 8 + 8 = 16
        self.assertEqual(interpreter.interpret(), 16)

    def test_division_with_parentheses(self):
        expr = "(6 + 2) / (5 - 3)"
        lexer = Lexer(expr)
        parser = Parser(lexer)
        interpreter = Interpreter(parser)
        # (6 + 2) / (5 - 3) = 8 / 2 = 4.0
        self.assertEqual(interpreter.interpret(), 4.0)

    def test_divide_by_zero_with_parentheses(self):
        expr = "(5 + 5) / (3 - 3)"
        lexer = Lexer(expr)
        parser = Parser(lexer)
        interpreter = Interpreter(parser)
        with self.assertRaises(InterpreterError):
            interpreter.interpret()

    def test_invalid_syntax_in_parentheses(self):
        expr = "(2 + 3 * 5"
        lexer = Lexer(expr)
        parser = Parser(lexer)
        interpreter = Interpreter(parser)
        with self.assertRaises(ParsingError):
            interpreter.interpret()

    def test_unexpected_parentheses(self):
        expr = "((2 + 3) * 4"
        lexer = Lexer(expr)
        parser = Parser(lexer)
        interpreter = Interpreter(parser)
        with self.assertRaises(ParsingError):
            interpreter.interpret()

    def test_complex_expression(self):
        expr = "(2 + (9/3)) * (4 - 5 + (3*3))"
        lexer = Lexer(expr)
        parser = Parser(lexer)
        interpreter = Interpreter(parser)
        # (2 + (9/3)) * (4 - 5 + (3*3)) = 5 * 8 = 40.0
        self.assertEqual(interpreter.interpret(), 40.0)


if __name__ == '__main__':
    unittest.main()
