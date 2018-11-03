#!/usr/bin/env python3

import unittest
import markov_text_gen
from random import seed  # seeding rng


class TestMarkovText(unittest.TestCase):
    def test_too_short_input_exception(self):
        with self.assertRaises(SystemExit) as cm:
            markov_text_gen.MarkovText(1, '')
        exc = cm.exception
        self.assertEqual(exc.code, -1)

    def test_depth_arg(self):
        with self.assertRaises(SystemExit) as cm:
            markov_text_gen.MarkovText(0, 'cat dog cat rat log')
        exc = cm.exception
        self.assertEqual(exc.code, -1)

        with self.assertRaises(SystemExit) as cm:
            markov_text_gen.MarkovText(-1, 'cat dog cat rat log')
        exc = cm.exception
        self.assertEqual(exc.code, -1)

    def test_basic(self):
        mc = markov_text_gen.MarkovText(1, 'cat dog')
        self.assertEqual(len(mc.chain), 1)
        self.assertEqual(mc.gen_text(0), '')
        self.assertEqual(mc.gen_text(2), 'cat dog')
        seed(1)
        self.assertEqual(mc.gen_text(1), 'cat')

    def test_sequence(self):
        seed(5)
        mc = markov_text_gen.MarkovText(1, 'cat dog cat')
        self.assertEqual(len(mc.chain), 2)
        self.assertEqual(mc.gen_text(3), 'dog cat dog')
        seed(1)
        self.assertEqual(mc.gen_text(2), 'cat dog')
        seed(1)
        self.assertEqual(mc.gen_text(1), 'cat')


if __name__ == '__main__':
    unittest.main()
