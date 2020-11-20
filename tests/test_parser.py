#!/usr/bin/env python
from .context import truequery

import unittest

class TestParser(unittest.TestCase):

    def test_parse_string(self):
        s = 'hello world'

        expected = truequery.Query()
        expected.text = s

        actual = truequery.parse(s)
        self.assertEqual(actual, expected)

    def test_parse_keyword(self):
        s = 'hello world kw:python'

        expected = truequery.Query()
        expected.text = "hello world"
        expected.keywords.append("python")

        actual = truequery.parse(s)
        self.assertEqual(actual, expected)

    def test_parse_subject(self):
        s = 'hello world sjt:programming'

        expected = truequery.Query()
        expected.text = "hello world"
        expected.subject = truequery.Subject.PROGRAMMING

        actual = truequery.parse(s)
        self.assertEqual(actual, expected)



if __name__ == '__main__':
    unittest.main()
