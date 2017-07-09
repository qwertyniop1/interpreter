'''Arithmetic lexical analizer module.

Provides `ArithmeticLexer` class.
'''
from interpreters.core import Lexer, Token
from interpreters.arithmetic import tokens


class ArithmeticLexer(Lexer):
    '''Arithmetic lexical analizer.

    Class responsing for deriving tokens from string expression. Expression
    should contain only numbers, parentheses and operators +, -, *, / in
    valid order. As result integer number is returned.

    Attributes:
        position(int): Expression string index of char that will be processed.
        current_char(str): Current char, that will be processed.

    Raises:
        AttributeError: If `expression` is not a non-empty string.
    '''
    def integer(self):
        '''Return integer number from expression.

        While `current_char` is digit split them into integer number.

        Returns:
            int: Parsed integer number.
        '''
        result = []

        while self.current_char is not None and self.current_char.isdigit():
            result.append(self.current_char)
            self.next_char()

        return int(''.join(result))


    def parse_char(self, token):
        '''Create token by char(s).

        If `char` is digit or one of +, -, *, /, (, ) returns according token.
        Otherwise returns None.

        Returns:
            obj: Token object.
        '''
        result = None

        if token.isdigit():
            result = Token(tokens.INTEGER, self.integer())
        else:
            if token == '+':
                result = Token(tokens.PLUS, token)
            if token == '-':
                result = Token(tokens.MINUS, token)
            if token == '*':
                result = Token(tokens.ASTERIX, token)
            if token == '/':
                result = Token(tokens.SLASH, token)
            if token == '(':
                result = Token(tokens.OPEN_BRACKET, token)
            if token == ')':
                result = Token(tokens.CLOSE_BRACKET, token)

            self.next_char()

        return result
