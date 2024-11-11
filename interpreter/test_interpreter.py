import unittest
from interpreter import (
    Interpreter, Lexer, LexicalError, Parser)


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

    def test_divide_by_zero(self):
        expr = "5 / 0"
        lexer = Lexer(expr)
        parser = Parser(lexer)
        interpreter = Interpreter(parser)
        with self.assertRaises(ZeroDivisionError):
            interpreter.interpret()

    def test_unknown_operation(self):
        expr = "2 ^ 3"
        lexer = Lexer(expr)
        parser = Parser(lexer)
        interpreter = Interpreter(parser)
        with self.assertRaises(LexicalError):
            interpreter.interpret()


if __name__ == '__main__':
    unittest.main()
