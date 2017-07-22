from src.tokenizer import *
from src.parser import Parser


def main():
    t = Tokenizer()
    p = Parser()
    tokens = t.tokenize('./test/hello_world.uplttoapthw')
    print(p.parse(tokens)[1])

if __name__ == '__main__':
    main()
