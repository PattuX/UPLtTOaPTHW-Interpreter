import re
from src.constants import *


class Tokenizer:

    def __init__(self):
        self.re_day = re.compile("day (\d+)")
        self.re_call_single = re.compile("call prisoner (\w+)\.")
        self.re_call_multiple = re.compile("call prisoners ((\w+, )+\w+)\.")
        self.re_squat = re.compile("squat.")
        self.re_shank = re.compile("shank prisoner (\w+)\.")
        self.re_jump = re.compile("jump to day (\d+)")
        self.re_slap = re.compile("slap prisoner (\w+)\.")
        self.re_eye_contact = re.compile("maintain eye contact with prisoner (\w+) for (\d+) seconds\.")
        self.re_space_or_newline = re.compile("[\n ]")

    def tokenize(self, filename):
        with open(filename, 'r') as src:

            # Structure: {int day: [(int command, str args), ...], ...}
            tokens = {}
            data = src.read().lower()
            i = 0
            curr_day = -1

            # check for correct end
            if not re.search("then he world\.\n*$", data):
                print("Programm must end with 'Then he world'")
                return

            # check for correct start
            first_day = self.re_day.match(data)
            if first_day is not None:
                curr_day = int(first_day.group(1))
                i += len(first_day.group())
            else:
                print("Programm must start by specifying the first day")
                return
            tokens[curr_day] = []

            while i < len(data):

                if self.re_space_or_newline.match(data, i) is not None:
                    i += 1

                elif self.re_day.match(data, i) is not None:
                    match = self.re_day.match(data, i)
                    new_day = int(match.group(1))
                    if new_day in tokens:
                        print("Each dach must only occur once")
                        return
                    else:
                        curr_day = new_day
                        tokens[curr_day] = []
                    i += len(match.group())

                elif self.re_call_single.match(data, i) is not None:
                    match = self.re_call_single.match(data, i)
                    tokens[curr_day].append(tuple([T_Call, match.group(1)]))
                    i += len(match.group())

                elif self.re_call_multiple.match(data, i) is not None:
                    match = self.re_call_multiple.match(data, i)
                    tokens[curr_day].append(tuple([T_Call, match.group(1)]))
                    i += len(match.group())

                elif self.re_squat.match(data, i) is not None:
                    string = self.re_squat.match(data, i).group()
                    tokens[curr_day].append(tuple([T_Squat, ""]))
                    i += len(string)

                elif self.re_shank.match(data, i) is not None:
                    match = self.re_shank.match(data, i)
                    tokens[curr_day].append(tuple([T_Shank, match.group(1)]))
                    i += len(match.group())

                elif self.re_jump.match(data, i) is not None:
                    match = self.re_jump.match(data, i)
                    tokens[curr_day].append(tuple([T_Jump, match.group(1)]))
                    i += len(match.group())

                elif self.re_slap.match(data, i) is not None:
                    match = self.re_slap.match(data, i)
                    tokens[curr_day].append(tuple([T_Slap, match.group(1)]))
                    i += len(match.group())

                elif self.re_eye_contact.match(data, i) is not None:
                    match = self.re_eye_contact.match(data, i)
                    tokens[curr_day].append(tuple([T_EyeContact, str(match.group(1))+", "+str(match.group(2))]))
                    i += len(match.group())

                elif re.match("then he world\.\n*", data[i:]):
                    if re.match("then he world\.\n*$", data[i:]):
                        return tokens
                    else:
                        print("'Then he world.' must only occur at the end of the file.")
                        return

                else:
                    print("unknown command at char "+str(i))
                    return


# debug
def print_tokens(tokens):
    for day in tokens:
        cmds = tokens[day]
        print("Day "+str(day))
        for cmd in cmds:
            print("    Command: "+str(cmd[0]))
            print("        Args: "+str(cmd[1]))
