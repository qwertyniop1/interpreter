from interpreter import Token, EOF


class Interpreter(object):
    def __init__(self, expression):
        self._expression = expression
        self.position = 0
        self.current_token = None
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


    def get(self, token_type):
        self.current_token = self.next_token()

        if self.current_token.token_type == token_type:
            return self.current_token

        self.error()


    def pick(self):
        previous_position = self.position
        previous_char = self.current_char

        self.current_token = self.next_token()

        self.position = previous_position
        self.current_char = previous_char
        return self.current_token


    def parse(self):
        try:
            return self.expression()
        except SyntaxError as error:
            raise
            # raise SyntaxError(error)


    def error(self):
        raise SyntaxError('Invalid syntax at position {}'.format(self.position))


    def parse_char(self, token):
        raise NotImplementedError('Cannot execute method of base interpreter class')


    def expression(self):
        raise NotImplementedError('Cannot execute method of base interpreter class')
