'''Abstract interpreter module.

Provides `Interpreter` class and `InterpreterError` exception class.
'''
from interpreters.core.exceptions import BaseInterpreterError


class InterpreterError(BaseInterpreterError):
    '''Interpreter exception.

    Exception thrown when interpreter got unexpected token.
    '''
    pass


class Interpreter(object):
    '''Interpreter class.

    Class that produce result from given expression with the help of `lexer`.

    Attributes:
        lexer(obj): `Lexer` instance.
        current_token(obj): `Token` instance representing current processing
            value.
    '''
    def __init__(self, lexer):
        self.lexer = lexer
        self.current_token = None


    def get(self, token_type):
        '''Get next token.

        Return next token derived from expression after checking its type. If
        type mismatch an exception thrown.

        Args:
            token_type(str): Token type.

        Returns:
            obj: Token object.

        Raises:
            InterpreterError: If interpreter got unexpected token.
            LexicalAnalizeError: If token cannot be created from given
                expression.
        '''
        self.current_token = self.lexer.next_token()

        if self.current_token.token_type == token_type:
            return self.current_token

        self.error()


    def pick(self):
        '''Get next token without changing parser state.

        Return next token derived from expression, but does not extract it
        from expression. Method can be used for checking lexical analizer
        state.

        Returns:
            obj: Token object.

        Raises:
            LexicalAnalizeError: If token cannot be created from given
                expression.
        '''
        previous_position = self.lexer.position
        previous_char = self.lexer.current_char

        self.current_token = self.lexer.next_token()

        self.lexer.position = previous_position
        self.lexer.current_char = previous_char
        return self.current_token


    def parse(self):
        '''Entry point of interpreter.

        Method return result of expression's execution.

        Returns:
            obj: Result of execution.

        Raises:
            SyntaxError: If any sintax error occurred.
        '''
        try:
            return self.expression()
        except SyntaxError as error:
            exception = SyntaxError(error)
            exception.text = error.text
            raise exception


    def error(self):
        '''Throw InterpreterError with current instance values.'''
        raise InterpreterError(self.lexer._expression, self.lexer.position)


    def expression(self):
        '''Execute expression.

        Method descripes rules of expression language.
        Method should be overriden in inheritor class.

        Returns:
            obj: Result of expression's execution.

        Raises:
            NotImplementedError: If method called from base abstract class.
        '''
        raise NotImplementedError('Cannot execute method of base interpreter class')
