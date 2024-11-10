"""Parser module"""
from lexer import Lexer
from tokenizer import TokenType


class ParsingError(Exception):
    pass


class AST:
    pass


class BinOp(AST):
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right


class Num(AST):
    def __init__(self, token):
        self.token = token
        self.value = token.value


class Parser:
    def __init__(self, lexer):
        self.lexer = lexer
        self.current_token = self.lexer.get_next_token()

    def error(self):
        raise ParsingError("Помилка синтаксичного аналізу")

    def eat(self, token_type):
        """
        Порівнюємо поточний токен з очікуваним токеном і, якщо вони збігаються,
        'поглинаємо' його і переходимо до наступного токена.
        """
        if self.current_token.type == token_type:
            self.current_token = self.lexer.get_next_token()
        else:
            print(f"Cur tok type: {
                self.current_token.type}, tok type: {token_type}")
            self.error()

    def term(self):
        """
        Парсер для 'term' правил граматики. У нашому випадку - це цілі числа.
        """
        token = self.current_token
        self.eat(TokenType.INTEGER)
        return Num(token)

    def expr(self):
        """Парсер для арифметичних виразів."""
        node = self.factor()
        exp_token_types = (
            TokenType.PLUS, TokenType.MINUS,
            TokenType.MUL, TokenType.DIV,
        )
        while self.current_token.type in exp_token_types:
            token = self.current_token
            if token.type == TokenType.PLUS:
                self.eat(TokenType.PLUS)
            elif token.type == TokenType.MINUS:
                self.eat(TokenType.MINUS)
            elif token.type == TokenType.MUL:
                self.eat(TokenType.MUL)
            elif token.type == TokenType.DIV:
                self.eat(TokenType.DIV)
            node = BinOp(left=node, op=token, right=self.factor())
        return node

    def factor(self):
        """Метод для обробки чисел та виразів у дужках"""
        token = self.current_token
        if token.type == TokenType.INTEGER:
            return self.term()
        elif token.type == TokenType.LPAREN:
            self.eat(TokenType.LPAREN)
            node = self.expr()
            self.eat(TokenType.RPAREN)
            return node
        raise ParsingError(f"Unknown Token type {token.type}")


def print_ast(node, level=0):
    indent = "  " * level
    if isinstance(node, Num):
        print(f"{indent}Num({node.value})")
    elif isinstance(node, BinOp):
        print(f"{indent}BinOp:")
        print(f"{indent}  left: ")
        print_ast(node.left, level + 2)
        print(f"{indent}  op: {node.op.type}")
        print(f"{indent}  right: ")
        print_ast(node.right, level + 2)
    else:
        print(f"{indent}Unknown node type: {type(node)}")


def main():
    while True:
        try:
            text = input('Введіть вираз (або "exit" для виходу): ')
            if text.lower() == "exit":
                print("Вихід із програми.")
                break
            lexer = Lexer(text)
            parser = Parser(lexer)
            tree = parser.expr()
            print_ast(tree)
        except Exception as e:
            print(e)


if __name__ == "__main__":
    main()
