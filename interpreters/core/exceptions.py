class BaseInterpreterError(SyntaxError):
    def __init__(self, expression, position):
        super(BaseInterpreterError, self).__init__('Invalid syntax at position {}'.format(position + 1))
        self.text = '\t{expression}\n\t{pointer}'.format(
            expression=expression,
            pointer=' ' * position + '^'
        )
