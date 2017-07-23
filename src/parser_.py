from constants import *


class Parser:

    @staticmethod
    def parse(tokens):
        for day in tokens.keys():
            func = "for i in range(1):\n"
            for cmd in tokens[day]:
                if cmd[0] == T_Jump:
                    func += "    self.jump("+cmd[1]+")\n    break\n"
                    break
                elif cmd[0] == T_Slap:
                    func += "    if self.slap("+cmd[1]+"):\n        break\n"
                else:
                    func += "    self."+function_name_dict[cmd[0]] + "(" + cmd[1] + ")\n"
            tokens[day] = func
        return tokens
