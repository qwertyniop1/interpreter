'''Token class.

Provides `Token` class and token type constant `EOF`.
'''

# EOF (end-of-file) token is used to indicate that there is no more input left
# for lexical analysis.
EOF = 'EOF'

class Token(object):
    '''Representation of expression token.

    Attributes:
        token_type(str):    Token type using for clasification.
        value(str):         Actual token's value.
    '''
    def __init__(self, token_type, value):
        self.token_type = token_type
        self.value = value

    def __str__(self):
        return 'Token <{}>: "{}"'.format(self.token_type, self.value)

    def __repr__(self):
        return self.__str__()
