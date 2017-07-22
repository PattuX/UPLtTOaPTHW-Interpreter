from uplttoapthw.constants import function_name_dict


class Parser:

    @staticmethod
    def parse(tokens):
        for day in tokens:
            func = ""
            for cmd in tokens[day]:
                func += "self."+function_name_dict[cmd[0]] + "(" + cmd[1] + ")\n"
            tokens[day] = func
        return tokens
