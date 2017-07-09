from interpreter import Token, EOF


class Interpreter(object):
    def __init__(self, lexer):
        self.lexer = lexer
        self.current_token = None

    def get(self, token_type):
        self.current_token = self.lexer.next_token()

        if self.current_token.token_type == token_type:
            return self.current_token

        self.error()


    def pick(self):
        previous_position = self.lexer.position
        previous_char = self.lexer.current_char

        self.current_token = self.lexer.next_token()

        self.lexer.position = previous_position
        self.lexer.current_char = previous_char
        return self.current_token


    def parse(self):
        try:
            return self.expression()
        except SyntaxError as error:
            raise
            # raise SyntaxError(error)


    def error(self):
        raise SyntaxError('Invalid syntax at position {}'.format(self.lexer.position))


    def expression(self):
        raise NotImplementedError('Cannot execute method of base interpreter class')
