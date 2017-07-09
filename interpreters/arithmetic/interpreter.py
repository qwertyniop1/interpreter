from interpreters.core import Interpreter, Token
from interpreters.arithmetic import tokens


class ArithmeticInterpreter(Interpreter):
    def factor(self):
        if self.pick().token_type == tokens.OPEN_BRACKET:
            self.get(tokens.OPEN_BRACKET)
            result = self.expression()
            self.get(tokens.CLOSE_BRACKET)
            return result
        if self.pick().token_type == tokens.MINUS:
            self.get(tokens.MINUS)
            return -self.factor()
        return int(self.get(tokens.INTEGER).value)


    def term(self):
        result = self.factor()

        while self.pick().token_type in (tokens.ASTERIX, tokens.SLASH):
            operator = self.pick()
            if operator.token_type == tokens.ASTERIX:
                operator = self.get(tokens.ASTERIX)
            else:
                operator = self.get(tokens.SLASH)

            right = self.factor()

            if operator.token_type == tokens.ASTERIX:
                result *= right
            elif operator.token_type == tokens.SLASH:
                result /= right

        return result


    def expression(self):
        result = self.term()

        while self.pick().token_type in (tokens.PLUS, tokens.MINUS):
            operator = self.pick()
            if operator.token_type == tokens.PLUS:
                operator = self.get(tokens.PLUS)
            else:
                operator = self.get(tokens.MINUS)

            right = self.term()

            if operator.token_type == tokens.PLUS:
                result += right
            elif operator.token_type == tokens.MINUS:
                result -= right

        return result
