from src.constants import function_name_dict


class Parser:

    def parse(self, tokens):
        for day in tokens:
            func = ""
            for cmd in tokens[day]:
                func += function_name_dict[cmd[0]] + "(" + cmd[1] + ")\n"
            tokens[day] = func
        return tokens
