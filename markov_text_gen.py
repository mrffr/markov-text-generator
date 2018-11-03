#!/usr/bin/env python3

import argparse
import sys
import random

# Markov chain splits the text into a dictionary
# the key is a chunk, the length of which is determined by depth,
# the value is a list of the words which occur after that chunk.
# Text is generated by randomly choosing a chunk and then following
# the chain by choosing from the subsequent words and creating a new chunk.
# The chain ends when we hit a dead end or produce enough text.


class MarkovText():
    '''Generate markov chain and then produce text from it.'''
    def __init__(self, depth, text):
        self.chain = {}
        self.gen_chain(text, depth)

    def gen_ngrams(self, words, depth):
        if len(words) <= depth:
            print("Not enough words for depth", depth)
            sys.exit(-1)

        # generator for list of words in chunks of depth length
        for i in range(len(words) - depth):
            yield [words[i+j] for j in range(depth + 1)]

    def gen_chain(self, text, depth):
        words = text.split()
        for word_l in self.gen_ngrams(words, depth):
            # key is everything but last word
            # value is last word
            key = tuple(word_l[:-1])
            last_word = word_l[-1]

            if key in self.chain:
                self.chain[key].append(last_word)
            else:
                self.chain[key] = [last_word]

    def gen_text(self, text_len, start_word=''):
        '''Generate text of text_len with optional start_word.'''
        wordtuple = random.choice(list(self.chain))
        if start_word != '':
            wordtuple = start_word
        text = ' '.join([str(w) for w in wordtuple])

        for i in range(text_len):
            try:
                word2 = random.choice(list(self.chain[wordtuple]))
                # next tuple is created from last tuple and next word
                # this is then the key for the next lookup
                wordtuple = tuple([w for w in wordtuple][1:] + [word2])
                text += ' ' + str(word2)
            except Exception:
                break

        return text.lstrip()


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

    chain = MarkovText(args.depth, args.input.read())
    print(chain.gen_text(args.len))
    return


if __name__ == "__main__":
    main()
    sys.exit(0)
