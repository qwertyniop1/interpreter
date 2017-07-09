from interpreter import Interpreter, Token, Lexer

INTEGER = 'INTEGER'
PLUS = 'PLUS'
MINUS = 'MINUS'
ASTERIX = 'ASTERIX'
SLASH = 'SLASH'
OPEN_BRACKET = 'OPEN_BRACKET'
CLOSE_BRACKET = 'CLOSE_BRACKET'


class SimpleLexer(Lexer):
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
        if token == '(':
            self.next_char()
            return Token(OPEN_BRACKET, token)
        if token == ')':
            self.next_char()
            return Token(CLOSE_BRACKET, token)


class SimpleInterpreter(Interpreter):
    def factor(self):
        if self.pick().token_type == OPEN_BRACKET:
            self.get(OPEN_BRACKET)
            result = self.expression()
            self.get(CLOSE_BRACKET)
            return result
        if self.pick().token_type == MINUS:
            self.get(MINUS)
            return -self.factor()
        return int(self.get(INTEGER).value)


    def term(self):
        result = self.factor()

        while self.pick().token_type in (ASTERIX, SLASH):
            operator = self.pick()
            if operator.token_type == ASTERIX:
                operator = self.get(ASTERIX)
            else:
                operator = self.get(SLASH)

            right = self.factor()

            if operator.token_type == ASTERIX:
                result *= right
            elif operator.token_type == SLASH:
                result /= right

        return result


    def expression(self):
        result = self.term()

        while self.pick().token_type in (PLUS, MINUS):
            operator = self.pick()
            if operator.token_type == PLUS:
                operator = self.get(PLUS)
            else:
                operator = self.get(MINUS)

            right = self.term()

            if operator.token_type == PLUS:
                result += right
            elif operator.token_type == MINUS:
                result -= right

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
            lexer = SimpleLexer(expression)
            result = SimpleInterpreter(lexer).parse()
            print result
        except SyntaxError:
            print traceback.format_exc()

        index += 1
