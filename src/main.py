from src.tokenizer import *
from src.parser import Parser
from src.program import Program


def main():
    t = Tokenizer()
    prog = Program()
    tokens = t.tokenize('./test/hello_world.uplttoapthw')
    days = Parser.parse(tokens)
    prog.run(days)

if __name__ == '__main__':
    main()
