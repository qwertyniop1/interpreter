import unittest

from interpreters.core import Token


class TestToken(unittest.TestCase):
    def test_str(self):
        token_type = 'TEST'
        value = 'test'
        token = Token(token_type, value)

        self.assertEqual(token.token_type, token_type)
        self.assertEqual(token.value, value)

        self.assertEqual(
            str(token),
            'Token <{}>: "{}"'.format(token_type, value)
        )
        self.assertEqual(repr(token), str(token))
