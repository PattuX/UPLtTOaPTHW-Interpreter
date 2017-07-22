import argparse
from uplttoapthw.program import Program
from uplttoapthw.parser import Parser
from uplttoapthw.tokenizer import *


def main():
    parser = argparse.ArgumentParser(
        description='Run a "Ultimate Programming Language to Take Over a Prison, Then He World" program!')
    parser.add_argument('source', metavar='src', type=str,
                        help='The "Ultimate Programming Language to Take Over a Prison, Then He World" program to run')
    args = parser.parse_args()

    t = Tokenizer()
    prog = Program()
    tokens = t.tokenize(args.source)
    days = Parser.parse(tokens)
    prog.run(days)

if __name__ == '__main__':
    main()
