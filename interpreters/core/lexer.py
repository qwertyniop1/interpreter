'''Abstract lexical analizer module.

Provides `Lexer` class and `LexicalAnalizeError` exception class.
'''
from interpreters.core.token import Token, EOF
from interpreters.core.exceptions import BaseInterpreterError


class LexicalAnalizeError(BaseInterpreterError):
    '''Lexical analize exception.

    Exception thrown when lexical analizer cannot create token from expression.
    '''
    pass


class Lexer(object):
    '''Abstract lexical analizer.

    Class responsing for deriving tokens from string expression. This is a base
    class for lexical analizers. All bussines logic of parsing should be
    written in children classes.

    Attributes:
        position(int): Expression string index of char that will be processed.
        current_char(str): Current char, that will be processed.

    Raises:
        AttributeError: If `expression` is not a non-empty string.
    '''
    def __init__(self, expression):
        if not expression or not isinstance(expression, str):
            raise AttributeError('Lexer expression should be non-empty string')

        self._expression = expression
        self.position = 0
        self.current_char = self._expression[self.position]


    def next_char(self):
        '''Move inner lexer pointer to the next character of expression.

        If expression string is over, sets `current_char` to None.
        '''
        self.position += 1
        if self.position >= len(self._expression):
            self.current_char = None
        else:
            self.current_char = self._expression[self.position]


    def next_token(self):
        '''Get next token.

        Returns one by one tokens derived from expression based on logic,
        described in inhereted Lexer class.

        Returns:
            obj: Token object.

        Raises:
            NotImplementedError: If method called from base abstract class.
            LexicalAnalizeError: If token cannot be created from given
                expression.
        '''
        while self.current_char is not None:
            if self.current_char.isspace():
                self.next_char()
                continue

            token = self.parse_char(self.current_char)
            if token:
                return token

            self.error()

        return Token(EOF, None)


    def error(self):
        '''Throw LexicalAnalizeError with current instance values.'''
        raise LexicalAnalizeError(self._expression, self.position)


    def parse_char(self, char):
        '''Create token according to the `char` value.

        Method should be overriden in inheritor class.

        Args:
            char(str): Character of expression.

        Returns:
            obj: Token object.

        Raises:
            NotImplementedError: If method called from base abstract class.
        '''
        raise NotImplementedError('Cannot execute method of base interpreter class')
