import unittest

from interpreters.core import Lexer


class TestLexer(unittest.TestCase):
    def setUp(self):
        self.expression = '123456789/*-+'
        self.lexer = Lexer(self.expression)


    def test_initialization(self):
        valid_expressions = [
            ' ',
            'abcd',
            '1+2+3*8',
        ]
        for expression in valid_expressions:
            lexer = Lexer(expression)
            self.assertEqual(lexer.position, 0)
            self.assertEqual(lexer.current_char, expression[0])


    def test_initialization_invalid(self):
        invalid_expressions = [
            '',
            None,
            {},
        ]
        for expression in invalid_expressions:
            with self.assertRaisesRegexp(
                AttributeError,
                'Lexer expression should be non-empty string'
            ):
                lexer = Lexer(expression)


    def test_next_char(self):
        for char in self.expression:
            self.assertEqual(self.lexer.current_char, char)
            self.lexer.next_char()

        for _ in range(10):
            self.assertIsNone(self.lexer.current_char)


    def test_next_token(self):
        with self.assertRaisesRegexp(
            NotImplementedError,
            'Cannot execute method of base interpreter class'
        ):
            self.lexer.next_token()


    def test_parse_char(self):
        with self.assertRaisesRegexp(
            NotImplementedError,
            'Cannot execute method of base interpreter class'
        ):
            self.lexer.parse_char(None)


if __name__ == '__main__':
    unittest.main()
