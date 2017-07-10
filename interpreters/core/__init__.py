'''Base abstract interpreter.

This module provide abstract base interpreter for evaluating EBNF expressions.

This module exports the following classes:
    Token       Class representing expression unit (token).
    Interpreter Class for evaluating expressions.
    Lexer       Lexical analyzer class.

Developed by Vitali Semenyuk, 2017
'''

from interpreters.core.token import Token, EOF
from interpreters.core.interpreter import Interpreter
from interpreters.core.lexer import Lexer
