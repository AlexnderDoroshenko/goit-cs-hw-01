"""Tokenizer module"""


class TokenType:
    """
    Додайте нові типи токенів для операцій множення MUL,
    ділення DIV та дужок, які відкривають LPAREN
    та закривають RPAREN частину арифметичного виразу.
    """
    INTEGER = "INTEGER"
    MUL = "MULTIPLY"
    DIV = "DIVIDE"
    PLUS = "PLUS"
    MINUS = "MINUS"
    LPAREN = "("
    RPAREN = ")"
    EOF = "EOF"  # Означає кінець вхідного рядка


class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __str__(self):
        return f"Token({self.type}, {repr(self.value)})"
