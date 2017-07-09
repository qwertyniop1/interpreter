INTEGER = 'INTEGER'
PLUS = 'PLUS'
EOF = 'EOF'

class Token(object):
    def __init__(self, token_type, value):
        self.token_type = token_type
        self.value = value

    def __str__(self):
        return 'Token <{}>: "{}"'.format(self.token_type, self.value)

    def __repr__(self):
        return self.__str__()


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
        return self.expression()

    def error(self):
        raise SyntaxError('Invalid syntax at position {}'.format(self.position))

    def parse_token(self, token):
        raise NotImplementedError('Cannot execute method of base interpreter class')

    def expression(self):
        raise NotImplementedError('Cannot execute method of base interpreter class')


class SimpleInterpreter(Interpreter):
    def parse_token(self, token):
        if token.isdigit():
            return Token(INTEGER, token)
        if token == '+':
            return Token(PLUS, token)

    def expression(self):
        left = self.get(INTEGER)
        operator = self.get(PLUS)
        right = self.get(INTEGER)

        return int(left.value) + int(right.value)


if __name__ == '__main__':
    import traceback

    index = 1

    while True:
        try:
            expression = raw_input('[{}]> '.format(index))
        except EOFError:
            break

        if not expression:
            continue

        try:
            result = SimpleInterpreter(expression).parse()
            print result
        except SyntaxError:
            print traceback.format_exc()

        index += 1
