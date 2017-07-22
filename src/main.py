from src.tokenizer import *


def main():
    t = Tokenizer()
    tokens = t.tokenize('./test/hello_world.uplttoapthw')
    print(tokens)

if __name__ == '__main__':
    main()
