from interpreter import Interpreter, Token

INTEGER = 'INTEGER'
PLUS = 'PLUS'
MINUS = 'MINUS'
ASTERIX = 'ASTERIX'
SLASH = 'SLASH'


class SimpleInterpreter(Interpreter):
    def integer(self):
        result = []

        while self.current_char is not None and self.current_char.isdigit():
            result.append(self.current_char)
            self.next_char()

        return int(''.join(result))


    def parse_char(self, token):
        if token.isdigit():
            return Token(INTEGER, self.integer())
        if token == '+':
            self.next_char()
            return Token(PLUS, token)
        if token == '-':
            self.next_char()
            return Token(MINUS, token)
        if token == '*':
            self.next_char()
            return Token(ASTERIX, token)
        if token == '/':
            self.next_char()
            return Token(SLASH, token)


    def expression(self):
        left = int(self.get(INTEGER).value)
        operator = self.pick()
        if operator.token_type in [PLUS, MINUS, ASTERIX]:
            operator = self.get(operator.token_type)
        else:
            operator = self.get(SLASH)
        right = int(self.get(INTEGER).value)

        if operator.token_type == PLUS:
            result = left + right
        elif operator.token_type == MINUS:
            result = left - right
        elif operator.token_type == ASTERIX:
            result = left * right
        elif operator.token_type == SLASH:
            result = left / right

        return result


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
