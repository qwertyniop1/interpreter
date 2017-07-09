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
            result = Token(tokens.INTEGER, self.integer())
        else:
            if token == '+':
                result = Token(tokens.PLUS, token)
            if token == '-':
                result = Token(tokens.MINUS, token)
            if token == '*':
                result = Token(tokens.ASTERIX, token)
            if token == '/':
                result = Token(tokens.SLASH, token)
            if token == '(':
                result = Token(tokens.OPEN_BRACKET, token)
            if token == ')':
                result = Token(tokens.CLOSE_BRACKET, token)

        self.next_char()
        return result
