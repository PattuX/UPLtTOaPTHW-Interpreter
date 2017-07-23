import random

from prisoner import Prisoner

from constants import *


class Program:

    def __init__(self):
        random.seed()
        self.curr_day = 0
        self.prisoners = {}
        self.clock = 0
        self.output = ""
        self.squatting = False

    def run(self, days: dict):
        while self.curr_day <= max(days.keys()):
            if self.curr_day in days.keys():
                exec(days[self.curr_day])
            self.curr_day += 1
        print(self.output)

    def call(self, *names):
        for name in names:
            if name in self.prisoners:
                print("prisoner "+str(name)+" already exists")
            else:
                self.prisoners[name] = Prisoner()
        self.squatting = False
        for name, p in self.prisoners.items():
            p.respect = 0
            p.fear = 0

    def squat(self):
        self.squatting = True

    def shank(self, name):
        if name in self.prisoners:
            prisoner = self.prisoners[name]
        else:
            print("prisoner "+str(name)+" does not exist")
            return
        self.output += chr(prisoner.respect)
        shanked_respect = prisoner.respect
        del self.prisoners[name]
        for name, p in self.prisoners.items():
            if self.squatting:
                p.respect = min(RESPECT_MAX, shanked_respect*p.respect)
                p.fear = 10

    def jump(self, day):
        # Jump to the day before, because jump is called in exec() (and stops exec) in run(),
        # which is followed by an incrementation of curr_day immediately
        self.curr_day = day - 1

    # :return: did prisoner slap back?
    def slap(self, name) -> bool:
        if name in self.prisoners:
            prisoner = self.prisoners[name]
        else:
            print("prisoner "+str(name)+" does not exist")
            return False
        if random.randint(1, RESPECT_MAX) > prisoner.respect:
            return False
        else:
            return True

    def eye_contact(self, name, time):
        if name in self.prisoners:
            prisoner = self.prisoners[name]
        else:
            print("prisoner "+str(name)+" does not exist")
            return
        for i in range(time):
            if self.squatting:
                prisoner.fear = min(10, prisoner.fear+1)
                prisoner.respect = min(RESPECT_MAX, prisoner.respect+1)
                self.clock += 1
                if self.clock > 9:
                    self.clock_update()

    def clock_update(self):
        self.clock = 0
        for name, p in self.prisoners.items():
            if self.squatting:
                p.respect = max(min(RESPECT_MAX, p.respect+p.fear-5), 0)
                p.fear = max(0, p.fear-1)
