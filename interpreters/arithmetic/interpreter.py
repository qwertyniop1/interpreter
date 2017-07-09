'''Arithmetic interpreter module.

Provides `ArithmeticInterpreter` class.
'''
from interpreters.core import Interpreter
from interpreters.arithmetic import tokens


class ArithmeticInterpreter(Interpreter):
    '''Arithmetic interpreter class.

    Class that produce result from given arithmetic expression with the help
    of `lexer`.

    Attributes:
        lexer(obj): `Lexer` instance.
        current_token(obj): `Token` instance representing current processing
            value.
    '''
    def factor(self):
        '''factor : INTEGER | LPAREN expr RPAREN'''
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
        '''term : factor ((MUL | DIV) factor)*'''
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
        '''Arithmetic expression parser / interpreter.

        >  14 + 2 * 3 - 6 / 2
        17

        expr   : term ((PLUS | MINUS) term)*
        term   : factor ((MUL | DIV) factor)*
        factor : INTEGER
        '''
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
