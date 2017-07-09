from interpreter import Interpreter, Token

INTEGER = 'INTEGER'
PLUS = 'PLUS'

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
