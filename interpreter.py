from interpreter import Interpreter, Token

INTEGER = 'INTEGER'
PLUS = 'PLUS'
MINUS = 'MINUS'

class SimpleInterpreter(Interpreter):
    def parse_token(self, token):
        if token.isdigit():
            return Token(INTEGER, token)
        if token == '+':
            return Token(PLUS, token)
        if token == '-':
            return Token(MINUS, token)

    def expression(self):
        left = int(self.get(INTEGER).value)
        operator = self.pick()
        if operator.token_type == PLUS:
            operator = self.get(PLUS)
        else:
            operator = self.get(MINUS)
        right = int(self.get(INTEGER).value)

        if operator.token_type == PLUS:
            result = left + right
        elif operator.token_type == MINUS:
            result = left - right

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
