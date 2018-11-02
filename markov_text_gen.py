#!/usr/bin/env python3

import argparse
import sys

def main():
    parser = argparse.ArgumentParser(description='Generate text using markov chain method.')
    parser.add_argument('text',type=str)
    parser.add_argument('--depth',type=int, help='Number of words to consider as one chunk')
    args = parser.parse_args()
    return

if __name__ == "__main__":
    main()
    sys.exit(0)
