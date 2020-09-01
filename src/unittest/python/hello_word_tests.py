import unittest


class HelloWorldTest(unittest.TestCase):

    def test_hello_message(self):
        self.assertEqual('foo'.upper(), 'FOO')
