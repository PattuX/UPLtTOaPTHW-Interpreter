from tokenizer import *


def main():
    t = Tokenizer()
    print_tokens(t.tokenize('hello_world.uplttoapthw'))

if __name__ == '__main__':
    main()