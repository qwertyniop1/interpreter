'''Core interpreter exceptions.

Exports:
    BaseInterpreterError
'''

class BaseInterpreterError(SyntaxError):
    '''Base Interpreter exception class.

    Extends build-in `SyntaxError` exception by adding visual information about
    error.

    Args:
        expression (str): Expression string that caused an error.
        position (int): Index of current processing char in expression string.
    '''
    def __init__(self, expression, position):
        super(BaseInterpreterError, self).__init__(
            'Invalid syntax at position {}'.format(position + 1)
        )
        self.text = '\t{expression}\n\t{pointer}'.format(
            expression=expression,
            pointer=' ' * position + '^'
        )
