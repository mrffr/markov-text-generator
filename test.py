#!/usr/bin/env python3

import unittest
import markov_text_gen


class TestMarkovText(unittest.TestCase):
    def test_too_short_input_exception(self):
        with self.assertRaises(SystemExit) as cm:
            markov_text_gen.MarkovText(1, '')
        exc = cm.exception
        self.assertEqual(exc.code, -1)

    def test_start_word(self):
        mc = markov_text_gen.MarkovText(1, 'cat dog cat')
        self.assertEqual(len(mc.chain), 2)


if __name__ == '__main__':
    unittest.main()
