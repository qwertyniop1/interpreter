from interpreters.core import Lexer, Token
from interpreters.arithmetic import tokens


class ArithmeticLexer(Lexer):
    def integer(self):
        result = []

        while self.current_char is not None and self.current_char.isdigit():
            result.append(self.current_char)
            self.next_char()

        return int(''.join(result))


    def parse_char(self, token):
        if token.isdigit():
            return Token(tokens.INTEGER, self.integer())
        if token == '+':
            self.next_char()
            return Token(tokens.PLUS, token)
        if token == '-':
            self.next_char()
            return Token(tokens.MINUS, token)
        if token == '*':
            self.next_char()
            return Token(tokens.ASTERIX, token)
        if token == '/':
            self.next_char()
            return Token(tokens.SLASH, token)
        if token == '(':
            self.next_char()
            return Token(tokens.OPEN_BRACKET, token)
        if token == ')':
            self.next_char()
            return Token(tokens.CLOSE_BRACKET, token)
