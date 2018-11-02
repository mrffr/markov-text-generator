#!/usr/bin/env python3

import argparse
import sys
import random


class MarkovChain():
    def __init__(self, depth):
        self.chain = {}
        self.depth = depth

    def gen_ngrams(self, words):
        if len(words) < self.depth:
            print("not enough words for {0} depth".format(self.depth))
            sys.exit(-1)
        for i in range(len(words) - (self.depth - 1)):
            yield [words[i+j] for j in range(self.depth)]

    def gen_chain(self, text):
        words = [word for word in text]
        for word_l in self.gen_ngrams(words):
            key = tuple(word_l[:-1])
            if key in self.chain:
                self.chain[key].append(word_l[-1])
            else:
                self.chain[key] = [word_l[-1]]

    def gen_text(self, text_len):
        text = ""
        wordtuple = random.choice(list(self.chain))
        text += ' '.join([str(w) for w in wordtuple])
        for i in range(text_len):
            try:
                word2 = random.choice(list(self.chain[wordtuple]))
                wordtuple = tuple([w for w in wordtuple][1:] + [word2])
                text += ' ' + str(word2)
            except Exception:
                break
        return text


def main():
    parser = argparse.ArgumentParser(
        description='Generate text using markov chain method.')

    # default to reading from stdin but can specify input file to read
    parser.add_argument('--input',
                        help='Input file to read.',
                        type=argparse.FileType('r'),
                        default='-')
    parser.add_argument('--len',
                        type=int,
                        help='Length of text to generate.',
                        default=100)
    parser.add_argument('--depth',
                        type=int,
                        help='Number of words to consider as one chunk.',
                        default=1)
    args = parser.parse_args()

    chain = MarkovChain(args.depth)
    chain.gen_chain(args.i)
    print(chain.gen_text(args.len))
    return


if __name__ == "__main__":
    main()
    sys.exit(0)
