from interpreter import Token, EOF


class Interpreter(object):
    def __init__(self, expression):
        self._expression = expression
        self.position = 0
        self.current_token = None


    def next_token(self):
        if self.position >= len(self._expression):
            return Token(EOF, None)

        token = self._expression[self.position]

        parsed_token = self.parse_token(token)
        if parsed_token:
            self.position += 1
            return parsed_token

        self.error()


    def get(self, token_type):
        self.current_token = self.next_token()

        if self.current_token.token_type == token_type:
            return self.current_token

        self.error()


    def parse(self):
        try:
            return self.expression()
        except SyntaxError as error:
            raise SyntaxError(error)


    def error(self):
        raise SyntaxError('Invalid syntax at position {}'.format(self.position))


    def parse_token(self, token):
        raise NotImplementedError('Cannot execute method of base interpreter class')


    def expression(self):
        raise NotImplementedError('Cannot execute method of base interpreter class')
