from interpreters.core import Token, EOF
from interpreters.core.exceptions import BaseInterpreterError


class LexicalAnalizeError(BaseInterpreterError):
    pass


class Lexer(object):
    def __init__(self, expression):
        self._expression = expression
        self.position = 0
        self.current_char = self._expression[self.position]


    def next_char(self):
        self.position += 1
        if self.position >= len(self._expression):
            self.current_char = None
        else:
            self.current_char = self._expression[self.position]


    def next_token(self):
        while self.current_char is not None:
            if self.current_char.isspace():
                self.next_char()
                continue

            parsed_token = self.parse_char(self.current_char)
            if parsed_token:
                return parsed_token

            self.error()

        return Token(EOF, None)


    def error(self):
        raise LexicalAnalizeError(self._expression, self.position)


    def parse_char(self, token):
        raise NotImplementedError('Cannot execute method of base interpreter class')
